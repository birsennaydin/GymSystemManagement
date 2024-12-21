# controllers/auth_controller.py
from models.enums import UserRole
from models.user import User  # Import User model
from views.display_menu import DisplayMenu  # Import DisplayMenu for displaying menus

class AuthController:
    @staticmethod
    def login():
        """
        Prompts the user for login credentials (email and password).
        If credentials are valid, returns the corresponding user object and role.
        """
        try:
            print("Welcome to St. Mary's Fitness System!")
            print("Please log in to continue.")

            # Get email and password from user input
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            # Check if a user with the given email and password exists
            user = AuthController.authenticate_user(email, password)

            if user:
                print(f"Login successful! Welcome {user.email}. Role: {user.role}")
                # Return the authenticated user with their role
                return user
            else:
                print("Invalid credentials. Please try again.")
                return None  # Return None if authentication fails
        except Exception as e:
            print(f"An error occurred during login: {str(e)}")
            return None  # Return None if an exception occurs during login

    @staticmethod
    def authenticate_user(email, password):
        """
        Checks if a user with the provided email and password exists.
        Returns the user if authenticated, otherwise returns None.
        """
        try:
            # Find user by email
            user = User.get_by_email(email)

            if user and user.password == password:  # Validate password
                return user
            return None  # Return None if no user found or password is incorrect
        except Exception as e:
            print(f"An error occurred while authenticating the user: {str(e)}")
            return None  # Return None if an exception occurs during user authentication

    @staticmethod
    def display_menu_based_on_role(user):
        """
        Displays the appropriate menu based on the user's role.
        """
        try:
            if user.role == UserRole.MANAGER:  # Check role as UserRole enum
                return DisplayMenu.display_admin_menu()  # Manager sees the full menu
            elif user.role == UserRole.TRAINER:
                return DisplayMenu.display_trainer_menu()  # Trainer has access to specific menus
            elif user.role == UserRole.ATTENDANT:
                return DisplayMenu.display_attendant_menu()  # Attendant can only access limited menus
            elif user.role == UserRole.MEMBER:
                return DisplayMenu.display_member_menu()  # Member can only access their profile and related menus
            else:
                print("Invalid role.")
                return None
        except Exception as e:
            print(f"An error occurred while displaying the menu: {str(e)}")
            return None
