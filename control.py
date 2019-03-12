import re

import constant


class FactoryCallInterface:
    """
    根据伤残等级（disability_grade），初始化对应的实例：
    工亡、1-4级、5-6级、7-10级
    """

    @classmethod
    def create(cls, disability_grade, **kwargs):
        """
        初始化对应的实例
        :param disability_grade: 0工亡, 1--10与之对应伤残等级
        :return:
        """
        disability_grade = int(disability_grade)
        if disability_grade == 0:
            return DeathCompensation(**kwargs)
        elif disability_grade in (1, 2, 3, 4):
            return One2FourCompensation(disability_grade, **kwargs)
        elif disability_grade in (5, 6):
            return Five2SixCompensation(disability_grade, **kwargs)
        elif disability_grade in (7, 8, 9, 10):
            return Seven2TenCompensation(disability_grade, **kwargs)
        else:
            raise '参数错误'


class BaseCompensation:
    """
    工伤赔偿基类
    """

    def __init__(self, province, city, my_salary):
        """
        :param province: 省
        :param city: 市
        :param my_salary: 本人工资
        """
        self.province = province  # 所选省份
        self.city = city  # 所选城市
        self.my_salary = my_salary  # 本人工资
        self.min_salary = 3000  # 本省最低工资
        self.country_per_income = 12000  # 上年度全国城镇居民人均可支配收入
        self.province_per_salary = 4000  # 本省上年度在岗职工月平均工资
        self.city_per_salary = 4500  # 统筹地区上年度职工月平均工资

    def get_result(self):
        """
        获取结果
        :return:
        """
        one_off_result = self._get_one_off_result()
        monthly_result = self._get_monthly_result()
        result = {
            'one_off_result': one_off_result,
            'monthly_result': monthly_result,
        }

        return result

    def _get_one_off_result(self):
        """
        获取一次性赔偿信息
        :return:
        """
        pass

    def _get_monthly_result(self):
        """
        获取按月赔偿信息
        :return:
        """
        pass

    def _get_base_formula(self, msg):
        """
        获取基础的计算规则，供后续进一步加工
        :param msg: '{shut_down_days}*{my_salary}'
        :return: '3*8000'
        """
        paras_key = re.findall('\{(.*?)\}', msg)  # ['shut_down_days', 'my_salary']
        paras_value = list(map(lambda x: eval('self.' + x), paras_key))  # [self.shut_down_days, self.my_salary]
        paras = dict(zip(paras_key, paras_value))  # {'shut_down_days': self.shut_down_days, ...}
        msg = msg.format(**paras)  # '3*8000'

        return msg

    def _get_formula_result(self, msg):
        """
        解析出计算规则
        :param msg: '{shut_down_days}*{my_salary}'
        :return:  '3×8000 = 24000.00'
        """
        msg = self._get_base_formula(msg)
        cal_result = self._output_number(eval(msg))  # '24000.00'

        # 如果存在max的情况
        if re.search('max', msg):
            # "max(6000*0.2, 3000)"：6000*0.2 < 3000 = 3000
            # "max(6000*0.9, 3000)"：6000*0.9 = 5400
            if re.search('^max', msg):
                num1, num2 = re.findall('^max\((.*?),(.*?)\)', msg)[0]  # [('6000*0.9', ' 3000')]
                if eval(num1) < eval(num2):
                    msg = '{}<{} = {}'.format(num1, num2, cal_result)
                else:
                    msg = '{} = {}'.format(num1, cal_result)
            # "500*max((75-60)*0.7, 15)"，类似于这种的经与产品确定，不返回公式
            else:
                pass
        # 正常的加减乘除
        else:
            msg += ' = ' + cal_result  # '3×8000 = 24000.00'

        msg = self._replace_sign_of_operation(msg)
        return msg

    def _get_cal_result(self, msg):
        """
        获取计算后的结果
        :param msg: '{shut_down_days}*{my_salary}'
        :return: '24000.00'
        """
        msg = self._get_base_formula(msg)
        cal_result = self._output_number(eval(msg))

        return cal_result

    def _replace_sign_of_operation(self, msg):
        """
        替换msg字符串中的 *-->× /-->÷
        :param msg:
        :return:
        """
        return msg.replace("**", "^").replace('*', '\u00D7').replace('/', '\u00F7')

    def _output_number(self, num):
        """
        格式化输出数字为两位小数的字符串
        :param num:
        :return:
        """
        return '{:.2f}'.format(num)

    def _get_single_result(self, event_name, choice=None):
        """
        获取每个单项的返回值
        :param event_name: 'm_one_off'
        :param choice: 二级key
        :return: {
            'm_one_off_cal_result': '24000.00',
            'm_one_off_formula_result': '3×8000 = 24000.00'
        }, '24000.00'
        """
        event_name += '{}'
        if choice:
            cal_msg = self.base_data.get(event_name).get(str(choice))
        else:
            cal_msg = self.base_data.get(event_name)

        # 如果没有对应公式，则返回空
        if not cal_msg:
            return {}, 0

        cal_result = self._get_cal_result(cal_msg)
        formula_result = self._get_formula_result(cal_msg)
        single_result = {
            event_name.format('_cal_result'): cal_result,
            event_name.format('_formula_result'): formula_result,
        }

        return single_result, cal_result


