# models/gym_location.py
from models.enums import CityEnum, CountryEnum

class GymLocation:
    id_counter = 1
    locations = []

    def __init__(self, name, address, city, country):
        self._id = GymLocation.id_counter
        self._name = None
        self._address = None
        self._city = None
        self._country = None

        self.name = name
        self.address = address
        self.city = city
        self.country = country

        GymLocation.id_counter += 1
        GymLocation.locations.append(self)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Gym location name cannot be empty.")
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not value:
            raise ValueError("Address cannot be empty.")
        self._address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        try:
            if value is None or value not in [member.value for member in CityEnum]:
                raise ValueError(
                    f"Invalid city: {value}. Please choose from {', '.join([member.value for member in CityEnum])}.")
            self._city = value

        except ValueError as e:
            print(f"Error: {e}")

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        print(f"COUNTRYYY: {value}")
        if value not in [member.value for member in CountryEnum]:
            raise ValueError(f"Invalid country. Please choose from {', '.join([member.value for member in CountryEnum])}.")
        self._country = value

    @classmethod
    def get_all(cls):
        """
        Returns all gym locations.
        """
        return cls.locations

    @classmethod
    def get_by_id(cls, id):
        """
        Returns a gym location by its ID.
        """
        return next((location for location in cls.locations if location.id == id), None)

    @classmethod
    def get_selected_gym_location(cls):
        """
        Allows the user to select a gym location from a list of available locations.
        """
        print("\nAvailable Gym Locations:")
        for idx, location in enumerate(cls.locations, 1):
            print(f"{idx}. {location.name} - {location.city}, {location.country}")
        choice = input(f"Select a gym location (1-{len(cls.locations)}): ").strip()

        try:
            selected_location = cls.locations[int(choice) - 1]
            return selected_location.id
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")
            return None

    @classmethod
    def initialize_default_locations(cls):
        if not cls.locations:
            GymLocation(
                name="Downtown Gym",
                address="123 Main St",
                city="London",
                country="United Kingdom"
            )
            GymLocation(
                name="City Center Gym",
                address="456 Market St",
                city="New York",
                country="United States of America"
            )

GymLocation.initialize_default_locations()
