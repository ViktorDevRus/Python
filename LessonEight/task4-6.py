"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
 будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
 классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
 каждого типа оргтехники.
 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
 определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
  данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""
import os


class ValidateTypeError(Exception):
    def __init__(self, text: str):
        self.txt = text

    @classmethod
    def check_user_input(cls, arg: str):
        if arg.isdigit():
            return True
        else:
            raise ValidateTypeError('Вы указали не целое положительное число. Повторите ввод значения:')


class Document:
    __type: str

    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content


class PaperDocument(Document):
    def __init__(self, name: str, content: str):
        super().__init__(name, content)
        self.__type = 'paper'


class DigitalDocument(Document):
    def __init__(self, name: str, content: str):
        super().__init__(name, content)
        self.__type = 'digital'


class Department:
    department_equipment_type_dict = {
        'printers': 'принтеры',
        'scanners': 'сканеры',
        'copiers': 'ксероксы'
    }

    def __init__(self, name: str):
        self.name = name
        self.resource = {
            'printers': {},
            'scanners': {},
            'copiers': {},
        }

    def print_resource(self):
        print(f'Оргтехника на балансе отдела {self.name}: ')
        for type_en, type_rus in self.department_equipment_type_dict.items():
            print(f'{type_rus}: ')
            for mark, mark_count in self.resource[type_en].items():
                print(f'{mark}: {mark_count}')


class CountingDep(Department):
    def __init__(self):
        super().__init__('Бухгалтерия')


class PersonnelServiceDep(Department):
    def __init__(self):
        super().__init__('Кадровая служба')


