class WorkCompensationConstant:
    base_data = {
        "上海": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*18",
                "m_one_off_job": "{city_per_salary}*18",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*15",
                "m_one_off_job": "{city_per_salary}*15",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*12",
                "m_one_off_job": "{city_per_salary}*12"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*9",
                "m_one_off_job": "{city_per_salary}*9"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*6",
                "m_one_off_job": "{city_per_salary}*6"
            },
            "level_10": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*3",
                "m_one_off_job": "{city_per_salary}*3"
            }
        },
        "江苏": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "200000.0",
                "m_one_off_job": "95000.0",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "160000.0",
                "m_one_off_job": "85000.0",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "120000.0",
                "m_one_off_job": "45000.0"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "80000.0",
                "m_one_off_job": "35000.0"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "50000.0",
                "m_one_off_job": "25000.0"
            },
            "level_10": {
                "m_one_off_job": "15000.0",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "30000.0"
            }
        },
        "浙江": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{province_per_salary}*30",
                "m_one_off_job": "{province_per_salary}*30",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{province_per_salary}*25",
                "m_one_off_job": "{province_per_salary}*25",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{province_per_salary}*10",
                "m_one_off_job": "{province_per_salary}*10"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{province_per_salary}*7",
                "m_one_off_job": "{province_per_salary}*7"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{province_per_salary}*4",
                "m_one_off_job": "{province_per_salary}*4"
            },
            "level_10": {
                "m_one_off_job": "{province_per_salary}*2",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{province_per_salary}*2"
            }
        },
        "安徽": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*24",
                "m_one_off_job": "{city_per_salary}*40",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*18",
                "m_one_off_job": "{city_per_salary}*34",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*20"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*8",
                "m_one_off_job": "{city_per_salary}*15"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*6",
                "m_one_off_job": "{city_per_salary}*10"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*5",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*4"
            }
        },
        "福建": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*max(({per_age}-{my_age})*0.7, 15)",
                "m_one_off_job": "{city_per_salary}*max(({per_age}-{my_age})*0.7, 15)",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*max(({per_age}-{my_age})*0.6, 15)",
                "m_one_off_job": "{city_per_salary}*max(({per_age}-{my_age})*0.6, 15)",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*max(({per_age}-{my_age})*0.4, 10)",
                "m_one_off_job": "{city_per_salary}*max(({per_age}-{my_age})*0.4, 10)"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*max(({per_age}-{my_age})*0.3, 10)",
                "m_one_off_job": "{city_per_salary}*max(({per_age}-{my_age})*0.3, 10)"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*max(({per_age}-{my_age})*0.2, 5)",
                "m_one_off_job": "{city_per_salary}*max(({per_age}-{my_age})*0.2, 5)"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*max(({per_age}-{my_age})*0.1, 3)",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*max(({per_age}-{my_age})*0.1, 3)"
            }
        },
        "山东": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*22",
                "m_one_off_job": "{city_per_salary}*36",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*18",
                "m_one_off_job": "{city_per_salary}*30",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*13",
                "m_one_off_job": "{city_per_salary}*20"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*16"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*7",
                "m_one_off_job": "{city_per_salary}*12"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*8",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*4"
            }
        },
        "广东": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*10",
                "m_one_off_job": "{my_salary}*50",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*8",
                "m_one_off_job": "{my_salary}*40",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*6",
                "m_one_off_job": "{my_salary}*25"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*4",
                "m_one_off_job": "{my_salary}*15"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*2",
                "m_one_off_job": "{my_salary}*8"
            },
            "level_10": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*1",
                "m_one_off_job": "{my_salary}*4"
            }
        },
        "广西": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*20",
                "m_one_off_job": "{my_salary}*18",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*18",
                "m_one_off_job": "{my_salary}*16",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*15",
                "m_one_off_job": "{my_salary}*13"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*13",
                "m_one_off_job": "{my_salary}*11"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*11",
                "m_one_off_job": "{my_salary}*19"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*7",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*9"
            }
        },
        "海南": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{province_per_salary}*18",
                "m_one_off_job": "{my_salary}*40",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{province_per_salary}*16",
                "m_one_off_job": "{my_salary}*30",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{province_per_salary}*14",
                "m_one_off_job": "{my_salary}*20"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{province_per_salary}*12",
                "m_one_off_job": "{my_salary}*16"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{province_per_salary}*10",
                "m_one_off_job": "{my_salary}*12"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*9",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{province_per_salary}*8"
            }
        },
        "河南": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*16",
                "m_one_off_job": "{city_per_salary}*56",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*14",
                "m_one_off_job": "{city_per_salary}*46",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*12",
                "m_one_off_job": "{city_per_salary}*36"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*26"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*8",
                "m_one_off_job": "{city_per_salary}*16"
            },
            "level_10": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*6",
                "m_one_off_job": "{city_per_salary}*6"
            }
        },
        "湖北": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*22",
                "m_one_off_job": "{city_per_salary}*34",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*18",
                "m_one_off_job": "{city_per_salary}*28",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*12",
                "m_one_off_job": "{city_per_salary}*20"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*16"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*8",
                "m_one_off_job": "{city_per_salary}*12"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*8",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*6"
            }
        },
        "湖南": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*24",
                "m_one_off_job": "{my_salary}*36",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*18",
                "m_one_off_job": "{my_salary}*30",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*15",
                "m_one_off_job": "{my_salary}*15"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*10",
                "m_one_off_job": "{my_salary}*10"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*8",
                "m_one_off_job": "{my_salary}*8"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*6",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*6"
            }
        },
        "江西": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*20",
                "m_one_off_job": "{my_salary}*32",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*17",
                "m_one_off_job": "{my_salary}*28",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*13",
                "m_one_off_job": "{my_salary}*25"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*10",
                "m_one_off_job": "{my_salary}*21"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*7",
                "m_one_off_job": "{my_salary}*17"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*13",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*4"
            }
        },
        "北京": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*15",
                "m_one_off_job": "{city_per_salary}*15",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*12.5",
                "m_one_off_job": "{city_per_salary}*12.5",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*10"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*7.5",
                "m_one_off_job": "{city_per_salary}*7.5"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*5",
                "m_one_off_job": "{city_per_salary}*5"
            },
            "level_10": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*2.5",
                "m_one_off_job": "{city_per_salary}*2.5"
            }
        },
        "天津": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*12",
                "m_one_off_job": "{city_per_salary}*18",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*15",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*8",
                "m_one_off_job": "{city_per_salary}*12"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*6",
                "m_one_off_job": "{city_per_salary}*9"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*4",
                "m_one_off_job": "{city_per_salary}*6"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*3",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*2"
            }
        },
        "河北": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{province_per_salary}*44",
                "m_one_off_job": "{province_per_salary}*22",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{province_per_salary}*38",
                "m_one_off_job": "{province_per_salary}*16",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{province_per_salary}*26",
                "m_one_off_job": "{province_per_salary}*10"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{province_per_salary}*20",
                "m_one_off_job": "{province_per_salary}*8"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{province_per_salary}*14",
                "m_one_off_job": "{province_per_salary}*6"
            },
            "level_10": {
                "m_one_off_job": "{province_per_salary}*4",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{province_per_salary}*8"
            }
        },
        "山西": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*36",
                "m_one_off_job": "{my_salary}*24",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*33",
                "m_one_off_job": "{my_salary}*21",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*24",
                "m_one_off_job": "{my_salary}*15"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*21",
                "m_one_off_job": "{my_salary}*12"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*18",
                "m_one_off_job": "{my_salary}*9"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*6",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*15"
            }
        },
        "内蒙古": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*26",
                "m_one_off_job": "{city_per_salary}*26",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*23",
                "m_one_off_job": "{city_per_salary}*23",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*16",
                "m_one_off_job": "{city_per_salary}*16"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*13",
                "m_one_off_job": "{city_per_salary}*13"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*10"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*7",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*7"
            }
        },
        "陕西": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*24",
                "m_one_off_job": "{city_per_salary}*21",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*24",
                "m_one_off_job": "{city_per_salary}*21",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*15",
                "m_one_off_job": "{city_per_salary}*15"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*12",
                "m_one_off_job": "{city_per_salary}*12"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*9",
                "m_one_off_job": "{city_per_salary}*9"
            },
            "level_10": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*6",
                "m_one_off_job": "{city_per_salary}*6"
            }
        },
        "甘肃": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*18",
                "m_one_off_job": "{my_salary}*18",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*16",
                "m_one_off_job": "{my_salary}*16",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*13",
                "m_one_off_job": "{my_salary}*13"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*11",
                "m_one_off_job": "{my_salary}*11"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*9",
                "m_one_off_job": "{my_salary}*9"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*7",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*7"
            }
        },
        "青海": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*15",
                "m_one_off_job": "{my_salary}*15",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*13.5",
                "m_one_off_job": "{my_salary}*13.5",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*12",
                "m_one_off_job": "{my_salary}*12"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*10.5",
                "m_one_off_job": "{my_salary}*10.5"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*9",
                "m_one_off_job": "{my_salary}*9"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*7.5",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*7.5"
            }
        },
        "新疆": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*11",
                "m_one_off_job": "{city_per_salary}*27",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*24",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*9",
                "m_one_off_job": "{city_per_salary}*21"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*8",
                "m_one_off_job": "{city_per_salary}*18"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*7",
                "m_one_off_job": "{city_per_salary}*15"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*12",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*6"
            }
        },
        "宁夏": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*22",
                "m_one_off_job": "{my_salary}*22",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*19",
                "m_one_off_job": "{my_salary}*19",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*15",
                "m_one_off_job": "{my_salary}*15"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*12",
                "m_one_off_job": "{my_salary}*12"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*9",
                "m_one_off_job": "{my_salary}*9"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*6",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*6"
            }
        },
        "重庆": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*12",
                "m_one_off_job": "{city_per_salary}*60",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*48",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*8",
                "m_one_off_job": "{city_per_salary}*15"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*6",
                "m_one_off_job": "{city_per_salary}*12"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*4",
                "m_one_off_job": "{city_per_salary}*9"
            },
            "level_10": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*2",
                "m_one_off_job": "{city_per_salary}*6"
            }
        },
        "四川": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*10",
                "m_one_off_job": "{city_per_salary}*26"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*8",
                "m_one_off_job": "{city_per_salary}*18"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*6",
                "m_one_off_job": "{city_per_salary}*10"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*6",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*4"
            }
        },
        "贵州": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*36",
                "m_one_off_job": "{city_per_salary}*36",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*26",
                "m_one_off_job": "{city_per_salary}*26",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*12",
                "m_one_off_job": "{city_per_salary}*12"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*9",
                "m_one_off_job": "{city_per_salary}*9"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*6",
                "m_one_off_job": "{city_per_salary}*6"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*3",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*3"
            }
        },
        "云南": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*15",
                "m_one_off_job": "{city_per_salary}*33",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*13",
                "m_one_off_job": "{city_per_salary}*29",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*8",
                "m_one_off_job": "{city_per_salary}*22"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*6",
                "m_one_off_job": "{city_per_salary}*18"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*3",
                "m_one_off_job": "{city_per_salary}*13"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*7",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*2"
            }
        },
        "西藏": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*23",
                "m_one_off_job": "{city_per_salary}*25",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*19",
                "m_one_off_job": "{city_per_salary}*21",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*14",
                "m_one_off_job": "{city_per_salary}*16"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*12",
                "m_one_off_job": "{city_per_salary}*13"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*9",
                "m_one_off_job": "{city_per_salary}*11"
            },
            "level_10": {
                "m_one_off_job": "{city_per_salary}*7",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*5"
            }
        },
        "辽宁": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{city_per_salary}*18",
                "m_one_off_job": "{city_per_salary}*28",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{city_per_salary}*16",
                "m_one_off_job": "{city_per_salary}*24",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{city_per_salary}*13",
                "m_one_off_job": "{city_per_salary}*20"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{city_per_salary}*11",
                "m_one_off_job": "{city_per_salary}*16"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{city_per_salary}*9",
                "m_one_off_job": "{city_per_salary}*12"
            },
            "level_10": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{city_per_salary}*7",
                "m_one_off_job": "{city_per_salary}*8"
            }
        },
        "吉林": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*18",
                "m_one_off_job": "{my_salary}*16",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*16",
                "m_one_off_job": "{my_salary}*14",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*13",
                "m_one_off_job": "{my_salary}*11"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*11",
                "m_one_off_job": "{my_salary}*9"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*9",
                "m_one_off_job": "{my_salary}*7"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*5",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*7"
            }
        },
        "黑龙江": {
            "death": {
                "m_one_off": "{country_per_income}*20",
                "m_funeral": "{city_per_salary}*6",
                "m_spouse": "{my_salary}*40%",
                "m_other": "{my_salary}*30%"
            },
            "level_1": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*27",
                "m_disability": "max({my_salary}*90%, {min_salary})"
            },
            "level_2": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*25",
                "m_disability": "max({my_salary}*85%, {min_salary})"
            },
            "level_3": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*23",
                "m_disability": "max({my_salary}*80%, {min_salary})"
            },
            "level_4": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*21",
                "m_disability": "max({my_salary}*75%, {min_salary})"
            },
            "level_5": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*18",
                "m_one_off_medical": "{my_salary}*30",
                "m_one_off_job": "{my_salary}*16",
                "m_disability": "max({my_salary}*70%, {min_salary})"
            },
            "level_6": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*16",
                "m_one_off_medical": "{my_salary}*25",
                "m_one_off_job": "{my_salary}*14",
                "m_disability": "max({my_salary}*60%, {min_salary})"
            },
            "level_7": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*13",
                "m_one_off_medical": "{my_salary}*20",
                "m_one_off_job": "{my_salary}*12"
            },
            "level_8": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*11",
                "m_one_off_medical": "{my_salary}*15",
                "m_one_off_job": "{my_salary}*10"
            },
            "level_9": {
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*9",
                "m_one_off_medical": "{my_salary}*10",
                "m_one_off_job": "{my_salary}*8"
            },
            "level_10": {
                "m_one_off_job": "{my_salary}*6",
                "m_shut_down": {
                    "1": "{shut_down_days}*{my_salary}/21.75",
                    "0": "({disability_begin_date}-{authenticate_date})*{my_salary}/21.75"
                },
                "m_self_care": {
                    "1": "{city_per_salary}*50%",
                    "2": "{city_per_salary}*40%",
                    "3": "{city_per_salary}*30%"
                },
                "m_one_off_disability": "{my_salary}*7",
                "m_one_off_medical": "{my_salary}*5"
            }
        }
    }

    # 出院自理能力
    not_care = 1  # 完全不能自理
    most_not_care = 2  # 大部分不能自理
    few_not_care = 3  # 部分不能自理
    all_care = 4  # 全部可以自理

    # 是否停工留薪
    keep_salary = 1  # 是
    no_keep_salary = 0  # 否
    no_cal = 2  # 不计算
