from controllers.member_controller import MemberController
from controllers.attendance_controller import AttendanceController
from controllers.payment_controller import PaymentController
from controllers.workout_zone_controller import WorkoutZoneController
from controllers.appointment_controller import AppointmentController
from controllers.staff_controller import StaffController
from controllers.report_controller import ReportController
from controllers.gym_location_controller import GymLocationController
from controllers.report_controller import ReportController
from views.display_menu import DisplayMenu


class GymSystem:
    def __init__(self):
        self.running = True
        self.gym_location_controller = GymLocationController()
        self.member_controller = MemberController()
        self.workout_zone_controller = WorkoutZoneController()
        self.report_controller = ReportController()

    def run(self):
        while self.running:
            result = DisplayMenu.display_menu()
            self.handle_choice(result)

    def handle_choice(self, choice):
        if choice == "1":
            self.member_controller.manage_member()
        elif choice == "2":
            self.workout_zone_controller.manage_zones()
        elif choice == "3":
            AppointmentController.manage_appointments()
        elif choice == "4":
            PaymentController.process_payments()
        elif choice == "5":
            AttendanceController.check_in()
        elif choice == "6":
            StaffController.manage_staff()
        elif choice == "7":
            ReportController.generate_reports()
        elif choice == "8":
            self.gym_location_controller.manage_locations()
        elif choice == "9":
            print("Exiting the system. Goodbye!")
            self.running = False
        else:
            print("Invalid choice. Please try again.")