class OfficeEquipmentWarehouse:
    __office_equipment_type_dict = {
        'printers': 'принтеры',
        'scanners': 'сканеры',
        'copiers': 'ксероксы'
    }

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.resource = {
            'printers': {},
            'scanners': {},
            'copiers': {},
        }

    def __str__(self):
        print('Складской запас оргтехники: ')
        for type_en, type_rus in self.__office_equipment_type_dict.items():
            print(f'{type_rus}: ')
            for mark, mark_count in self.resource[type_en].items():
                print(f'{mark}: {mark_count}')


    def acceptance_of_purchased_office_equipment_to_warehouse(self):
        for type_en, type_rus in self.__office_equipment_type_dict.items():
            type_accept = input(f'Добавить {type_rus} на склад? y - да, n - нет: ')
            while type_accept.lower() not in ('y', 'n'):
                type_accept = input(f'Некорректный ответ [допустимо указать y (да) либо n (нет)]. Добавить {type_rus} на склад? ')
            if type_accept.lower() == 'n':
                continue
            while type_accept:
                mark = input('Укажите модель/наименование: ')
                validate_ok = False
                count = 0
                while not validate_ok:
                    count_str = input('Укажите количество (шт.) (значение должно быть больше либо равно 1: ')
                    try:
                        if ValidateTypeError.check_user_input(count_str):
                            count = abs(int(count_str))
                            if count >= 1:
                                validate_ok = True
                                break
                            else:
                                print('Неверное значение! ', end='')
                    except ValidateTypeError as error_obj:
                        print(error_obj.txt)
                        continue
                self.resource[type_en][mark] = count
                mark_accept = input(f'Добавить ещё модель/наименование? y - да, n - нет: ')
                while mark_accept.lower() not in ('y', 'n'):
                    mark_accept = input('Некорректный ответ [допустимо указать y (да) либо n (нет)]. Добавить ещё модель/наименование? ')
                if mark_accept.lower() == 'n':
                    break
        print('Добавление завершено.')
        self.__str__()

    def pass_from_warehouse_to_department(self, dept: Department):
        print('Доступная оргтехника для выдачи: ')
        equipment_type_tuple = tuple(enumerate(self.__office_equipment_type_dict.items(), 1))
        for key, value in equipment_type_tuple:
            print(f'{key}: {value[1]}')
        validate_ok = False
        choice_type = 0
        while not validate_ok:
            choice_type_input = input('Выберите нужный вариант цифрой: ')
            try:
                if ValidateTypeError.check_user_input(choice_type_input):
                    choice_type = abs(int(choice_type_input))
                    if choice_type  in range(1, len(self.resource.keys()) + 1):
                        validate_ok = True
                        break
                    else:
                        print('Неверное значение! ', end='')
            except ValidateTypeError as error_obj:
                print(error_obj.txt)
                continue
        choice_type_str = equipment_type_tuple[choice_type-1][1][0]
        if self.resource.get(choice_type_str) != {}:
            print('Доступные модели/наименования для выбранного типа оргтехники: ')
            equipment_mark_tuple = tuple(enumerate(self.resource.get(choice_type_str).items(), 1))
            for key, value in equipment_mark_tuple:
                if value[1] > 0:
                    print(f'{key}: {value[0]}, остаток: {value[1]}')
            validate_ok = False
            choice_mark = 0
            while not validate_ok:
                choice_mark_input = input('Выберите нужный вариант цифрой: ')
                try:
                    if ValidateTypeError.check_user_input(choice_mark_input):
                        choice_mark = abs(int(choice_mark_input))
                        if choice_mark in range(1, len(self.resource.get(choice_type_str).keys()) + 1):
                            validate_ok = True
                            break
                        else:
                            print('Неверное значение! ', end='')
                except ValidateTypeError as error_obj:
                    print(error_obj.txt)
                    continue
            choice_mark_str = equipment_mark_tuple[choice_mark - 1][1][0]
            validate_ok = False
            count = 0
            while not validate_ok:
                count_input = input('Укажите количество аппаратов для выдачи (значение должно быть больше либо равно 1 и меньше либо равно фактическому количеству аппаратов): ')
                try:
                    if ValidateTypeError.check_user_input(count_input):
                        count = abs(int(count_input))
                        if count in range(1, equipment_mark_tuple[choice_mark - 1][1][1] + 1):
                            validate_ok = True
                            break
                        else:
                            print('Неверное значение! ', end='')
                except ValidateTypeError as error_obj:
                    print(error_obj.txt)
                    continue
            if dept.resource[choice_type_str].get(choice_mark_str) is None:
                dept.resource[choice_type_str][choice_mark_str] = count
            else:
                dept.resource[choice_type_str][choice_mark_str] = dept.resource[choice_type_str].get(choice_mark_str) + count
            self.resource[choice_type_str][choice_mark_str] = self.resource[choice_type_str].get(choice_mark_str) - count
            print('Оргтехника выдана в отдел. Проверка выдачи:')
            self.__str__()
            dept.print_resource()
        else:
            print('Аппаратов данного типа оргтехники нет на складе')


    def put_from_department_to_warehouse(self, dept: Department):
        print('Доступная оргтехника для сдачи на склад: ')
        equipment_type_tuple = tuple(enumerate(dept.department_equipment_type_dict.items(), 1))
        for key, value in equipment_type_tuple:
            print(f'{key}: {value[1]}')
        validate_ok = False
        choice_type = 0
        while not validate_ok:
            choice_type_input = input('Выберите нужный вариант цифрой: ')
            try:
                if ValidateTypeError.check_user_input(choice_type_input):
                    choice_type = abs(int(choice_type_input))
                    if choice_type  in range(1, len(dept.resource.keys()) + 1):
                        validate_ok = True
                        break
                    else:
                        print('Неверное значение! ', end='')
            except ValidateTypeError as error_obj:
                print(error_obj.txt)
                continue
        choice_type_str = equipment_type_tuple[choice_type-1][1][0]
        if dept.resource.get(choice_type_str) != {}:
            print('Доступные модели/наименования для выбранного типа оргтехники: ')
            equipment_mark_tuple = tuple(enumerate(dept.resource.get(choice_type_str).items(), 1))
            for key, value in equipment_mark_tuple:
                if value[1] > 0:
                    print(f'{key}: {value[0]}, остаток: {value[1]}')
            validate_ok = False
            choice_mark = 0
            while not validate_ok:
                choice_mark_input = input('Выберите нужный вариант цифрой: ')
                try:
                    if ValidateTypeError.check_user_input(choice_mark_input):
                        choice_mark = abs(int(choice_mark_input))
                        if choice_mark in range(1, len(dept.resource.get(choice_type_str).keys()) + 1):
                            validate_ok = True
                            break
                        else:
                            print('Неверное значение! ', end='')
                except ValidateTypeError as error_obj:
                    print(error_obj.txt)
                    continue
            choice_mark_str = equipment_mark_tuple[choice_mark - 1][1][0]
            validate_ok = False
            count = 0
            while not validate_ok:
                count_input = input('Укажите количество аппаратов для сдачи на склад (значение должно быть больше либо равно 1 и меньше либо равно фактическому количеству аппаратов): ')
                try:
                    if ValidateTypeError.check_user_input(count_input):
                        count = abs(int(count_input))
                        if count in range(1, equipment_mark_tuple[choice_mark - 1][1][1] + 1):
                            validate_ok = True
                            break
                        else:
                            print('Неверное значение! ', end='')
                except ValidateTypeError as error_obj:
                    print(error_obj.txt)
                    continue
            if self.resource[choice_type_str].get(choice_mark_str) is None:
                self.resource[choice_type_str][choice_mark_str] = count
            else:
                self.resource[choice_type_str][choice_mark_str] = self.resource[choice_type_str].get(choice_mark_str) + count
            dept.resource[choice_type_str][choice_mark_str] = dept.resource[choice_type_str].get(choice_mark_str) - count
            print('Оргтехнику сдали на склад. Проверка операции:')
            dept.print_resource()
            self.__str__()
        else:
            print('Аппаратов данного типа оргтехники нет на балансе отдела')


