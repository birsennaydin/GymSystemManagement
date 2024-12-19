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
        self.city = city
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
        return cls.locations

    @classmethod
    def get_by_id(cls, id):
        return next((location for location in cls.locations if location.id == id), None)
