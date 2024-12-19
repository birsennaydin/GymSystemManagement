from Models.member import Member
from Models.enums import MembershipType
from views.member_view import MemberView


class MemberController:
    def __init__(self):
        self.members = []

    def manage_member(self):
        while True:
            choice = MemberView.display_member_menu()

            if choice == "1":
                self.add_member()
            elif choice == "2":
                self.list_members()
            elif choice == "3":
                member_id = MemberView.get_member_id_for_update()
                self.update_member(member_id)
            elif choice == "4":
                MemberView.display_return_to_main_menu()
                break
            else:
                MemberView.display_invalid_choice()

    def add_member(self):
        MemberView.display_member_details_prompt()
        name = MemberView.get_member_name()
        membership_type = self.get_membership_type()
        gym_location = MemberView.get_gym_location()
        health_info = MemberView.get_health_info()

        new_member = Member(name, membership_type, gym_location, health_info)
        self.members.append(new_member)
        MemberView.display_member_added_success(name)

    def update_member(self, member_id):
        member = self.get_member_by_id(member_id)
        if member:
            MemberView.display_member_update_prompt(member)
            member.set_name(MemberView.get_new_value(member.get_name(), "New Name"))
            member.set_membership_type(
                self.get_membership_type() or member.get_membership_type()
            )
            member.set_gym_location(
                MemberView.get_new_value(
                    member.get_gym_location(), "New Gym Location"
                )
            )
            MemberView.display_member_updated_success(member_id)
        else:
            MemberView.display_member_not_found()

    def get_member_by_id(self, member_id):
        for member in self.members:
            if member.get_member_id() == member_id:
                return member
        return None

    def list_members(self):
        if not self.members:
            MemberView.display_no_members_found()
            return
        for member in self.members:
            MemberView.display_member_list(member)

    @staticmethod
    def get_membership_type():
        choice = MemberView.display_membership_type_prompt()
        if choice == '1':
            return MembershipType.REGULAR
        elif choice == '2':
            return MembershipType.PREMIUM
        elif choice == '3':
            return MembershipType.TRIAL
        else:
            MemberView.display_membership_type_invalid()
            return MembershipType.REGULAR
