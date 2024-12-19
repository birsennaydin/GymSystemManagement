# models/appointment.py

class Appointment:
    id_counter = 1
    appointments = []

    def __init__(self, member_id, trainer_id, date, appointment_type, status):
        self._id = Appointment.id_counter
        self._member_id = None
        self._trainer_id = None
        self._date = None
        self._type = None
        self._status = None

        self.member_id = member_id
        self.trainer_id = trainer_id
        self.date = date
        self.appointment_type = appointment_type
        self.status = status

        Appointment.id_counter += 1
        Appointment.appointments.append(self)

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
    def trainer_id(self):
        return self._trainer_id

    @trainer_id.setter
    def trainer_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Trainer ID must be an integer.")
        self._trainer_id = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not value:
            raise ValueError("Appointment date cannot be empty.")
        self._date = value

    @property
    def appointment_type(self):
        return self._type

    @appointment_type.setter
    def appointment_type(self, value):
        if value not in ['Personal Training', 'Group Class', 'Consultation']:
            raise ValueError("Appointment type must be 'Personal Training', 'Group Class', or 'Consultation'.")
        self._type = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ['Scheduled', 'Cancelled', 'Completed']:
            raise ValueError("Status must be one of 'Scheduled', 'Cancelled', 'Completed'.")
        self._status = value

    @classmethod
    def get_all(cls):
        return cls.appointments

    @classmethod
    def get_by_id(cls, id):
        return next((appointment for appointment in cls.appointments if appointment.id == id), None)