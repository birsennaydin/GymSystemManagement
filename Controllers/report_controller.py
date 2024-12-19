# controllers/report_controller.py
from Models.report import Report
from Models.member import Member
from Models.payment import Payment

class ReportController:
    def __init__(self):
        self.reports = []

    def generate_membership_growth_report(self):
        print("Generate Membership Growth Report")
        report_type = input("Enter report type (e.g., Monthly, Yearly): ")
        content = "Membership growth data would go here."
        report_id = len(self.reports) + 1
        new_report = Report(report_id, report_type, content)
        self.reports.append(new_report)
        print(f"Report {report_id} generated successfully!")

    def generate_revenue_report(self):
        print("Generate Revenue Report")
        total_revenue = sum(payment.amount for payment in Payment.payments)
        report_type = "Revenue"
        content = f"Total Revenue: {total_revenue}"
        report_id = len(self.reports) + 1
        new_report = Report(report_id, report_type, content)
        self.reports.append(new_report)
        print(f"Revenue Report generated successfully!")

    def generate_attendance_report(self):
        print("Generate Attendance Report")
        report_type = "Attendance"
        content = "Attendance report data goes here."  # Example content
        report_id = len(self.reports) + 1  # Generate a new report ID
        new_report = Report(report_id, report_type, content)
        self.reports.append(new_report)
        print(f"Attendance Report generated successfully!")
