# controllers/member_controller.py
from models.user import User
from views.member_view import MemberView
from models.member import Member
from models.gym_location import GymLocation
from models.enums import MembershipType
from views.user_view import UserView


class MemberController:
    @staticmethod
    def manage_member(user):
        """
        Manages the member-related actions like add, update, delete, list.
        """
        from controllers.auth_controller import AuthController
        while True:
            choice = MemberView.display_member_menu(user.role.value)
            if choice == "1" and user.role.value != "MEMBER":  # Add member
                MemberController.add_member()
            elif choice == "2" and user.role.value != "MEMBER":  # List members
                MemberController.list_members()
            elif choice == "3" or (choice == "1" and user.role.value == "MEMBER"):  # Update member
                MemberController.update_member(user.id, user.role.value)
            elif choice == "4":  # Delete member
                MemberController.delete_member()
            elif choice == "5" or (choice == "2" and user.role.value == "MEMBER"):  # Return to main menu
                MemberView.display_return_to_main_menu()
                return AuthController.display_menu_based_on_role(user)
            else:
                MemberView.display_invalid_choice()

    @staticmethod
    def add_member():
        """
        Adds a new member to the system.
        """
        MemberView.display_member_details_prompt()
        users = User.get_all()
        if not users:
            print("Error: No users found.")
            return

        UserView.display_users(users)
        # Get user
        user_id = MemberView.get_user_id()
        user = User.get_users_by_id(user_id)
        if not user:
            print("Error: No users found. User ID is wrong.")
            return

        # Get member details
        name = MemberView.get_member_name()
        email = MemberView.get_member_email()
        phone = MemberView.get_member_phone()

        # Get membership type
        membership_type = MemberView.display_membership_type_prompt()
        membership_type = MembershipType[membership_type.upper()] if membership_type in MembershipType.__members__ else MembershipType.REGULAR

        health_info = MemberView.get_health_info()

        # Get available gym locations
        gym_locations = GymLocation.get_all()  # Fetch all gym locations
        MemberView.display_gym_locations(gym_locations)

        selected_location_idx = int(MemberView.get_selected_gym_location()) - 1
        if selected_location_idx < 0 or selected_location_idx >= len(gym_locations):
            print("Invalid selection. Returning to menu...")
            return

        gym_location = gym_locations[selected_location_idx]
        gym_location_id = gym_location.id  # Use the selected gym location's ID

        # Create the new member
        new_member = Member(
            name=name,
            email=email,
            phone=phone,
            membership_type=membership_type,
            health_info=health_info,
            status="Active",  # Default to Active status
            gym_location_id=gym_location_id,  # Set gym location ID
            user_id= user_id
        )

        MemberView.display_member_added_success(name)

        print(f"MEMBER: {new_member.name}, {new_member.email}, {new_member.phone}, {new_member.membership_type}, {gym_location_id}, {new_member.status}, USER: {user[0].email}")

    @staticmethod
    def list_members():
        """
        Lists all members in the system.
        """
        members = Member.get_all()  # Use the get_all method from the Member model
        if members:
            for member in members:
                MemberView.display_member_list(member)  # Assuming you want to display details
        else:
            MemberView.display_no_members_found()

    @staticmethod
    def update_member(user_id, role):
        """
        Updates a member's details.
        """
        members = Member.get_all()

        # Check if members exist
        if not members:
            print("Error: No members found.")
            return

        users = User.get_all()
        if not users:
            print("Error: No users found.")
            return

        # If the user is a member, allow them to update only their own profile
        if role == "MEMBER":
            member = Member.get_by_user_id(user_id)  # Get the member by user_id (the logged-in user's ID)
            if not member:
                print("Error: Member not found.")
                return
            print(f"Member: {member.name}, {member.email}, {member.phone}")

        else:
            # For Admin/Trainer, show the list of all members
            member_id = MemberView.get_member_id(members)
            member = Member.get_by_id(member_id)  # Find the member by ID

        # If member found, show current details and update
        if member:
            if role == "MEMBER":
                new_user_id = member.user_id
            else:
                UserView.display_users(users)
                new_user_id = MemberView.get_user_id()
                user = User.get_users_by_id(new_user_id)
                if not user:
                    print("Error: No users found. User ID is wrong.")
                    return

            # Get new values from the user
            name = MemberView.get_new_value(member.name, "Name")
            email = MemberView.get_new_value(member.email, "Email")
            phone = MemberView.get_new_value(member.phone, "Phone")
            membership_type = MemberView.display_membership_type_prompt()
            health_info = MemberView.get_new_value(member.health_info, "Health Info")

            # Get new gym location
            gym_locations = GymLocation.get_all()
            MemberView.display_gym_locations(gym_locations)
            selected_location_idx = int(MemberView.get_selected_gym_location()) - 1
            if selected_location_idx < 0 or selected_location_idx >= len(gym_locations):
                print("Invalid selection. Returning to menu...")
                return
            gym_location = gym_locations[selected_location_idx]
            gym_location_id = gym_location.id  # Use the selected gym location's ID

            # Update the member's details
            member.name = name
            member.email = email
            member.phone = phone
            member.membership_type = MembershipType[
                membership_type.upper()] if membership_type in MembershipType.__members__ else MembershipType.REGULAR
            member.health_info = health_info
            member.gym_location_id = gym_location_id
            member.user_id = new_user_id

            # Show updated details
            print(
                f"Updated member: {member.name}, {member.email}, {member.phone}, {member.membership_type}, {gym_location.name}, {member.status}")

            # Confirm the update by printing updated member details
            updated_member = Member.get_by_email(email)
            if updated_member:
                print(
                    f"Confirmed updated details: {updated_member.name}, {updated_member.email}, {updated_member.phone}, {updated_member.membership_type}, {updated_member.gym_location_id}, {updated_member.user_id}")

            MemberView.display_member_added_success(name)  # Display success message
        else:
            MemberView.display_member_not_found()

    @staticmethod
    def delete_member():
        """
        Deletes a member from the system by their email.
        """
        members = Member.get_all()
        # Check if members or classes are empty
        if not members:
            print("Error: No members found.")
            return

        member_id = MemberView.get_member_id(members)
        member = Member.get_by_id(member_id)

        if member:
            Member.members.remove(member)  # Remove the member from the list
            MemberView.display_member_deleted_success(member.email)  # Display success message
            print(f"Deleted member with email: {member.email}")
        else:
            MemberView.display_member_not_found()