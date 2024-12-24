# controllers/attendance_controller.py
from models.attendance import Attendance
from models.class_schedule import ClassSchedule
from models.member import Member
from views.attendance_view import AttendanceView

class AttendanceController:
    @staticmethod
    def check_in(user):
        from controllers.auth_controller import AuthController
        while True:
            try:
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

            except Exception as e:
                print(f"Error occurred in check-in process: {e}")
                AttendanceView.display_invalid_choice()

    @staticmethod
    def add_attendance():
        try:
            members = Member.get_all()
            # Check if members list is empty
            if not members:
                print("Error: No members found. Unable to add attendance.")
                return

            classes = ClassSchedule.get_all()
            if not classes:
                print("Error: No classes found. Unable to add attendance.")
                return

            member_id = AttendanceView.get_member_id(members)
            class_id = AttendanceView.get_class_id(classes)
            status = AttendanceView.get_status()
            attendance_date = AttendanceView.get_attendance_date()

            attendance = Attendance(member_id=member_id, class_id=class_id, attendance_date=attendance_date, status=status)
            AttendanceView.display_attendance_success(attendance)

        except Exception as e:
            print(f"Error occurred while adding attendance: {e}")

    @staticmethod
    def list_attendance():
        try:
            attendance_records = Attendance.get_all()
            if not attendance_records:
                AttendanceView.display_no_attendance_found()
            else:
                for record in attendance_records:
                    try:
                        # Fetch the Member and Class details based on their IDs
                        member = Member.get_by_id(record.member_id)
                        class_detail = ClassSchedule.get_by_id(record.class_id)
                        AttendanceView.display_attendance_record(record, member.name, class_detail.class_name)
                    except Exception as e:
                        print(f"Error occurred while fetching details for record {record.id}: {e}")
                        continue

        except Exception as e:
            print(f"Error occurred while listing attendance: {e}")
