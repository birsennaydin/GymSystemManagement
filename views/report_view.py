# views/report_view.py
class ReportView:
    @staticmethod
    def display_report_menu():
        print("\nReport Menu")
        print("1. Monthly Income Report")
        print("2. Member Attendance Report")
        print("3. Popular Class Report")
        print("4. Trainer Performance Report")
        print("5. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_monthly_income_report(income):
        print(f"Total Income for the month: ${income:.2f}")

    @staticmethod
    def display_member_attendance_report(attendance_data):
        print("Member Attendance Report:")
        for data in attendance_data:
            print(data)

    @staticmethod
    def display_popular_class_report(popular_classes):
        print("Popular Classes Report:")
        for class_id, participants in popular_classes.items():
            print(f"Class ID {class_id}: {participants} participants")

    @staticmethod
    def display_trainer_performance_report(trainer_performance):
        print("Trainer Performance Report:")
        for trainer_id, sessions in trainer_performance.items():
            print(f"Trainer {trainer_id}: {sessions} sessions")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")
