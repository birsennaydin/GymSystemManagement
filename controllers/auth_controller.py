# controllers/auth_controller.py
from controllers.appointment_controller import AppointmentController
from controllers.attendance_controller import AttendanceController
from controllers.gym_location_controller import GymLocationController
from controllers.member_controller import MemberController
from controllers.payment_controller import PaymentController
from controllers.report_controller import ReportController
from controllers.staff_controller import StaffController
from controllers.user_controller import UserController
from controllers.workout_zone_controller import WorkoutZoneController
from models.enums import UserRole
from models.user import User  # Import User model
from views.display_menu import DisplayMenu  # Import DisplayMenu for displaying menus
from views.member_view import MemberView
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
            print(f"PASSWORD: {user.password}, {password}, {email}, {user}")
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
                choice =  DisplayMenu.display_admin_menu()  # Manager sees the full menu
                print(f"Display menu: {choice}")
                AuthController.handle_admin_menu_choice(choice, user)
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

    @staticmethod
    def handle_admin_menu_choice(choice, user):
        """
        Handles the choices for the Admin/Manager menu.
        Redirects to the appropriate functionality based on user choice.
        """
        try:
            if choice == "1":  # Member Management
                MemberController.manage_member(user)
            elif choice == "2":  # Workout Zones
                WorkoutZoneController.manage_zones(user)
            elif choice == "3":  # Appointments
                AppointmentController.manage_appointments(user)
            elif choice == "4":  # Payments and Subscriptions
                PaymentController.process_payments(user)
            elif choice == "5":  # Attendance Tracking
                AttendanceController.check_in(user)
            elif choice == "6":  # Staff Management
                StaffController.manage_staff(user)
            elif choice == "7":  # Reports
                ReportController.generate_reports(user)
            elif choice == "8":  # Manage Gym Locations
                GymLocationController.manage_locations(user)
            elif choice == "9":  # Manage User Management
                print(f"UserController: {choice}")
                UserController.manage_users(user)
            elif choice == "10":  # Logout
                print("Logging out...")
                return False  # End the session and logout
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred while handling the menu choice: {str(e)}")
        return True  # Continue running the menu after valid choices