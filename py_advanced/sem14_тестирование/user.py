import random
import json
import os
from faker import Faker


def create_employee(company: str, count: int):
    employees = {}
    list_id = []
    for _ in range(count):
        name = Faker('ru_RU').name()
        while True:
            employee_id = str(random.randint(1, 999999)).zfill(6)
            if employee_id not in list_id:
                list_id.append(employee_id)
                break
        lvl_access = int(employee_id) % 7 + 1
        if lvl_access in employees:
            employees[lvl_access][employee_id] = name
        else:
            employees[lvl_access] = {employee_id: name}
    with open(f'{company}.json', 'w', encoding='UTF-8') as file:
        json.dump(employees, file, indent=4, ensure_ascii=False)
    return employees


class EmployeeName:
    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value):
        if not all([all(list(map(lambda x: x.isalpha(), name))) for name in value.split()]):
            raise ValueError(f'Имя может состоять только из букв: {value}')
        if not all(map(lambda x: x.istitle(), value.split())):
            raise ValueError(f'Имя должно быть написано с заглавной буквы: {value}')
        setattr(instance, self.parameter_name, value)


class EmployeeId:
    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value):
        if not len(value) == 6:
            raise ValueError(f'ID  должен состоять из 6 цифр: {value}')
        if not value.isdigit():
            raise ValueError(f'ID может состоять только из цифр: {value}')
        setattr(instance, self.parameter_name, value)


class Employee:
    name = EmployeeName()
    employee_id = EmployeeId()

    def __init__(self, name: str, employee_id: str, lvl_access: int):
        self.name = name
        self.employee_id = employee_id
        if 0 < lvl_access < 8:
            self.lvl_access = lvl_access
        else:
            raise ValueError(f'Уровень доступа должен быть от 1 до 7: {lvl_access}')

    def __str__(self):
        return f'{self.name} ({self.employee_id}) | Доступ: {self.lvl_access}'

    def __repr__(self):
        return f'{self.name} ({self.employee_id}) | Доступ: {self.lvl_access}'

    def __eq__(self, other):
        return self.name == other.name and self.employee_id == other.employee_id


class UsersException(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class LevelError(UsersException):
    def __init__(self, hr: Employee, new: Employee):
        super(LevelError, self).__init__(f'Пользователь {hr.name} {hr.lvl_access}-го уровня '
                                         f'не может создать пользователя {new.lvl_access}-го уровня')


class AccessError(UsersException):
    def __init__(self, empl: Employee):
        super(AccessError, self).__init__(f'Пользователь {empl.name} ID {empl.employee_id} в базе не найден.'
                                         f'Проверье правильность ввода имени и ID')


class DoubleUserError(UsersException):
    def __init__(self, empl: Employee):
        super(DoubleUserError, self).__init__(f'Пользователь {empl.name} ID {empl.employee_id} в базе уже существует')


class Company:
    def __init__(self, name):
        self.name = name
        if os.path.exists(f'{self.name}.json'):
            with open(f'{self.name}.json', 'r', encoding='UTF-8') as file:
                employees_list = json.load(file)
        else:
            employees_list = create_employee(self.name, 10)
        self.employees = [Employee(e_name, e_id, int(e_lvl))
                          for e_lvl, person in employees_list.items()
                          for e_id, e_name in person.items()]

    def login(self, name: str, e_id: str):
        for employee in self.employees:
            if employee.name == name and employee.employee_id == e_id:
                return employee
        raise AccessError(Employee(name, e_id, 1))

    def hiring(self, hr: Employee, new_name: str, new_id: str, new_lvl: int):
        if hr:
            if hr.lvl_access > new_lvl:
                if new_id not in [employee.employee_id for employee in self.employees]:
                    self.employees.append(Employee(new_name, new_id, new_lvl))
                    self.__save()
                else:
                    raise DoubleUserError(Employee(new_name, new_id, new_lvl))
            else:
                raise LevelError(hr, Employee(new_name, new_id, new_lvl))
        else:
            raise AccessError(hr)

    def __save(self):
        employees_list = {}
        for employee in self.employees:
            if employee.lvl_access in employees_list:
                employees_list[employee.lvl_access][employee.employee_id] = employee.name
            else:
                employees_list[employee.lvl_access] = {employee.employee_id: employee.name}
        with open(f'{self.name}.json', 'w', encoding='UTF-8') as file:
            json.dump(employees_list, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    nike = Company('NIKE')
    print(*nike.employees, sep='\n', end='\n')
    me = nike.login('Святополк Венедиктович Меркушев', '219755')
    print(me)
    nike.hiring(me, 'Ольга Игоревна Борисова', '140000', 4)

