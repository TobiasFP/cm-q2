import pytest

from code import code


def test_get_emails_of_users_withouth_holiday_left():
    employees: list[code.employee] = [
        code.employee('hi@hi.dk', ["2021 11/26"]),
        code.employee('mi@hi.dk', ["2021 11/24", "2021 11/25", "2021 11/26"]),
        code.employee('ni@hi.dk', []),
        code.employee('ii@hi.dk', []),
        code.employee('ki@hi.dk', []),
        code.employee('li@hi.dk', []),
        code.employee('li@hi.dk', [])
    ]
    assert code.get_emails_of_users_withouth_holiday_left(employees) == [
        'ni@hi.dk',
        'ii@hi.dk',
        'ki@hi.dk',
        'li@hi.dk',
        'li@hi.dk'
    ]
