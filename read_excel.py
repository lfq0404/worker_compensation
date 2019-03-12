import xlrd
import json
import re

data = xlrd.open_workbook('A工伤赔偿计算.xlsx')

province_name = ''
result = {}

for sheet_name in ['华东地区', '华南地区', '华中地区', '华北地区', '西北地区', '西南地区', '东北地区']:
    table = data.sheet_by_name(sheet_name)
    nrows = table.nrows
    base_level = ''
    m_type = ''

    for i in range(nrows):
        row_values = table.row_values(i)
        m_type = row_values[1] if row_values[1] else m_type

        # 获取省份名
        if '工伤赔偿' in row_values[0]:
            new_province_name = row_values[0].replace('工伤赔偿', '')
            if new_province_name != province_name:
                if province_name:
                    result[province_name]['death'] = death
                    result[province_name]['level_1'] = level_1
                    result[province_name]['level_2'] = level_2
                    result[province_name]['level_3'] = level_3
                    result[province_name]['level_4'] = level_4
                    result[province_name]['level_5'] = level_5
                    result[province_name]['level_6'] = level_6
                    result[province_name]['level_7'] = level_7
                    result[province_name]['level_8'] = level_8
                    result[province_name]['level_9'] = level_9
                    result[province_name]['level_10'] = level_10
                province_name = new_province_name
            result[province_name] = {}
            death, level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9, level_10 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

        now_level = row_values[0]
        if now_level and base_level != now_level and now_level in ['工亡', '1-10级', '1级', '2级', '3级', '4级', '5级',
                                                                   '6级', '7级', '8级', '9级', '10级']:
            base_level = now_level
        if base_level == '工亡':
            if '一次性工亡补助金' in m_type:
                death['m_one_off'] = row_values[2]
            elif '丧葬补助金' in m_type:
                death['m_funeral'] = row_values[2]
            elif '供养亲属抚恤金' in m_type:
                if row_values[2] == '配偶':
                    death['m_spouse'] = row_values[3]
                else:
                    death['m_other'] = row_values[3]
        elif base_level == '1-10级':
            if '停工留薪期工资' in m_type:
                if row_values[2] == '有停工留薪期':
                    m_shut_down_1 = row_values[3]
                    for level_temp in [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9,
                                       level_10]:
                        level_temp['m_shut_down'] = {
                            1: m_shut_down_1,
                        }
                elif row_values[2] == '没有停工留薪期':
                    m_shut_down_0 = row_values[3]
                    for level_temp in [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9,
                                       level_10]:
                        level_temp['m_shut_down'][0] = m_shut_down_0
            elif '出院后的护理费' in m_type:
                if row_values[2] == '完全不能自理':
                    not_care = row_values[3]
                    for level_temp in [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9,
                                       level_10]:
                        level_temp['m_self_care'] = {
                            1: not_care,
                        }
                elif row_values[2] == '大部分不能自理':
                    most_not_care = row_values[3]
                    for level_temp in [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9,
                                       level_10]:
                        level_temp['m_self_care'][2] = most_not_care
                elif row_values[2] == '部分不能自理':
                    few_not_care = row_values[3]
                    for level_temp in [level_1, level_2, level_3, level_4, level_5, level_6, level_7, level_8, level_9,
                                       level_10]:
                        level_temp['m_self_care'][3] = few_not_care
        elif base_level in ['1级']:
            if m_type == '一次性伤残补助金':
                level_1['m_one_off_disability'] = row_values[2]
            elif m_type == '伤残津贴':
                level_1['m_disability'] = row_values[2]
        elif base_level in ['2级']:
            if m_type == '一次性伤残补助金':
                level_2['m_one_off_disability'] = row_values[2]
            elif m_type == '伤残津贴':
                level_2['m_disability'] = row_values[2]
        elif base_level in ['3级']:
            if m_type == '一次性伤残补助金':
                level_3['m_one_off_disability'] = row_values[2]
            elif m_type == '伤残津贴':
                level_3['m_disability'] = row_values[2]
        elif base_level in ['4级']:
            if m_type == '一次性伤残补助金':
                level_4['m_one_off_disability'] = row_values[2]
            elif m_type == '伤残津贴':
                level_4['m_disability'] = row_values[2]
        elif base_level in ['5级']:
            if m_type == '一次性伤残补助金':
                level_5['m_one_off_disability'] = row_values[2]
            elif m_type == '一次性工伤医疗补助金':
                level_5['m_one_off_medical'] = row_values[2]
            elif m_type == '一次性伤残就业补助金':
                level_5['m_one_off_job'] = row_values[2]
            elif m_type == '伤残津贴':
                level_5['m_disability'] = row_values[2]
        elif base_level in ['6级']:
            if m_type == '一次性伤残补助金':
                level_6['m_one_off_disability'] = row_values[2]
            elif m_type == '一次性工伤医疗补助金':
                level_6['m_one_off_medical'] = row_values[2]
            elif m_type == '一次性伤残就业补助金':
                level_6['m_one_off_job'] = row_values[2]
            elif m_type == '伤残津贴':
                level_6['m_disability'] = row_values[2]
        elif base_level in ['7级']:
            if m_type == '一次性伤残补助金':
                level_7['m_one_off_disability'] = row_values[2]
            elif m_type == '一次性工伤医疗补助金':
                level_7['m_one_off_medical'] = row_values[2]
            elif m_type == '一次性伤残就业补助金':
                level_7['m_one_off_job'] = row_values[2]
        elif base_level in ['8级']:
            if m_type == '一次性伤残补助金':
                level_8['m_one_off_disability'] = row_values[2]
            elif m_type == '一次性工伤医疗补助金':
                level_8['m_one_off_medical'] = row_values[2]
            elif m_type == '一次性伤残就业补助金':
                level_8['m_one_off_job'] = row_values[2]
        elif base_level in ['9级']:
            if m_type == '一次性伤残补助金':
                level_9['m_one_off_disability'] = row_values[2]
            elif m_type == '一次性工伤医疗补助金':
                level_9['m_one_off_medical'] = row_values[2]
            elif m_type == '一次性伤残就业补助金':
                level_9['m_one_off_job'] = row_values[2]
        elif base_level in ['10级']:
            if m_type == '一次性伤残补助金':
                level_10['m_one_off_disability'] = row_values[2]
            elif m_type == '一次性工伤医疗补助金':
                level_10['m_one_off_medical'] = row_values[2]
            elif m_type == '一次性伤残就业补助金':
                level_10['m_one_off_job'] = row_values[2]
        else:
            if (base_level not in ['', '伤残级别']) or ('工伤赔偿' not in base_level):
                print('没有纳入计算的base_level:', base_level)

