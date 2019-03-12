import re

import constant


class FactoryCallInterface:
    """
    根据伤残等级（disability_grade），初始化对应的实例：
    工亡、1-4级、5-6级、7-10级
    """

    def create(self, disability_grade):
        """
        初始化对应的实例
        :param disability_grade: 0工亡, 1--10与之对应伤残等级
        :return:
        """
        disability_grade = int(disability_grade)
        if disability_grade == 0:
            return


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
        msg = self._replace_sign_of_operation(msg)  # '3×8000'
        msg += ' = ' + cal_result

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

    def _get_single_result(self, event_name):
        """
        获取每个单项的返回值
        :param event_name: 'm_one_off'
        :return: {
            'm_one_off_cal_result': '24000.00',
            'm_one_off_formula_result': '3×8000 = 24000.00'
        }, '24000.00'
        """
        event_name += '{}'
        cal_msg = self.base_data.get(event_name)
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
        m_one_off, m_one_off_num = self._get_single_result('m_one_off')
        m_funeral, m_funeral_num = self._get_single_result('m_funeral')
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
        one_off_result = {
            'm_spouse': m_spouse,
            'm_other': m_other,
            'total': {
                'cal_result': cal_result,
                'formula_result': '{}+{} = {}'.format(m_spouse_num, m_other_num, cal_result)
            }
        }

        return one_off_result
