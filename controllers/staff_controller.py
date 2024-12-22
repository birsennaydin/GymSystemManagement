# controllers/staff_controller.py
from controllers.auth_controller import AuthController
from views.staff_view import StaffView  # Import StaffView for displaying staff menus
from models.staff import Staff
from models.enums import StaffRole

class StaffController:
    def __init__(self):
        self.staff_list = []

    def manage_staff(self, user):
        """
        Manages the staff options such as add, update, list, etc.
        Displays the staff menu and handles user choices.
        """
        while True:
            # Display the staff management menu
            choice = StaffView.display_staff_menu()

            if choice == "1":
                # Add staff
                self.add_staff()
            elif choice == "2":
                # Update staff
                self.update_staff()
            elif choice == "3":
                # List staff
                self.list_staff()
            elif choice == "4":
                # Return to main menu
                StaffView.display_return_to_main_menu()
                return AuthController.display_menu_based_on_role(user)
            else:
                # Invalid choice
                StaffView.display_invalid_choice()

    def add_staff(self):
        """
        Handles adding a new staff member.
        """
        StaffView.display_add_staff_prompt()
        name = StaffView.get_staff_name()
        role_input = StaffView.get_staff_role()

        try:
            print(f"Staff Role: {role_input.upper()}, Role List: {StaffRole}")
            role = StaffRole[role_input.upper()]  # Converts input to StaffRole enum
        except KeyError:
            StaffView.display_invalid_role()
            return

        staff_id = len(self.staff_list) + 1
        new_staff = Staff(staff_id, name, role)
        self.staff_list.append(new_staff)
        StaffView.display_staff_added_success(name, role.name)

    def update_staff(self):
        """
        Handles updating staff details.
        """
        staff_id = int(input("Enter the staff ID to update: "))
        staff = self.get_staff_by_id(staff_id)

        if staff:
            name = StaffView.get_new_name(staff.get_name())
            role_input = StaffView.get_new_role(staff.get_role().name)

            try:
                role = StaffRole[role_input.upper()]
            except KeyError:
                StaffView.display_invalid_role()
                return

            staff.set_name(name)
            staff.set_role(role)
            StaffView.display_staff_updated_success(staff_id, name, role.name)
        else:
            print(f"Staff with ID {staff_id} not found.")

    def list_staff(self):
        """
        Lists all staff members.
        """
        StaffView.display_staff_list(self.staff_list)

    def get_staff_by_id(self, staff_id):
        """
        Gets a staff member by ID.
        """
        for staff in self.staff_list:
            if staff.get_staff_id() == staff_id:
                return staff
        return None
