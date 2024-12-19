from views.gym_location_view import GymLocationView
from Models.gym_location import GymLocation
from Models.enums import CityEnum, CountryEnum

class GymLocationController:
    def __init__(self):
        self.locations = []

    def manage_locations(self):
        while True:
            choice = GymLocationView.display_gym_location_menu()
            if choice == "1":
                self.add_location()
            elif choice == "2":
                GymLocationView.display_locations(self.locations)
            elif choice == "3":
                self.select_location()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_location(self):
        location_data = GymLocationView.get_new_location_input()
        if location_data:
            location_id, location_name, city_name, country_name = location_data
            try:
                city = CityEnum[city_name.upper()]
                country = CountryEnum[country_name.upper()]
                new_location = GymLocation(location_id, location_name, city, country)
                self.locations.append(new_location)
                print("New gym location added successfully!")
            except KeyError:
                print("Invalid city or country entered.")

    def select_location(self):
        GymLocationView.display_locations(self.locations)
        location_id = GymLocationView.select_location()
        if location_id is not None:
            selected_location = next(
                (loc for loc in self.locations if loc.get_location_id() == location_id), None
            )
            if selected_location:
                print(f"Selected Gym Location: {selected_location.get_location_name()}")
            else:
                print("Location not found.")
