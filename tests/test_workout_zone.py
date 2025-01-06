import unittest

from models.enums import StaffRole
from models.workout_zone import WorkoutZone
from models.gym_location import GymLocation
from models.staff import Staff


class TestWorkoutZone(unittest.TestCase):

    def setUp(self):
        """This method will run before every test."""
        # Clear the workout zones list before each test to avoid any conflicts.
        WorkoutZone.zones = []
        WorkoutZone.id_counter = 1
        GymLocation.locations = []
        Staff.staff = []

    def test_create_workout_zone(self):
        """Test that a workout zone is created successfully with valid details."""
        gym_location = GymLocation(
                name="Downtown Gym",
                address="123 Main St",
                city="London",
                country="United Kingdom"
            )
        staff = Staff(name="Melis", role=StaffRole["TRAINER"], email="trainer@example.com", phone="1234567890",
                        gym_location_id=1)

        workout_zone = WorkoutZone(
            name="Cardio Zone",
            zone_type="Cardio",
            gym_location_id=gym_location.id,
            staff_id=staff.id
        )

        self.assertEqual(len(WorkoutZone.zones), 1)  # One workout zone should be created
        self.assertEqual(workout_zone.name, "Cardio Zone")
        self.assertEqual(workout_zone.zone_type, "Cardio")
        self.assertEqual(workout_zone.gym_location_id, gym_location.id)
        self.assertEqual(workout_zone.staff_id, staff.id)

    def test_get_workout_zones_by_gym_location(self):
        """Test that workout zones can be filtered by gym location."""
        gym_location1 = GymLocation(
            name="Downtown Gym",
            address="123 Main St",
            city="London",
            country="United Kingdom"
        )
        gym_location2 = GymLocation(
            name="Secondary Gym Location",
            address="145 Main St",
            city="London",
            country="United Kingdom"
        )

        staff = Staff(name="Melis", role=StaffRole["TRAINER"], email="trainer@example.com", phone="1234567890",
                      gym_location_id=1)

        WorkoutZone(
            name="Cardio Zone",
            zone_type="Cardio",
            gym_location_id=gym_location1.id,
            staff_id=staff.id
        )
        WorkoutZone(
            name="Strength Zone",
            zone_type="Strength",
            gym_location_id=gym_location2.id,
            staff_id=staff.id
        )

        zones = WorkoutZone.get_by_gym_location(gym_location1.id)
        self.assertEqual(len(zones), 1)
        self.assertEqual(zones[0].name, "Cardio Zone")

    def test_get_workout_zone_by_id(self):
        """Test that a workout zone can be retrieved by its ID."""
        gym_location = GymLocation(
            name="Gym Location",
            address="145 Main St",
            city="London",
            country="United Kingdom"
        )
        staff = Staff(name="Melis", role=StaffRole["TRAINER"], email="trainer@example.com", phone="1234567890",
                      gym_location_id=1)

        workout_zone = WorkoutZone(
            name="Cardio Zone",
            zone_type="Cardio",
            gym_location_id=gym_location.id,
            staff_id=staff.id
        )

        found_zone = WorkoutZone.get_by_id(workout_zone.id)
        self.assertEqual(found_zone.id, workout_zone.id)
        self.assertEqual(found_zone.name, "Cardio Zone")

    def tearDown(self):
        """This method will run after every test."""
        # Reset the workout zones and other related lists after each test to maintain isolation
        WorkoutZone.zones = []
        WorkoutZone.id_counter = 1
        GymLocation.locations = []
        Staff.staff = []


if __name__ == '__main__':
    unittest.main()
