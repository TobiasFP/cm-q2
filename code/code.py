

class employee:
    def __init__(self, email: str, holidays_left: int) -> None:
        self.email: str = email
        self.holidays_left: list[str] = holidays_left


def get_emails_of_users_withouth_holiday_left(employees: list[employee]) -> list[str]:
    return [employee.email for employee in employees if len(employee.holidays_left) == 0]
