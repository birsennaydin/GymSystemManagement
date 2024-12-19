# models/staff.py
from models.enums import StaffRole


class Staff:
    id_counter = 1
    staff_members = []

    def __init__(self, name, role, email, phone, gym_location_id=None):
        self._id = Staff.id_counter
        self._name = None
        self._role = None
        self._email = None
        self._phone = None
        self._gym_location_id = None

        self.name = name
        self.role = role
        self.email = email
        self.phone = phone
        self.gym_location_id = gym_location_id

        Staff.id_counter += 1
        Staff.staff_members.append(self)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Staff name cannot be empty.")
        self._name = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if value not in StaffRole.__members__:
            raise ValueError(f"Invalid role. Please choose from {', '.join(StaffRole.__members__.keys())}.")
        self._role = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty.")
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value:
            raise ValueError("Phone number cannot be empty.")
        self._phone = value

    @property
    def gym_location_id(self):
        return self._gym_location_id

    @gym_location_id.setter
    def gym_location_id(self, value):
        if value and not isinstance(value, int):
            raise ValueError("Gym Location ID must be an integer.")
        self._gym_location_id = value

    @classmethod
    def get_all(cls):
        return cls.staff_members

    @classmethod
    def get_by_id(cls, id):
        return next((staff for staff in cls.staff_members if staff.id == id), None)