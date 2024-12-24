# views/member_view.py
from models.gym_location import GymLocation


class MemberView:
    @staticmethod
    def display_member_menu():
        print("\nMember Management Menu")
        print("1. Add Member")
        print("2. List Members")
        print("3. Update Member")
        print("4. Delete Member")  # Add delete option
        print("5. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_member_details_prompt():
        print("Enter new member details:")

    @staticmethod
    def get_member_name():
        return input("Name: ")

    @staticmethod
    def get_member_email():
        return input("Email: ")

    @staticmethod
    def get_member_phone():
        return input("Phone: ")

    @staticmethod
    def display_membership_type_prompt():
        print("Choose Membership Type:")
        print("1. Regular")
        print("2. Premium")
        print("3. Trial")
        membership_type = input("Enter choice (1/2/3): ").strip()
        if membership_type == "1":
            return "REGULAR"
        elif membership_type == "2":
            return "PREMIUM"
        elif membership_type == "3":
            return "TRIAL"
        else:
            print("Invalid membership type. Defaulting to Regular.")
            return "REGULAR"

    @staticmethod
    def get_health_info():
        return input("Enter Health Info: ")

    @staticmethod
    def display_gym_locations(gym_locations):
        print("Choose a Gym Location:")
        for idx, location in enumerate(gym_locations, 1):
            print(f"{idx}. {location.name} - {location.city}, {location.country}")

    @staticmethod
    def get_selected_gym_location():
        return input("Enter the number of the gym location: ")

    @staticmethod
    def display_member_added_success(name):
        print(f"Member {name} added successfully!")

    @staticmethod
    def display_no_members_found():
        print("No members found.")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")

    @staticmethod
    def display_member_list(member):
        # Find the gym location by the gym_location_id
        gym_location = GymLocation.get_by_id(member.gym_location_id)  # Get the GymLocation object
        gym_location_name = gym_location.name if gym_location else "Unknown Location"

        print(
            f"ID: {member.id}, Name: {member.name}, Membership: {member.membership_type}, Gym Location: {gym_location_name}")

    @staticmethod
    def display_member_not_found():
        print("Member not found!")

    @staticmethod
    def display_member_update_prompt(member):
        """
        Displays the current details of the member before updating.
        """
        print(f"Updating details for {member.name}:")
        print(f"Current Email: {member.email}")
        print(f"Current Phone: {member.phone}")
        print(f"Current Membership Type: {member.membership_type}")
        print(f"Current Health Info: {member.health_info}")
        print(f"Current Gym Location: {GymLocation.get_by_id(member.gym_location_id).name}")

    @staticmethod
    def get_new_value(current_value, prompt):
        """
        Prompts the user to enter a new value. If the user enters nothing, the current value is kept.
        """
        new_value = input(f"{prompt} (current: {current_value}): ")
        return new_value or current_value

    @staticmethod
    def display_member_deleted_success(email):
        print(f"Member with email {email} has been deleted successfully!")

    @staticmethod
    def get_member_id(members):
        print("\nSelect a Member:")
        for idx, member in enumerate(members, 1):
            print(f"{idx}. {member.name}")
        member_choice = int(input("Enter the number of the member: "))
        return members[member_choice - 1].id  # Return the selected member's ID