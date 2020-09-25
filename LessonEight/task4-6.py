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


class OfficeEquipmentWarehouse:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.resource = {
            'printers': 0,
            'scanners': 0,
            'copiers': 0,
        }


class OfficeEquipment:
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
    @staticmethod
    def scan_doc(doc_for_scan: PaperDocument):
        print(f'Сканирование документа {doc_for_scan.name} [{doc_for_scan.content}]')
        scan_doc = DigitalDocument(f'Scan_{doc_for_scan.name}', doc_for_scan.content)
        print(f'Сканирование завершено. Получен документ {scan_doc.name} [{scan_doc.content}]')
        return scan_doc


class Copier(OfficeEquipment):
    @staticmethod
    def copy_doc(doc_for_copy: PaperDocument):
        print(f'Копирование документа {doc_for_copy.name} [{doc_for_copy.content}]')
        copy_doc = PaperDocument(f'Copy_{doc_for_copy.name}', doc_for_copy.content)
        print(f'Копирование завершено. Получен документ {copy_doc.name} [{copy_doc.content}]')
        return copy_doc

class Department:
    def __init__(self, name: str):
        self.name = name


class CountingDep(Department):
    def __init__(self):
        super().__init__('Бухгалтерия')


class PersonnelServiceDep(Department):
    def __init__(self):
        super().__init__('Кадровая служба')


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
office_warehouse = OfficeEquipmentWarehouse('Офисный склад на Волгоградской', 'г. Москва, ул. Волгоградская, стр. 10')
office_counting_dep = CountingDep()
office_personnel_service_dep = PersonnelServiceDep()