# controllers/attendance_controller.py
from models.attendance import Attendance
from views.attendance_view import AttendanceView

class AttendanceController:
    @staticmethod
    def check_in(user):
        from controllers.auth_controller import AuthController
        while True:
            choice = AttendanceView.display_attendance_menu()

            if choice == "1":
                AttendanceController.add_attendance()
            elif choice == "2":
                AttendanceController.list_attendance()
            elif choice == "3":
                AttendanceView.display_return_to_main_menu()
                return AuthController.display_menu_based_on_role(user)
            else:
                AttendanceView.display_invalid_choice()

    @staticmethod
    def add_attendance():
        member_id = AttendanceView.get_member_id()
        class_id = AttendanceView.get_class_id()
        status = AttendanceView.get_status()

        attendance = Attendance(member_id=member_id, class_id=class_id, attendance_date="2024-12-20", status=status)
        AttendanceView.display_attendance_success(attendance)

    @staticmethod
    def list_attendance():
        attendance_records = Attendance.get_all()
        if not attendance_records:
            AttendanceView.display_no_attendance_found()
        else:
            for record in attendance_records:
                AttendanceView.display_attendance_record(record)
