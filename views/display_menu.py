class DisplayMenu:
    @staticmethod
    def display_menu():
        print("\nWelcome to St Mary's Fitness System")
        print("1. Member Management")
        print("2. Workout Zones")
        print("3. Appointments")
        print("4. Payments and Subscriptions")
        print("5. Attendance Tracking")
        print("6. Staff Management")
        print("7. Reports")
        print("8. Manage Gym Locations")
        print("9. Exit")

        return input("Enter your choice: ").strip()