# 记录最后一个循环的省份
result[province_name]['death'] = death
result[province_name]['level_1'] = level_1
result[province_name]['level_2'] = level_2
result[province_name]['level_3'] = level_3
result[province_name]['level_4'] = level_4
result[province_name]['level_5'] = level_5
result[province_name]['level_6'] = level_6
result[province_name]['level_7'] = level_7
result[province_name]['level_8'] = level_8
result[province_name]['level_9'] = level_9
result[province_name]['level_10'] = level_10

# 数据清洗
with open('result.txt', 'w') as f:
    result_str = json.dumps(result).encode('utf-8').decode('unicode_escape')
    result_str = result_str \
        .replace('本人工资', '{my_salary}') \
        .replace('上年度全国城镇居民人均可支配收入', '{country_per_income}') \
        .replace('统筹地区（市）上年度职工月平均工资', '{city_per_salary}*') \
        .replace('停工留薪期', '{shut_down_days}') \
        .replace('伤残鉴定之日－工伤发生之日', '{disability_begin_date}-{authenticate_date}') \
        .replace('倍', '') \
        .replace('上年度全市职工月平均工资', '{city_per_salary}') \
        .replace('个月', '') \
        .replace('月工资', '{my_salary}') \
        .replace('统筹地区上年度职工月平均工资', '{city_per_salary}') \
        .replace('本市上年度职工月平均工资', '{city_per_salary}') \
        .replace('本省上年度在岗职工月平均工资', '{province_per_salary}') \
        .replace('上年度全省在岗职工月平均工资', '{province_per_salary}') \
        .replace('本省上一年度职工月平均工资', '{province_per_salary}') \
        .replace('统筹地区最后一次公布的人口平均预期寿命－年龄', '{per_age}-{my_age}') \
        .replace('，按月给', '') \
        .replace('。', '') \
        .replace('**', '*')
    result_str = re.sub(': \"([a-z_0-9%\{\}\*]*?)，按月支付，不足最低工资按最低工资算\"',
                        lambda x: ': "max({}, {{min_salary}})"'.format(x.group(1)),
                        result_str)
    result_str = re.sub(': "([0-9\.]*?)万"', lambda x: ': "{}"'.format(float(x.group(1)) * 10000), result_str)
    result_str = re.sub('(\(\{per_age\}-\{my_age\}\)\*.*?)\(不满一年按一年计算\)【低于(.*?)的.*?】',
                        lambda x: 'max({}, {})'.format(x.group(1), x.group(2)), result_str)

    f.write(result_str)