class Company:
    def __init__(self, company_name: str, company_address: str, departments_tuple: tuple, warehouse: OfficeEquipmentWarehouse):
        self.company = company_name
        self.address = company_address
        self.departments = departments_tuple
        self.warehouse = warehouse


class OfficeEquipment:
    type: str

    def __init__(self, mark: str):
        self.mark = mark
        self.state = 'off'

    def on(self):
        print('Включение аппарата.')
        self.state = 'on'
        return self.state

    def off(self):
        print('Выключение аппарата.')
        self.state = 'off'
        return self.state


class Printer(OfficeEquipment):
    type = 'printer'

    @staticmethod
    def print_doc(doc_path: str):
        print(f'Печать документа {doc_path}')
        if os.path.exists(doc_path) and os.path.isfile(doc_path):
            try:
                with open(doc_path, 'r') as document:
                    content = document.readlines()
                    printed_document = PaperDocument(os.path.basename(doc_path), content)
                    print(f'Печать завершена.')
                    return printed_document
            except IOError:
                print(
                    "Ошибка ввода-вывода при открытии файла или выполнении печати! Попробуйте переоткрыть файл и заново запустить печать")
        else:
            print('Печать не выполнена. Проверьте существование указанного файла.')
            return None


class Scanner(OfficeEquipment):
    type = 'scanner'

    @staticmethod
    def scan_doc(doc_for_scan: PaperDocument):
        print(f'Сканирование документа {doc_for_scan.name} [{doc_for_scan.content}]')
        scan_doc = DigitalDocument(f'Scan_{doc_for_scan.name}', doc_for_scan.content)
        print(f'Сканирование завершено. Получен документ {scan_doc.name} [{scan_doc.content}]')
        return scan_doc


class Copier(OfficeEquipment):
    type = 'copier'

    @staticmethod
    def copy_doc(doc_for_copy: PaperDocument):
        print(f'Копирование документа {doc_for_copy.name} [{doc_for_copy.content}]')
        copy_doc = PaperDocument(f'Copy_{doc_for_copy.name}', doc_for_copy.content)
        print(f'Копирование завершено. Получен документ {copy_doc.name} [{copy_doc.content}]')
        return copy_doc

office_counting_dep = CountingDep()
office_personnel_service_dep = PersonnelServiceDep()
office_warehouse_name = 'Офисный склад компании "Microsoft"'
office_warehouse_address = 'г. Москва, ул. Волгоградская, стр. 10'
office_warehouse = OfficeEquipmentWarehouse(office_warehouse_name, office_warehouse_address)
main_company = Company('Microsoft', 'г. Москва, Крылатский проспект, стр. 20/2', (office_counting_dep, office_personnel_service_dep), office_warehouse)

print(f'\nРабота со складом оргтехники: {office_warehouse_name} по адресу: {office_warehouse_address}')
print('Приём купленной оргтехники на склад:')
office_warehouse.acceptance_of_purchased_office_equipment_to_warehouse()
print('\nВыдача оргтехники со склада для Бухгалтерии: ')
office_warehouse.pass_from_warehouse_to_department(office_counting_dep)
print('\nВыдача оргтехники со склада для Кадровой службы: ')
office_warehouse.pass_from_warehouse_to_department(office_personnel_service_dep)
print('\nСдача оргтехники из отдела Бухгалтерии на склад: ')
office_warehouse.put_from_department_to_warehouse(office_counting_dep)

print('\nПлановое выборочное тестирование работы оргтехники на складе:')
my_paper_doc = PaperDocument('Доверенность', 'Текст доверенности')
first_scanner = Scanner('Toshiba')
print('\nПроверка работоспособности сканера:')
first_scanner.on()
scan_document = first_scanner.scan_doc(my_paper_doc)
first_scanner.off()
first_printer = Printer('HP')
print('\nПроверка работы принтера: ')
first_printer.on()
printing_doc = first_printer.print_doc('test_doc.txt')
first_printer.off()
first_copier = Copier('Samsung')
print('\nПроверка копировального аппарата: ')
first_copier.on()
copy_document = first_copier.copy_doc(my_paper_doc)
first_copier.off()
print('Работа с программой завершена.')