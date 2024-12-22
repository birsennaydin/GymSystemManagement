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
        self._gym_location_id = None  # Gym Location ID to be associated

        self.membership_id = membership_id
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_type = membership_type
        self.health_info = health_info
        self.status = status
        self.gym_location_id = gym_location_id  # Gym Location ID here

        Member.id_counter += 1
        Member.members.append(self)

    @property
    def id(self):
        return self._id

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

    @classmethod
    def get_by_email(cls, email):
        """
        Returns a member by their email address.
        """
        # Searching for the member by email in the class members list
        return next((member for member in cls.members if member.email == email), None)
