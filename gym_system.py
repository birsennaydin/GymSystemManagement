from Controllers.member_controller import MemberController
from Controllers.attendance_controller import AttendanceController
from Controllers.payment_controller import PaymentController
from Controllers.workout_zone_controller import WorkoutZoneController
from Controllers.appointment_controller import AppointmentController
from Controllers.staff_controller import StaffController
from Controllers.report_controller import ReportController
from Controllers.gym_location_controller import GymLocationController
from views.display_menu import DisplayMenu


class GymSystem:
    def __init__(self):
        self.running = True
        self.gym_location_controller = GymLocationController()
        self.member_controller = MemberController()
        self.workout_zone_controller = WorkoutZoneController()

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
