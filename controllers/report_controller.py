# controllers/report_controller.py
from views.report_view import ReportView
from models.report import Report

class ReportController:
    def __init__(self):
        self.report_list = []

    def show_report_menu(self, user):
        from controllers.auth_controller import AuthController

        while True:
            choice = ReportView.display_report_menu()

            if choice == "1":
                self.show_attendance_report()
            elif choice == "2":
                self.show_payment_report()
            elif choice == "3":
                self.show_member_growth_report()
            elif choice == "4":
                return AuthController.display_menu_based_on_role(user)
            else:
                ReportView.display_invalid_choice()

    def show_attendance_report(self):
        report = Report.generate_attendance_report()
        ReportView.display_attendance_report(report)

    def show_payment_report(self):
        # Ask the user for the start date
        start_date = input("Enter the start date for the payment report (YYYY-MM-DD): ").strip()

        # Generate the report with the start date
        try:
            report = Report.generate_payment_report(start_date)
            ReportView.display_payment_report(report)
        except ValueError as e:
            print(f"Error: {e}")
            # Handle the error (e.g., ask for the date again or display an error message)

    def show_member_growth_report(self):
        report = Report.generate_member_growth_report()
        ReportView.display_member_growth_report(report)
