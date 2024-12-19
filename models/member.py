# models/member.py
from models.enums import MembershipType


class Member:
    id_counter = 1
    members = []

    def __init__(self, membership_id, name, email, phone, membership_type, health_info, status, gym_location_id):
        self._id = Member.id_counter
        self._membership_id = None
        self._name = None
        self._email = None
        self._phone = None
        self._membership_type = None
        self._health_info = None
        self._status = None
        self._gym_location_id = None

        self.membership_id = membership_id
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_type = membership_type
        self.health_info = health_info
        self.status = status
        self.gym_location_id = gym_location_id

        Member.id_counter += 1
        Member.members.append(self)

    @property
    def id(self):
        return self._id

    @property
    def membership_id(self):
        return self._membership_id

    @membership_id.setter
    def membership_id(self, value):
        if not value:
            raise ValueError("Membership ID cannot be empty.")
        self._membership_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Member name cannot be empty.")
        self._name = value

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
    def membership_type(self):
        return self._membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in MembershipType.__members__:
            raise ValueError(
                f"Invalid membership type. Please choose from {', '.join(MembershipType.__members__.keys())}.")
        self._membership_type = value

    @property
    def health_info(self):
        return self._health_info

    @health_info.setter
    def health_info(self, value):
        if not value:
            raise ValueError("Health information cannot be empty.")
        self._health_info = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ['Active', 'Suspended']:
            raise ValueError("Status must be one of 'Active', 'Suspended'.")
        self._status = value

    @property
    def gym_location_id(self):
        return self._gym_location_id

    @gym_location_id.setter
    def gym_location_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Gym Location ID must be an integer.")
        self._gym_location_id = value

    @classmethod
    def get_all(cls):
        return cls.members

    @classmethod
    def get_by_id(cls, id):
        return next((member for member in cls.members if member.id == id), None)