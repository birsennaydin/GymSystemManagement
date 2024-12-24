# models/attendance.py
from models.enums import AttendanceStatusEnum


class Attendance:
    id_counter = 1
    records = []

    def __init__(self, member_id, class_id, attendance_date, status):
        self._id = Attendance.id_counter
        self._member_id = None
        self._class_id = None
        self._attendance_date = None
        self._status = None

        self.member_id = member_id
        self.class_id = class_id
        self.attendance_date = attendance_date
        self.status = status

        Attendance.id_counter += 1
        Attendance.records.append(self)

    @property
    def id(self):
        return self._id

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Member ID must be an integer.")
        self._member_id = value

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Class ID must be an integer.")
        self._class_id = value

    @property
    def attendance_date(self):
        return self._attendance_date

    @attendance_date.setter
    def attendance_date(self, value):
        if not value:
            raise ValueError("Attendance date cannot be empty.")
        self._attendance_date = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in [member.value for member in AttendanceStatusEnum]:
            raise ValueError(
                f"Invalid attendance status. Please choose from {', '.join([member.value for member in AttendanceStatusEnum])}.")
        self._status = value

    @classmethod
    def get_all(cls):
        return cls.records

    @classmethod
    def get_by_id(cls, id):
        return next((attendance for attendance in cls.records if attendance.id == id), None)
