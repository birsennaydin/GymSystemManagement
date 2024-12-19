from Models.enums import CityEnum, CountryEnum

class GymLocation:
    def __init__(self, location_id, location_name, city: CityEnum, country: CountryEnum):
        self.location_id = location_id
        self.location_name = location_name
        self.city = city
        self.country = country

    # Getters
    def get_location_id(self):
        return self.location_id

    def get_location_name(self):
        return self.location_name

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    # Setters
    def set_location_id(self, location_id):
        self.location_id = location_id

    def set_location_name(self, location_name):
        self.location_name = location_name

    def set_city(self, city: CityEnum):
        if isinstance(city, CityEnum):
            self.city = city
        else:
            raise ValueError(f"Invalid city. Valid options are: {[city.name for city in CityEnum]}")

    def set_country(self, country: CountryEnum):
        if isinstance(country, CountryEnum):
            self.country = country
        else:
            raise ValueError(f"Invalid country. Valid options are: {[country.name for country in CountryEnum]}")
