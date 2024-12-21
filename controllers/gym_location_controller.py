# controllers/gym_location_controller.py
from models.gym_location import GymLocation
from views.gym_location_view import GymLocationView

class GymLocationController:
    @staticmethod
    def manage_locations():
        while True:
            choice = GymLocationView.display_gym_location_menu()

            if choice == "1":
                GymLocationController.add_gym_location()
            elif choice == "2":
                GymLocationController.list_gym_locations()
            elif choice == "3":
                GymLocationController.update_gym_location()
            elif choice == "4":
                GymLocationView.display_return_to_main_menu()
                break
            else:
                GymLocationView.display_invalid_choice()

    @staticmethod
    def add_gym_location():
        name = GymLocationView.get_gym_location_name()
        address = GymLocationView.get_address()
        city = GymLocationView.get_city()
        country = GymLocationView.get_country()

        gym_location = GymLocation(name=name, address=address, city=city, country=country)
        GymLocationView.display_gym_location_added_success(gym_location)

    @staticmethod
    def list_gym_locations():
        locations = GymLocation.get_all()
        if not locations:
            GymLocationView.display_no_gym_locations_found()
        else:
            for location in locations:
                GymLocationView.display_gym_location_list(location)

    @staticmethod
    def update_gym_location():
        location_id = GymLocationView.get_gym_location_id_for_update()
        location = GymLocation.get_by_id(location_id)

        if not location:
            GymLocationView.display_gym_location_not_found()
        else:
            GymLocationView.display_gym_location_update_prompt(location)
            name = GymLocationView.get_new_value(location.name, "Name")
            address = GymLocationView.get_new_value(location.address, "Address")
            city = GymLocationView.get_new_value(location.city, "City")
            country = GymLocationView.get_new_value(location.country, "Country")

            location.name = name
            location.address = address
            location.city = city
            location.country = country
            GymLocationView.display_gym_location_updated_success(location.id)
