# Controller/report_controller.py
from models.report import Report
from models.payment import Payment
from models.attedance import Attendance
from models.workout_zone import WorkoutZone

class ReportController:
    def __init__(self):
        self.report = Report()

    def generate_monthly_income_report(self):
        """
        Monthly income report based on payments made by members.
        """
        total_income = 0
        for payment in Payment.payments:
            total_income += payment.amount
        self.report.total_income = total_income
        return self.report.total_income

    def generate_member_attendance_report(self):
        """
        Generate a report on member attendance, listing attendance status for each member.
        """
        attendance_report = []
        for attendance in Attendance.records:
            attendance_report.append(f"Member {attendance.member_id}: {attendance.status}")
        self.report.attendance_data = attendance_report
        return self.report.attendance_data

    def generate_popular_class_report(self):
        """
        Generate a report on the most popular workout classes based on attendance.
        """
        class_attendance = {}
        for attendance in Attendance.records:
            class_id = attendance.class_id
            if class_id not in class_attendance:
                class_attendance[class_id] = 0
            class_attendance[class_id] += 1

        self.report.popular_classes = class_attendance
        return self.report.popular_classes

    def generate_trainer_performance_report(self):
        """
        Generate a report on trainer performance, showing the number of sessions completed by each trainer.
        """
        trainer_sessions = {}
        for attendance in Attendance.records:
            trainer_id = attendance.member_id  # assuming trainer_id is stored in member_id for this example
            if trainer_id not in trainer_sessions:
                trainer_sessions[trainer_id] = 0
            trainer_sessions[trainer_id] += 1

        self.report.trainer_performance = trainer_sessions
        return self.report.trainer_performance