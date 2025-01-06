import unittest
from models.gym_location import GymLocation
from models.enums import CityEnum, CountryEnum


class TestGymLocation(unittest.TestCase):

    def setUp(self):
        """This method will run before every test."""
        # Clear the gym locations list before each test to avoid any conflicts.
        GymLocation.locations = []
        GymLocation.id_counter = 1

    def test_create_gym_location(self):
        """Test that a gym location is created successfully with valid details."""
        gym_location = GymLocation(
            name="Downtown Gym",
            address="123 Main St",
            city=CityEnum.LONDON.value,
            country=CountryEnum.UNITED_KINGDOM.value
        )

        self.assertEqual(len(GymLocation.locations), 1)  # One gym location should be created
        self.assertEqual(gym_location.name, "Downtown Gym")
        self.assertEqual(gym_location.city, CityEnum.LONDON.value)
        self.assertEqual(gym_location.country, CountryEnum.UNITED_KINGDOM.value)

    def test_invalid_country(self):
        """Test that an invalid country raises a ValueError."""
        with self.assertRaises(ValueError):
            gym_location = GymLocation(
                name="Invalid Country Gym",
                address="789 Elm St",
                city=CityEnum.NEW_YORK.value,
                country="InvalidCountry"  # Invalid country
            )

    def test_get_all_gym_locations(self):
        """Test that all gym locations can be retrieved."""
        GymLocation(
            name="Downtown Gym",
            address="123 Main St",
            city=CityEnum.LONDON.value,
            country=CountryEnum.UNITED_KINGDOM.value
        )

        locations = GymLocation.get_all()
        self.assertEqual(len(locations), 1)

    def tearDown(self):
        """This method will run after every test."""
        # Reset the gym locations list after each test to maintain isolation
        GymLocation.locations = []
        GymLocation.id_counter = 1


if __name__ == '__main__':
    unittest.main()
