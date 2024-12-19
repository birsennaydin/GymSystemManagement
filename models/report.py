# models/report.py

class Report:
    def __init__(self):
        self.total_income = 0
        self.attendance_data = []
        self.popular_classes = {}
        self.trainer_performance = {}

    @property
    def total_income(self):
        return self._total_income

    @total_income.setter
    def total_income(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Income must be a number.")
        self._total_income = value

    @property
    def attendance_data(self):
        return self._attendance_data

    @attendance_data.setter
    def attendance_data(self, value):
        if not isinstance(value, list):
            raise ValueError("Attendance data must be a list.")
        self._attendance_data = value

    @property
    def popular_classes(self):
        return self._popular_classes

    @popular_classes.setter
    def popular_classes(self, value):
        if not isinstance(value, dict):
            raise ValueError("Popular classes must be a dictionary.")
        self._popular_classes = value

    @property
    def trainer_performance(self):
        return self._trainer_performance

    @trainer_performance.setter
    def trainer_performance(self, value):
        if not isinstance(value, dict):
            raise ValueError("Trainer performance must be a dictionary.")
        self._trainer_performance = value