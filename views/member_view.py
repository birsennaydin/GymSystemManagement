class MemberView:
    @staticmethod
    def display_member_menu():
        print("\nMember Management Menu")
        print("1. Add Member")
        print("2. List Members")
        print("3. Update Member")
        print("4. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_member_details_prompt():
        print("Enter new member details:")

    @staticmethod
    def get_member_name():
        return input("Name: ")

    @staticmethod
    def get_gym_location():
        return input("Gym Location: ")

    @staticmethod
    def display_member_added_success(name):
        print(f"Member {name} added successfully!")

    @staticmethod
    def get_member_id_for_update():
        return int(input("Enter Member ID to update: "))

    @staticmethod
    def display_member_update_prompt(member):
        print(f"Updating details for {member.get_name()}:")

    @staticmethod
    def get_new_value(current_value, prompt):
        new_value = input(f"{prompt} (current: {current_value}): ")
        return new_value or current_value

    @staticmethod
    def display_member_updated_success(member_id):
        print(f"Member {member_id} updated successfully!")

    @staticmethod
    def display_no_members_found():
        print("No members found.")

    @staticmethod
    def display_member_list(member):
        print(
            f"ID: {member.get_member_id()}, Name: {member.get_name()}, "
            f"Membership: {member.get_membership_type().value}, Gym Location: {member.get_gym_location()}"
        )

    @staticmethod
    def display_membership_type_prompt():
        print("Choose Membership Type:")
        print("1. Regular")
        print("2. Premium")
        print("3. Trial")
        return input("Enter choice (1/2/3): ")

    @staticmethod
    def display_membership_type_invalid():
        print("Invalid choice. Defaulting to Regular.")

    @staticmethod
    def display_member_not_found():
        print("Member not found!")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")

    @staticmethod
    def get_health_info():
        return input("Enter Health Info: ")
