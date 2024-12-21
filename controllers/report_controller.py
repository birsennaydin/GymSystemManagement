# controllers/report_controller.py
from models.report import Report
from views.report_view import ReportView

class ReportController:
    @staticmethod
    def generate_reports():
        while True:
            choice = ReportView.display_report_menu()

            if choice == "1":
                ReportController.generate_monthly_income_report()
            elif choice == "2":
                ReportController.generate_member_attendance_report()
            elif choice == "3":
                ReportController.generate_popular_class_report()
            elif choice == "4":
                ReportController.generate_trainer_performance_report()
            elif choice == "5":
                ReportView.display_return_to_main_menu()
                break
            else:
                ReportView.display_invalid_choice()

    @staticmethod
    def generate_monthly_income_report():
        income = Report.generate_monthly_income_report()
        ReportView.display_monthly_income_report(income)

    @staticmethod
    def generate_member_attendance_report():
        attendance = Report.generate_member_attendance_report()
        ReportView.display_member_attendance_report(attendance)

    @staticmethod
    def generate_popular_class_report():
        popular_classes = Report.generate_popular_class_report()
        ReportView.display_popular_class_report(popular_classes)

    @staticmethod
    def generate_trainer_performance_report():
        trainer_performance = Report.generate_trainer_performance_report()
        ReportView.display_trainer_performance_report(trainer_performance)
