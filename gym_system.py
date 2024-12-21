# gym_system.py
from controllers.auth_controller import AuthController
from controllers.member_controller import MemberController
from controllers.workout_zone_controller import WorkoutZoneController
from controllers.appointment_controller import AppointmentController
from controllers.payment_controller import PaymentController
from controllers.attendance_controller import AttendanceController
from controllers.staff_controller import StaffController
from views.display_menu import DisplayMenu  # Import DisplayMenu from views

class GymSystem:
    def __init__(self):
        self.running = True
        self.auth_controller = AuthController()
        self.member_controller = MemberController()
        self.workout_zone_controller = WorkoutZoneController()
        self.appointment_controller = AppointmentController()
        self.payment_controller = PaymentController()
        self.attendance_controller = AttendanceController()
        self.staff_controller = StaffController()

    def authenticate_user(self):
        """
        Prompts the user for login credentials and validates them.
        """
        try:
            user = self.auth_controller.login()  # Get the authenticated user
            return user
        except Exception as e:
            print(f"An error occurred during user authentication: {str(e)}")
            return None

    def run(self):
        try:
            user = self.authenticate_user()  # Authenticate user
            if user:
                self.display_menu(user)
        except Exception as e:
            print(f"An error occurred during the system run: {str(e)}")

    def display_menu(self, user):
        """
        Displays the menu based on the user's role.
        """
        try:
            self.auth_controller.display_menu_based_on_role(user)  # Show the role-based menu
        except Exception as e:
            print(f"An error occurred while displaying the menu: {str(e)}")
