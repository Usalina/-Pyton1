#5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.

class Warehouse:
    def input(self):
        print()



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

