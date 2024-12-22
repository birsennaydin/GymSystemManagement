# models/user.py
from models.enums import UserRole  # Import UserRole enum


class User:
    id_counter = 1
    users = []  # This will hold all users, including the default user

    def __init__(self, email, password, role):
        try:
            # If role is a string, convert it to the corresponding enum
            if isinstance(role, UserRole):
                try:
                    print(f"Save Role INITIALIZE000: {role}, {role.value}")
                    role = role.value
                except KeyError:
                    raise ValueError(
                        f"Invalid role '{role}'. Please choose from {', '.join(UserRole.__members__.keys())}.")

            # Check if the email already exists
            if User.get_by_email(email):
                raise ValueError(f"Email address '{email}' is already taken.")

            self._id = User.id_counter
            self._email = None
            self._password = None
            self._role = None

            self.email = email
            self.password = password
            print(f"Save PASSword INITIALIZE: {self.password}, {self.email}")
            self.role = role  # Manager, Trainer, Attendant, Member

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
        print(f"Password 000: {value}")
        self._password = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        # If the value is an enum instance (UserRole), assign it directly
        print(f"SETTER ROLE: {value}")
        if isinstance(value, UserRole):
            self._role = value
        elif isinstance(value, str):  # If it's a string, convert it to the enum
            try:
                self._role = UserRole[value.upper()]  # Convert string to the correct UserRole enum
            except KeyError:
                raise ValueError(
                    f"Invalid role '{value}'. Please choose from {', '.join(UserRole.__members__.keys())}.")
        else:
            raise ValueError(f"Invalid role '{value}'. Please choose from {', '.join(UserRole.__members__.keys())}.")

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
        Creates default users when the application first runs.
        Adds the default users to the users list automatically.
        """
        try:
            # Check if users already exist to prevent duplicate creation
            if not cls.users:
                # Create the default users
                User(
                    email="admin@stmarys.com",  # Admin's default email
                    password="admin123",  # Admin's default password
                    role="MANAGER"  # Admin role as Manager (string, will be converted to UserRole.MANAGER)
                )

                User(
                    email="trainer@stmarys.com",
                    password="trainer123",
                    role="TRAINER"
                )

                User(
                    email="attendant@stmarys.com",
                    password="attendant123",
                    role="ATTENDANT"
                )

                User(
                    email="member@stmarys.com",
                    password="member123",
                    role="MEMBER"
                )

                print("Default users created.")
            else:
                print("Default users already exist.")
        except Exception as e:
            print(f"Error occurred while creating default user: {str(e)}")

    @classmethod
    def get_all(cls):
        """
        Returns all users.
        """
        return cls.users