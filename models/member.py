# models/member.py
from models.enums import MembershipType

class Member:
    id_counter = 1
    members = []

    def __init__(self, name, email, phone, membership_type, health_info, status, gym_location_id, user_id):
        self._id = Member.id_counter
        self._name = None
        self._email = None
        self._phone = None
        self._membership_type = None
        self._health_info = None
        self._status = None
        self._gym_location_id = None  # Gym Location ID to be associated
        self._user_id = None

        self.name = name
        self.email = email
        self.phone = phone
        self.membership_type = membership_type
        self.health_info = health_info
        self.status = status
        self.gym_location_id = gym_location_id  # Gym Location ID here
        self.user_id = user_id

        Member.id_counter += 1
        Member.members.append(self)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, int):
            raise ValueError("User ID must be an integer.")
        self._user_id = value

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

    @classmethod
    def get_by_user_id(cls, user_id):
        """
        Returns a member by their  user id.
        """
        # Searching for the member by user_id in the class members list
        return next((member for member in cls.members if member.user_id == user_id), None)

    @email.setter
    def email(self, value):
        self._email = value

    @name.setter
    def name(self, value):
        self._name = value

    @phone.setter
    def phone(self, value):
        self._phone = value

    @classmethod
    def create_default_member(cls):
        """
        Creates default members when the application first runs.
        Adds the default members to the member list automatically.
        """
        try:
            # Check if users already exist to prevent duplicate creation
            if not cls.members:
                # Create the default members
                Member(
                    name="Manager",
                    email="admin@stmarys.com",
                    phone="0709898595",
                    membership_type="Regular",
                    health_info="normal",
                    status="Active",  # Default to Active status
                    gym_location_id=1,  # Set gym location ID
                    user_id=1
                )

                Member(
                    name="Member",
                    email="member@stmarys.com",
                    phone="0709898595",
                    membership_type="Regular",
                    health_info="normal",
                    status="Active",  # Default to Active status
                    gym_location_id=1,  # Set gym location ID
                    user_id=2
                )

                print("Default members created.")
            else:
                print("Default members already exist.")
        except Exception as e:
            print(f"Error occurred while creating default member: {str(e)}")