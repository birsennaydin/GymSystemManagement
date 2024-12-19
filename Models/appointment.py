# models/appointment.py
from datetime import datetime

class Appointment:
    def __init__(self, appointment_id, member_id, appointment_type, appointment_date):
        self.appointment_id = appointment_id
        self.member_id = member_id
        self.appointment_type = appointment_type
        self.appointment_date = appointment_date

    # Getters and Setters
    def get_appointment_id(self):
        return self.appointment_id

    def set_appointment_id(self, appointment_id):
        self.appointment_id = appointment_id

    def get_member_id(self):
        return self.member_id

    def set_member_id(self, member_id):
        self.member_id = member_id

    def get_appointment_type(self):
        return self.appointment_type

    def set_appointment_type(self, appointment_type):
        self.appointment_type = appointment_type

    def get_appointment_date(self):
        return self.appointment_date

    def set_appointment_date(self, appointment_date: datetime):
        self.appointment_date = appointment_date
