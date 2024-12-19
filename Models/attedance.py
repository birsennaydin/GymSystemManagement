from datetime import datetime

class Attendance:
    def __init__(self, attendance_id, member_id, class_type, attendance_date: datetime):
        self.attendance_id = attendance_id
        self.member_id = member_id
        self.class_type = class_type
        self.attendance_date = attendance_date

    # Getters and Setters
    def get_attendance_id(self):
        return self.attendance_id

    def set_attendance_id(self, attendance_id):
        self.attendance_id = attendance_id

    def get_member_id(self):
        return self.member_id

    def set_member_id(self, member_id):
        self.member_id = member_id

    def get_class_type(self):
        return self.class_type

    def set_class_type(self, class_type):
        self.class_type = class_type

    def get_attendance_date(self):
        return self.attendance_date

    def set_attendance_date(self, attendance_date: datetime):
        self.attendance_date = attendance_date
