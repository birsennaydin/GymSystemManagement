# views/attendance_view.py
class AttendanceView:
    @staticmethod
    def display_attendance_menu():
        print("\nAttendance Management Menu")
        print("1. Add Attendance")
        print("2. List Attendance Records")
        print("3. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_member_id():
        return input("Enter Member ID: ")

    @staticmethod
    def get_class_id():
        return input("Enter Class ID: ")

    @staticmethod
    def get_status():
        print("Enter Attendance Status:")
        print("1. Present")
        print("2. Absent")
        return input("Enter choice (1/2): ")

    @staticmethod
    def display_attendance_success(attendance):
        print(f"Attendance for Member ID {attendance.member_id} on Class ID {attendance.class_id} recorded successfully!")

    @staticmethod
    def display_attendance_record(record):
        print(f"Member ID: {record.member_id}, Class ID: {record.class_id}, Status: {record.status}")

    @staticmethod
    def display_no_attendance_found():
        print("No attendance records found.")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")
