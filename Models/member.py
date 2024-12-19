from Models.enums import MembershipType

class Member:

    member_next_id = 1

    def __init__(self, name, membership_type: MembershipType, gym_location, health_info):
        self.member_id = Member.member_next_id
        Member.member_next_id += 1
        self.name = name
        self.membership_type = membership_type
        self.gym_location = gym_location
        self.health_info = health_info

    # Getters and Setters
    def get_member_id(self):
        return self.member_id

    def set_member_id(self, member_id):
        self.member_id = member_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_membership_type(self):
        return self.membership_type

    def set_membership_type(self, membership_type: MembershipType):
        if isinstance(membership_type, MembershipType):
            self.membership_type = membership_type
        else:
            raise ValueError("Invalid membership type")

    def get_health_info(self):
        return self.health_info

    def set_health_info(self, health_info):
        self.health_info = health_info

    def get_gym_location(self):
        return self.gym_location

    def set_gym_location(self, gym_location):
        self.gym_location = gym_location
