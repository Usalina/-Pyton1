#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Warehouse:
    pass


class Equipment:
    def __init__(self, model, quantity):
        self.model = model
        self.quantity = quantity


class Printer(Equipment):
    def __init__(self, print_speed):
        self.print_speed = print_speed


class Scanner(Equipment):
    def __init__(self, scan_speed):
        self.scan_speed = scan_speed


class Xerox(Equipment):
    def __init__(self, xerox_speed):
        self.xerox_speed = xerox_speed


