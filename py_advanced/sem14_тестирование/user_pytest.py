import json
import pytest
from user import Company, AccessError, DoubleUserError, Employee


@pytest.fixture
def data():
    return Company('NIKE')


@pytest.fixture
def user():
    return Employee('Егор Тихонович Соколов', '492728', 6)


def test_login(data, user):
    assert data.login('Егор Тихонович Соколов', '492728') == user


def test_hiring(data, user):
    new_test = Employee('Тестов Тест Тестович', '000000', 1)
    data.hiring(user, new_test.name, new_test.employee_id, new_test.lvl_access)
    with open(f'{data.name}.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    assert file[str(new_test.lvl_access)].get(str(new_test.employee_id)) == new_test.name
    file[str(new_test.lvl_access)].pop(str(new_test.employee_id))
    with open(f'{data.name}.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, indent=4, ensure_ascii=False)


def test_name_error(data, user):
    with pytest.raises(ValueError, match=r'Имя должно быть написано с заглавной буквы: мария петровна петрова'):
        data.hiring(user, 'мария петровна петрова', '400000', 5)


def test_access_error(data):
    with pytest.raises(AccessError):
        data.login('Егор Тихонович Соколов', '492028')


def test_double_employee(data, user):
    with pytest.raises(DoubleUserError):
        data.hiring(user, 'Егор Тихонович Соколов', '492728', 5)


def test_id_error(data,user):
    with pytest.raises(ValueError, match=r'ID  должен состоять из 6 цифр: 400'):
        data.hiring(user, 'Мария Петровна Петрова', '400', 5)

if __name__ == '__main__':
    pytest.main()

