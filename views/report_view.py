# views/report_view.py

class ReportView:
    @staticmethod
    def display_report_menu():
        """
        Displays the menu for generating reports.
        """
        print("\nReport Menu:")
        print("1. Attendance Report")
        print("2. Payment Report")
        print("3. Member Growth Report")
        print("4. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_attendance_report(report):
        """
        Displays the attendance report.
        """
        print("\nAttendance Report:")
        for email, attendance in report.items():
            print(f"Member: {email}, Sessions Attended: {attendance}")

    @staticmethod
    def display_payment_report(report):
        """
        Displays the payment report.
        """
        print("\nPayment Report:")
        print(f"Total Revenue: ${report['total_revenue']}")
        print("Payment Methods Breakdown:")
        for method, amount in report['payment_methods'].items():
            print(f"{method}: ${amount}")

    @staticmethod
    def display_member_growth_report(report):
        """
        Displays the member growth report.
        """
        print("\nMember Growth Report:")
        print(f"Total Members Amount: {report['new_members']}")

    @staticmethod
    def display_invalid_choice():
        """
        Displays an error message for invalid choices.
        """
        print("Invalid choice. Please try again.")
