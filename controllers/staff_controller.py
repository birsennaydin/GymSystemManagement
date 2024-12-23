# controllers/staff_controller.py
from models.gym_location import GymLocation
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
        from controllers.auth_controller import AuthController
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
        email = StaffView.get_staff_email()
        phone = StaffView.get_staff_phone()
        role_input = StaffView.get_staff_role()

        # Get available gym locations and select one
        gym_locations = GymLocation.get_all()  # Get all gym locations
        gym_location_id = StaffView.get_gym_location(gym_locations)  # Get gym location ID

        try:
            # Convert the string to StaffRole enum
            role = StaffRole[role_input]  # Convert to StaffRole enum
        except KeyError:
            StaffView.display_invalid_role()
            return

        staff_id = len(self.staff_list) + 1
        new_staff = Staff(name, role, email, phone, gym_location_id)  # Create a new staff member with gym_location_id
        self.staff_list.append(new_staff)
        StaffView.display_staff_added_success(name, role.name)

    def update_staff(self):
        """
        Handles updating staff details.
        """
        # List the staff first
        StaffView.display_staff_list(self.staff_list)

        # Get the staff ID to update
        staff_index = int(input("Enter the number of the staff member to update: ")) - 1
        if 0 <= staff_index < len(self.staff_list):
            staff = self.staff_list[staff_index]
            StaffView.display_update_staff_prompt(staff)

            # Get updated details
            name = StaffView.get_new_name(staff.name)  # Get updated name
            role_input = StaffView.get_new_role(staff.role)  # Get updated role

            # Get email update
            email = input(f"Enter new email (current: {staff.email}): ") or staff.email

            # Get phone update
            phone = input(f"Enter new phone (current: {staff.phone}): ") or staff.phone

            # Get gym location update
            gym_locations = GymLocation.get_all()  # Get all gym locations
            gym_location_id = StaffView.get_gym_location(gym_locations)  # Get gym location ID

            try:
                # Convert the string to StaffRole enum
                role = StaffRole[role_input]  # Convert to StaffRole enum
            except KeyError:
                StaffView.display_invalid_role()
                return

            # Update staff details
            staff.name = name
            staff.role = role
            staff.email = email  # Update email
            staff.phone = phone  # Update phone
            staff.gym_location_id = gym_location_id  # Update gym location
            print(f"Update Staff: {staff.name}, {staff.role}, {staff.email}, {staff.phone}, {staff.gym_location_id}")
            StaffView.display_staff_updated_success(name, role.name, staff.email)
        else:
            print("Invalid staff selection.")

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
