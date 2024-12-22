# views/display_menu.py

class DisplayMenu:
    @staticmethod
    def display_admin_menu():
        """
        Displays the full menu for the Admin/Manager, including all system functionalities.
        """
        print("\nAdmin/Manager Menu:")
        print("1. Member Management")
        print("2. Workout Zones")
        print("3. Appointments")
        print("4. Payments and Subscriptions")
        print("5. Attendance Tracking")
        print("6. Staff Management")
        print("7. Reports")
        print("8. Manage Gym Locations")
        print("9. User Management")  # New option for managing users
        print("10. Logout")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_trainer_menu():
        """
        Displays the menu for Trainers, which includes access to appointments, attendance, and members.
        """
        print("\nTrainer Menu:")
        print("1. View Appointments")
        print("2. Manage Your Profile")
        print("3. Attendance Tracking")
        print("4. View Members")
        print("5. Logout")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_attendant_menu():
        """
        Displays the menu for Attendants, with access to attendance tracking and workout zones.
        """
        print("\nAttendant Menu:")
        print("1. Track Attendance")
        print("2. Manage Workout Zones")
        print("3. Logout")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_member_menu():
        """
        Displays the menu for Members, with access to their own profile and scheduling appointments.
        """
        print("\nMember Menu:")
        print("1. View Your Profile")
        print("2. View Your Appointments")
        print("3. Attendance Tracking")
        print("4. Logout")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_return_to_main_menu():
        """
        Displays the option to return to the main menu or log out.
        """
        print("\nReturning to the main menu...")
