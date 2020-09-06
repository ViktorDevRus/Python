# task6
print("Решение шестого задания")

products_list = []
print("Введите данные по товарам")
agreement = True
i = 1
while agreement:
    product_name = input("название: ")
    product_price = float(input("цена: "))
    product_number = int(input("количество: "))
    product_measure = input("единица измерения: ")
    product_dict = {'название': product_name, 'цена': product_price, 'количество': product_number,
                    'eд': product_measure}
    product_tuple = (i, product_dict)
    products_list.append(product_tuple)
    i += 1
    agreement = input("Хотите добавить ещё один товар? y - Да, n - Нет: ")
    agreement = True if agreement == 'y' else False
print('Готовая структура товаров: ')
print(products_list)
# Аналитика товаров
product_name_list = []
product_price_list = []
product_number_list = []
product_measure_list = []
for el in range(len(products_list)):
    product_name_list.append(products_list[el][1].get('название'))
    product_price_list.append(products_list[el][1].get('цена'))
    product_number_list.append(products_list[el][1].get('количество'))
    product_measure_list.append(products_list[el][1].get('eд'))
product_measure_list = list(set(product_measure_list))
analytics = {
    'название': product_name_list,
    'цена': product_price_list,
    'количество': product_number_list,
    'eд': product_measure_list
   }
print('Аналитика товаров: ')
print(analytics)
