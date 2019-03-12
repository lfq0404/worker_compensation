import control

if __name__ == '__main__':
    # # 工亡
    # disability_grade = 0
    # kwargs = {
    #     'province': '福建',
    #     'city': '厦门',  # 在此demo中的城市没有用，在项目中是根据city获取对应城市的月平均工资等信息
    #     'my_salary': 5000,
    # }
    # new_compensation = control.FactoryCallInterface.create(disability_grade, **kwargs)
    # result = new_compensation.get_result()
    # print(result)

    # # 1--4级
    # disability_grade = 1
    # kwargs = {
    #     'province': '福建',
    #     'city': '厦门',  # 在此demo中的城市没有用，在项目中是根据city获取对应城市的月平均工资等信息
    #     'my_salary': 5000,
    #     'self_care': 1,
    #     'is_keep_salary': 0,
    #     'shut_down_days': 200,
    #     'disability_begin_date': '2019-1-1',
    #     'authenticate_date': '2019-3-12',
    # }
    # new_compensation = control.FactoryCallInterface.create(disability_grade, **kwargs)
    # result = new_compensation.get_result()
    # print(result)

    # # 5--6级
    # disability_grade = 5
    # kwargs = {
    #     'province': '福建',
    #     'city': '厦门',  # 在此demo中的城市没有用，在项目中是根据city获取对应城市的月平均工资等信息
    #     'my_salary': 5000,
    #     'self_care': 1,
    #     'is_keep_salary': 0,
    #     'shut_down_days': 200,
    #     'disability_begin_date': '2019-1-1',
    #     'authenticate_date': '2019-3-12',
    #     'per_age': 74,
    #     'my_age': 50,
    # }
    # new_compensation = control.FactoryCallInterface.create(disability_grade, **kwargs)
    # result = new_compensation.get_result()
    # print(result)

    # 7--10级
    disability_grade = 10
    kwargs = {
        'province': '福建',
        'city': '厦门',  # 在此demo中的城市没有用，在项目中是根据city获取对应城市的月平均工资等信息
        'my_salary': 5000,
        'self_care': 1,
        'is_keep_salary': 0,
        'shut_down_days': 200,
        'disability_begin_date': '2019-1-1',
        'authenticate_date': '2019-3-12',
        'per_age': 74,
        'my_age': 50,
    }
    new_compensation = control.FactoryCallInterface.create(disability_grade, **kwargs)
    result = new_compensation.get_result()
    print(result)
