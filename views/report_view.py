class ReportView:
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