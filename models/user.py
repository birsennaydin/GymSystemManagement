# models/user.py
from models.enums import UserRole  # Import UserRole enum


class User:
    id_counter = 1
    users = []  # This will hold all users, including the default user

    def __init__(self, email, password, role, associated_id):
        try:
            # Ensure role is valid and convert it to the enum if it's a string
            if isinstance(role, str):
                role = UserRole[role.upper()]  # Convert string role to enum

            # Check if the email already exists
            if User.get_by_email(email):
                raise ValueError(f"Email address '{email}' is already taken.")

            self._id = User.id_counter
            self._email = None
            self._password = None
            self._role = None
            self._associated_id = None  # ID of the associated Staff or Member

            self.email = email
            self.password = password
            self.role = role  # Manager, Trainer, Attendant, Member
            self.associated_id = associated_id  # Staff ID or Member ID

            User.id_counter += 1
            User.users.append(self)  # Add the new user to the users list

        except ValueError as e:
            print(f"Error during user initialization: {str(e)}")
            raise

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty.")
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not value:
            raise ValueError("Password cannot be empty.")
        self._password = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if value not in UserRole.__members__:
            raise ValueError(f"Invalid role. Please choose from {', '.join(UserRole.__members__.keys())}.")
        self._role = value

    @property
    def associated_id(self):
        return self._associated_id

    @associated_id.setter
    def associated_id(self, value):
        self._associated_id = value

    @classmethod
    def get_by_email(cls, email):
        """
        Returns a user by email address.
        """
        try:
            return next((user for user in cls.users if user.email == email), None)
        except Exception as e:
            print(f"Error occurred while fetching user by email: {str(e)}")
            return None

    @classmethod
    def get_by_id(cls, id):
        """
        Returns a user by their ID.
        """
        try:
            return next((user for user in cls.users if user.id == id), None)
        except Exception as e:
            print(f"Error occurred while fetching user by ID: {str(e)}")
            return None

    @classmethod
    def create_default_user(cls):
        """
        Creates a default Manager user when the application first runs.
        Adds the default user to the users list.
        """
        try:
            # Check if users already exist to prevent duplicate creation
            if not cls.users:
                default_user = User(
                    email="admin@stmarys.com",  # Admin's default email
                    password="admin123",  # Admin's default password
                    role="MANAGER",  # Admin role as Manager
                    associated_id=None  # No associated ID for Admin
                )
                # Add the default user to the users list
                cls.users.append(default_user)
                print(f"Default user created: {default_user.email}")
            else:
                print("Default user already exists.")
        except Exception as e:
            print(f"Error occurred while creating default user: {str(e)}")
