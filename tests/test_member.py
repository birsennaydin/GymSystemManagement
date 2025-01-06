import unittest
from models.member import Member
from models.enums import MembershipType


class TestMember(unittest.TestCase):

    def setUp(self):
        """This method will run before every test."""
        # Clear the members list before each test to avoid any conflicts.
        Member.members = []
        Member.id_counter = 1

    def test_create_member(self):
        """Test that a member is created successfully with valid details."""
        member = Member(
            name="John Doe",
            email="john.doe@example.com",
            phone="1234567890",
            membership_type=MembershipType.REGULAR,
            health_info="Healthy",
            status="Active",
            gym_location_id=1,
            user_id=101
        )

        self.assertEqual(len(Member.members), 1)  # One member should be created
        self.assertEqual(member.name, "John Doe")
        self.assertEqual(member.email, "john.doe@example.com")
        self.assertEqual(member.membership_type, MembershipType.REGULAR)
        self.assertEqual(member.status, "Active")
        self.assertEqual(member.gym_location_id, 1)
        self.assertEqual(member.user_id, 101)

    def test_get_member_by_email(self):
        """Test that a member can be retrieved by email."""
        member = Member(
            name="John Doe",
            email="john.doe@example.com",
            phone="1234567890",
            membership_type=MembershipType.REGULAR,
            health_info="Healthy",
            status="Active",
            gym_location_id=1,
            user_id=101
        )

        found_member = Member.get_by_email("john.doe@example.com")
        self.assertEqual(found_member.email, "john.doe@example.com")
        self.assertEqual(found_member.name, "John Doe")

    def test_invalid_user_id(self):
        """Test that setting an invalid user ID raises a ValueError."""
        with self.assertRaises(ValueError):
            member = Member(
                name="John Doe",
                email="john.doe@example.com",
                phone="1234567890",
                membership_type=MembershipType.REGULAR,
                health_info="Healthy",
                status="Active",
                gym_location_id=1,
                user_id="invalid_user_id"  # Invalid user ID type
            )

    def test_invalid_gym_location_id(self):
        """Test that setting an invalid gym location ID raises a ValueError."""
        with self.assertRaises(ValueError):
            member = Member(
                name="John Doe",
                email="john.doe@example.com",
                phone="1234567890",
                membership_type=MembershipType.REGULAR,
                health_info="Healthy",
                status="Active",
                gym_location_id="invalid_location",  # Invalid gym location ID type
                user_id=101
            )

    def test_get_all_members(self):
        """Test that the get_all method returns all members."""
        member1 = Member(
            name="Alice",
            email="alice@example.com",
            phone="9876543210",
            membership_type=MembershipType.REGULAR,
            health_info="Normal",
            status="Active",
            gym_location_id=2,
            user_id=102
        )
        member2 = Member(
            name="Bob",
            email="bob@example.com",
            phone="1231231234",
            membership_type=MembershipType.PREMIUM,
            health_info="Normal",
            status="Active",
            gym_location_id=3,
            user_id=103
        )

        members = Member.get_all()
        self.assertEqual(len(members), 2)
        self.assertEqual(members[0].name, "Alice")
        self.assertEqual(members[1].name, "Bob")

    def tearDown(self):
        """This method will run after every test."""
        # Reset the members list after each test to maintain isolation
        Member.members = []
        Member.id_counter = 1


if __name__ == '__main__':
    unittest.main()
