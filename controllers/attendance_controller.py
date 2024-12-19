from models.attedance import Attendance

class AttendanceController:
    attendance_records = []

    @staticmethod
    def check_in():
        member_id = input("Enter member ID: ").strip()
        date = input("Enter date (YYYY-MM-DD): ").strip()
        zone = input("Enter workout zone: ").strip()
        check_in_time = input("Enter check-in time (HH:MM): ").strip()

        new_record = Attendance(member_id, date, zone, check_in_time)
        AttendanceController.attendance_records.append(new_record)
        print(f"Member {member_id} checked in successfully!")

    @staticmethod
    def list_attendance():
        if not AttendanceController.attendance_records:
            print("No attendance records found.")
            return
        print("\nAttendance Records:")
        for record in AttendanceController.attendance_records:
            print(record)