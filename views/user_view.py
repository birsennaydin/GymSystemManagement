# views/user_view.py

class UserView:
    @staticmethod
    def display_user_menu():
        """
        Displays the user management menu.
        """
        print("\nUser Management Menu")
        print("1. List Users")
        print("2. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_user_email():
        return input("Enter the user's email: ")

    @staticmethod
    def get_user_password():
        return input("Enter the user's password: ")

    @staticmethod
    def get_user_role(associate_role):
        """
        Displays the available roles and ensures the user picks a valid one.
        """
        if associate_role == "MEMBER":
            return "MEMBER"

        print("Choose the role for the user:")
        print("1. Manager")
        print("2. Trainer")
        print("3. Attendant")
        role_choice = input("Enter choice (1/2/3): ").strip()
        role_dict = {
            "1": "MANAGER",
            "2": "TRAINER",
            "3": "ATTENDANT"
        }
        return role_dict.get(role_choice)

    @staticmethod
    def display_gym_locations(gym_locations):
        """
        Displays the gym locations for the user to select.
        """
        print("Select a Gym Location:")
        for idx, location in enumerate(gym_locations, 1):
            print(f"{idx}. {location.name} - {location.city}, {location.country}")
        return input("Enter the number of the gym location: ").strip()

    @staticmethod
    def display_user_added_success(email):
        print(f"User with email {email} added successfully!")

    @staticmethod
    def display_user_updated_success(email):
        print(f"User with email {email} updated successfully!")

    @staticmethod
    def display_user_deleted_success(email):
        print(f"User with email {email} deleted successfully!")

    @staticmethod
    def display_user(user):
        print(f"Email: {user.email}, Role: {user.role.value}")

    @staticmethod
    def display_users(users):
        print("Users List:")
        for idx, user in enumerate(users, 1):
            print(f"ID:{idx},  Email: {user.email}, Role: {user.role.value}")

    @staticmethod
    def display_no_users_found():
        print("No users found.")

    @staticmethod
    def display_user_not_found():
        print("User not found.")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")
