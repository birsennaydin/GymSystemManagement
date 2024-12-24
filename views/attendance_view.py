# views/attendance_view.py
from models.enums import AttendanceStatusEnum


class AttendanceView:
    @staticmethod
    def display_attendance_menu():
        print("\nAttendance Management Menu")
        print("1. Add Attendance")
        print("2. List Attendance Records")
        print("3. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_class_id(classes):
        print("\nEnter Class ID: ")
        for idx, member in enumerate(classes, 1):
            print(f"{idx}. {member.class_name}. {member.instructor}")
        member_choice = int(input("Enter the number of the class: "))
        return classes[member_choice - 1].id  # Return the selected class's ID

    @staticmethod
    def get_status():
        print("\nEnter Attendance Status:")
        for idx, method in enumerate(AttendanceStatusEnum, 1):
            print(f"{idx}. {method.value}")

        choice = input("Enter choice (1/2/3): ").strip()

        try:
            # Map the input to the enum, using zero-based indexing (subtract 1 from the choice)
            selected_attendance_status = list(AttendanceStatusEnum)[int(choice) - 1]
            return selected_attendance_status.value
        except (IndexError, ValueError):
            print("Invalid choice. Please select a valid payment method.")
            return AttendanceView.get_status()

    @staticmethod
    def display_attendance_success(attendance):
        print(f"Attendance for Member ID {attendance.member_id} on Class ID {attendance.class_id} recorded successfully!")

    @staticmethod
    def display_attendance_record(record, member_name, class_name):
        print(
            f"Appointment ID: {record.id}, Member: {member_name}, Class: {class_name}, Date: {record.attendance_date}, Status: {record.status}")

    @staticmethod
    def get_member_id(members):
        print("\nSelect a Member:")
        for idx, member in enumerate(members, 1):
            print(f"{idx}. {member.name}")
        member_choice = int(input("Enter the number of the member: "))
        return members[member_choice - 1].id  # Return the selected member's ID

    @staticmethod
    def display_no_attendance_found():
        print("No attendance records found.")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")

    @staticmethod
    def get_attendance_date():
        return input("Enter Attendance Date (YYYY-MM-DD HH:MM): ")
