print("Решение второго задания")


def print_user_data(name, lastname, year, city, mail, phone):
    user_data_dict = {
        'имя': name,
        'фамилия': lastname,
        'год рождения': year,
        'город проживания': city,
        'email': mail,
        'телефон': phone
    }
    for user_feature, user_feature_value in user_data_dict.items():
        print(f"{user_feature}: {user_feature_value}", end='; ')
    return user_data_dict


print("Задайте данные пользователя")
user_name = input('имя: ')
user_lastname = input('фамилия: ')
user_year_of_birth = input('год рождения: ')
user_city = input('город проживания: ')
user_email = input('email: ')
user_phone = input('телефон: ')
data = print_user_data(name=user_name, lastname=user_lastname, year=user_year_of_birth, city=user_city, mail=user_email,
                       phone=user_phone)
