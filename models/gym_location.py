# models/gym_location.py
from models.enums import CityEnum, CountryEnum

class GymLocation:
    id_counter = 1
    locations = []

    def __init__(self, name, address, city, country, manager_id):
        self._id = GymLocation.id_counter
        self._name = None
        self._address = None
        self._city = None
        self._country = None
        self._manager_id = None

        self.name = name
        self.address = address
        self.city = city  # Enum'dan gelen city değeri
        self.country = country
        self.manager_id = manager_id

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
        if value not in CityEnum.__members__:
            raise ValueError(f"Invalid city. Please choose from {', '.join(CityEnum.__members__.keys())}.")
        self._city = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if value not in CountryEnum.__members__:
            raise ValueError(f"Invalid country. Please choose from {', '.join(CountryEnum.__members__.keys())}.")
        self._country = value

    @property
    def manager_id(self):
        return self._manager_id

    @manager_id.setter
    def manager_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Manager ID must be an integer.")
        self._manager_id = value

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
            cls.locations.append(GymLocation(
                name="Downtown Gym",
                address="123 Main St",
                city="LONDON",
                country="UNITED_KINGDOM",
                manager_id=1
            ))
            cls.locations.append(GymLocation(
                name="City Center Gym",
                address="456 Market St",
                city="NEW_YORK",
                country="USA",
                manager_id=2
            ))

GymLocation.initialize_default_locations()
