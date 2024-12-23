class StaffView:
    @staticmethod
    def display_staff_menu():
        """
        Displays the menu for managing staff (add, update, list).
        """
        print("\nStaff Management Menu:")
        print("1. Add Staff")
        print("2. Update Staff")
        print("3. List Staff")
        print("4. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_add_staff_prompt():
        """
        Prompts for adding a new staff member.
        """
        print("Enter new staff details:")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")

    @staticmethod
    def get_staff_name():
        """
        Prompts for the staff name.
        """
        return input("Staff Name: ")

    @staticmethod
    def get_staff_email():
        """
        Prompts for the staff email.
        """
        return input("Staff Email: ")

    @staticmethod
    def get_staff_phone():
        """
        Prompts for the staff phone number.
        """
        return input("Staff Phone: ")

    @staticmethod
    def get_staff_role():
        """
        Prompts for the staff role and returns the role as a string.
        """
        print("Choose a role for the staff:")
        print("1. MANAGER")
        print("2. TRAINER")
        print("3. ATTENDANT")
        role_choice = input("Enter role choice (1/2/3): ").strip()

        # Convert the role_choice into the corresponding StaffRole enum
        role_dict = {
            "1": "MANAGER",
            "2": "TRAINER",
            "3": "ATTENDANT"
        }

        return role_dict.get(role_choice)

    @staticmethod
    def get_gym_location(gym_locations):
        """
        Prompts for the staff's gym location.
        """
        print("Select Gym Location:")
        for idx, location in enumerate(gym_locations, 1):
            print(f"{idx}. {location.name} - {location.city}")

        location_choice = input("Enter choice: ").strip()
        return gym_locations[int(location_choice) - 1].id

    @staticmethod
    def display_staff_added_success(name, role):
        """
        Displays success message after adding a new staff member.
        """
        print(f"Staff {name} added successfully with the role {role}.")

    @staticmethod
    def display_invalid_role():
        """
        Displays an error message for invalid role.
        """
        print("Invalid role. Please choose from Manager, Trainer, or Attendant.")

    @staticmethod
    def display_update_staff_prompt(staff):
        """
        Prompts for updating the staff member's details.
        """
        print(f"Updating details for {staff.get_name()}:")

    @staticmethod
    def get_new_name(current_name):
        """
        Prompts the user to update the staff name.
        """
        return input(f"Enter new name (current: {current_name}): ") or current_name

    @staticmethod
    def get_new_role(current_role):
        """
        Prompts the user to update the staff role.
        """
        print(f"Enter new role (current: {current_role}): ")
        print("1. Manager")
        print("2. Trainer")
        print("3. Attendant")
        role_choice = input("Enter new role (1/2/3): ").strip()
        role_dict = {
            "1": "MANAGER",
            "2": "TRAINER",
            "3": "ATTENDANT"
        }
        return role_dict.get(role_choice)

    @staticmethod
    def display_staff_updated_success(name, role, email):
        """
        Displays success message after updating a staff member.
        """
        print(f"Staff {email} updated to {name} with role {role}.")

    @staticmethod
    def display_no_staff_found():
        """
        Displays a message when no staff are found.
        """
        print("No staff members found.")

    @staticmethod
    def display_staff_list(staff_list):
        """
        Displays the list of staff members.
        """
        if not staff_list:
            print("No staff members to display.")
        else:
            for staff in staff_list:
                print(
                    f"ID: {staff.get_staff_id()}, Name: {staff.get_name()}, Role: {staff.get_role()}, Email: {staff.email}, Phone: {staff.phone}")

    @staticmethod
    def display_invalid_choice():
        """
        Displays an error message when an invalid choice is made.
        """
        print("Invalid choice. Please try again.")