class DeathCompensation(BaseCompensation):
    """
    工亡赔偿计算
    """

    def __init__(self, province, city, my_salary):
        BaseCompensation.__init__(province, city, my_salary)
        self.base_data = constant.WorkCompensationConstant.base_data.get(self.province, {}).get('death')  # 省份对应类型的基础信息

    def _get_one_off_result(self):
        """
        获取一次性赔偿
        :return:
        """
        m_one_off, m_one_off_num = self._get_single_result('m_one_off')  # 一次性工亡补助金
        m_funeral, m_funeral_num = self._get_single_result('m_funeral')  # 丧葬补助金
        cal_result = self._output_number(eval(m_one_off_num) + eval(m_funeral_num))
        one_off_result = {
            'm_one_off': m_one_off,
            'm_funeral': m_funeral,
            'total': {
                'cal_result': cal_result,
                'formula_result': '{}+{} = {}'.format(m_one_off_num, m_funeral_num, cal_result)
            }
        }

        return one_off_result

    def _get_monthly_result(self):
        """
        获取按月赔偿
        :return:
        """
        m_spouse, m_spouse_num = self._get_single_result('m_spouse')
        m_other, m_other_num = self._get_single_result('m_other')
        cal_result = self._output_number(eval(m_spouse_num) + eval(m_other_num))
        monthly_result = {
            'm_spouse': m_spouse,
            'm_other': m_other,
            'total': {
                'cal_result': cal_result,
                'formula_result': '{}+{} = {}'.format(m_spouse_num, m_other_num, cal_result)
            }
        }

        return monthly_result


class HurtBaseCompensation(BaseCompensation):
    """
    1--10级的基类，主要方便初始化工作
    """

    def __init__(self, disability_grade, province, city, my_salary, self_care, is_keep_salary, shut_down_days,
                 disability_begin_date, authenticate_date):
        BaseCompensation.__init__(province, city, my_salary)
        self.disability_grade = int(disability_grade)  # 伤残等级
        self.self_care = int(self_care)  # 出院自理能力：1完全不能自理，2大部分不能自理，3部分不能自理，4全部可以自理
        self.is_keep_salary = int(is_keep_salary)  # 是否停工留薪
        self.shut_down_days = shut_down_days  # 停工留薪期，最多365
        self.disability_begin_date = disability_begin_date  # 工伤发生日
        self.authenticate_date = authenticate_date  # 伤残鉴定日
        key_name = 'level_{}'.format(disability_grade)
        self.base_data = constant.WorkCompensationConstant.base_data.get(self.province, {}).get(key_name)  # 省份对应类型的基础信息


class One2FourCompensation(HurtBaseCompensation):
    """
    1--4级工伤赔偿计算
    """

    def _get_one_off_result(self):
        """
        获取一次性赔偿
        :return:
        """
        m_one_off_disability, m_one_off_disability_num = self._get_single_result('m_one_off_disability')  # 一次性伤残补助金
        m_shut_down, m_shut_down_num = self._get_single_result('m_shut_down', self.is_keep_salary)  # 停工留薪期工资
        m_self_care, m_self_care_num = self._get_single_result('m_self_care', self.self_care)  # 护理费

        # 不计算停工留薪 and 完全可以自理，在结果中不显示“停工留薪期工资”和“护理费”
        cal_result = eval(m_one_off_disability_num)
        formula_result = m_one_off_disability_num
        if m_shut_down_num:
            cal_result += eval(m_shut_down_num)
            formula_result += '+' + m_shut_down_num
        if m_self_care_num:
            cal_result += eval(m_self_care_num)
            formula_result += '+' + m_self_care_num

        cal_result = self._output_number(cal_result)

        one_off_result = {
            'm_one_off_disability': m_one_off_disability,
            'm_shut_down': m_shut_down,
            'm_self_care': m_self_care,
            'total': {
                'cal_result': cal_result,
                'formula_result': '{} = {}'.format(formula_result, cal_result)
            }
        }

        return one_off_result

    def _get_monthly_result(self):
        """
        获取按月赔偿
        :return:
        """
        m_disability, m_disability_num = self._get_single_result('m_disability')
        cal_result = self._output_number(eval(m_disability_num))
        monthly_result = {
            'm_disability': m_disability,
            'total': {
                'cal_result': cal_result,
                'formula_result': '{} = {}'.format(m_disability_num, cal_result)
            }
        }

        return monthly_result
