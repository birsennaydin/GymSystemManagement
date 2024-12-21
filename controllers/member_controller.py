# controllers/member_controller.py
from models.member import Member
from views.member_view import MemberView

class MemberController:
    @staticmethod
    def manage_member():
        while True:
            choice = MemberView.display_member_menu()

            if choice == "1":
                MemberController.add_member()
            elif choice == "2":
                MemberController.list_members()
            elif choice == "3":
                MemberController.update_member()
            elif choice == "4":
                MemberView.display_return_to_main_menu()
                break
            else:
                MemberView.display_invalid_choice()

    @staticmethod
    def add_member():
        MemberView.display_member_details_prompt()
        name = MemberView.get_member_name()
        gym_location = MemberView.get_gym_location()
        membership_type = MemberView.display_membership_type_prompt()
        health_info = MemberView.get_health_info()

        member = Member(
            membership_id=Member.id_counter,  # Auto-increment membership_id
            name=name,
            email="test@email.com",  # Dummy email for now
            phone="123456789",  # Dummy phone number
            membership_type=membership_type,
            health_info=health_info,
            status="Active",
            gym_location_id=gym_location
        )
        MemberView.display_member_added_success(name)

    @staticmethod
    def list_members():
        members = Member.get_all()
        if not members:
            MemberView.display_no_members_found()
        else:
            for member in members:
                MemberView.display_member_list(member)

    @staticmethod
    def update_member():
        member_id = MemberView.get_member_id_for_update()
        member = Member.get_by_id(member_id)

        if not member:
            MemberView.display_member_not_found()
        else:
            MemberView.display_member_update_prompt(member)
            name = MemberView.get_new_value(member.name, "Name")
            gym_location = MemberView.get_new_value(member.gym_location_id, "Gym Location")
            membership_type = MemberView.get_new_value(member.membership_type, "Membership Type")
            health_info = MemberView.get_new_value(member.health_info, "Health Info")

            member.name = name
            member.gym_location_id = gym_location
            member.membership_type = membership_type
            member.health_info = health_info
            MemberView.display_member_updated_success(member.id)
