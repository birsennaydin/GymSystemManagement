import unittest
from models.staff import Staff
from models.enums import StaffRole


class TestStaff(unittest.TestCase):

    def setUp(self):
        """This method will run before every test."""
        # Clear the staff list before each test to avoid any conflicts.
        Staff.staff_members = []
        Staff.id_counter = 1

    def test_create_staff(self):
        """Test that a staff member is created successfully with valid details."""
        staff = Staff(
            name="Birsen",
            role=StaffRole.TRAINER,
            email="birsen@example.com",
            phone="1234567890",
            gym_location_id=1
        )

        self.assertEqual(len(Staff.staff_members), 1)  # One staff member should be created
        self.assertEqual(staff.name, "Birsen")
        self.assertEqual(staff.role, "TRAINER")
        self.assertEqual(staff.email, "birsen@example.com")
        self.assertEqual(staff.phone, "1234567890")

    def test_get_staff_by_role(self):
        """Test that staff can be filtered by role."""
        Staff(
            name="Birsen",
            role=StaffRole.TRAINER,
            email="birsen@example.com",
            phone="1234567890",
            gym_location_id=1
        )
        Staff(
            name="Melis",
            role=StaffRole.MANAGER,
            email="melis@example.com",
            phone="9876543210",
            gym_location_id=1
        )

        trainers = Staff.get_by_role("TRAINER")
        self.assertEqual(len(trainers), 1)
        self.assertEqual(trainers[0].name, "Birsen")

    def tearDown(self):
        """This method will run after every test."""
        # Reset the staff list after each test to maintain isolation
        Staff.staff_members = []
        Staff.id_counter = 1


if __name__ == '__main__':
    unittest.main()
