# models/report.py
from datetime import datetime

from models.attendance import Attendance
from models.payment import Payment
from models.member import Member
from models.staff import Staff

class Report:
    @staticmethod
    def generate_attendance_report():
        """
        Generates a report on member attendance.
        """
        attendance_data = Attendance.get_all()  # Get all attendance records
        report = {}
        for record in attendance_data:
            member = Member.get_by_id(record.member_id)
            report[member.email] = report.get(member.email, 0) + 1  # Track number of attendances per member
        return report

    @staticmethod
    def generate_payment_report(start_date=None):
        """
        Generates a report on payments and revenue starting from the specified date.
        """
        payment_data = Payment.get_all()
        report = {"total_revenue": 0, "payment_methods": {}}

        # Convert start_date string to datetime object if provided
        if start_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")  # Ensure it's in the correct format
            except ValueError:
                raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

        for payment in payment_data:
            # Filter payments based on start_date if provided
            payment_date = datetime.strptime(payment.payment_date, "%Y-%m-%d %H:%M:%S")
            if not start_date or payment_date >= start_date:
                report["total_revenue"] += payment.amount
                report["payment_methods"][payment.payment_method] = report["payment_methods"].get(
                    payment.payment_method, 0) + payment.amount

        return report

    @staticmethod
    def generate_member_growth_report():
        """
        Generates a report on member growth over time.
        """
        members = Member.get_all()
        report = {"new_members": len(members)}  # Just a simple count for now
        return report
