# views/gym_location_view.py
from models.enums import CityEnum, CountryEnum


class GymLocationView:
    @staticmethod
    def display_gym_location_menu():
        print("\nGym Location Management Menu")
        print("1. Add Gym Location")
        print("2. List Gym Locations")
        print("3. Update Gym Location")
        print("4. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_gym_location_name():
        return input("Enter Gym Location Name: ")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")

    @staticmethod
    def get_address():
        return input("Enter Address: ")

    @staticmethod
    def get_city():
        print("\nEnter City ID: ")

        for idx, method in enumerate(CityEnum, 1):
            print(f"{idx}. {method.value}")

        choice = input("Enter choice (1/2/3/4/5/6): ").strip()

        try:
            # Map the input to the enum, using zero-based indexing (subtract 1 from the choice)
            selected_city = list(CityEnum)[int(choice) - 1]
            return selected_city.value
        except (IndexError, ValueError):
            print("Invalid choice. Please select a valid city.")
            return GymLocationView.get_city()

    @staticmethod
    def get_country():
        print("\nEnter Country ID: ")

        for idx, method in enumerate(CountryEnum, 1):
            print(f"{idx}. {method.value}")

        choice = input("Enter choice (1/2/3/4/5/6): ").strip()

        try:
            selected_country = list(CountryEnum)[int(choice) - 1]
            return selected_country.value
        except (IndexError, ValueError):
            print("Invalid choice. Please select a valid country.")
            return GymLocationView.get_country()

    @staticmethod
    def display_gym_location_added_success(gym_location):
        print(f"Gym Location {gym_location.name} added successfully!")

    @staticmethod
    def display_gym_location_list(gym_location):
        print(f"ID: {gym_location.id}, Name: {gym_location.name}, City: {gym_location.city}, Country: {gym_location.country}")

    @staticmethod
    def display_no_gym_locations_found():
        print("No gym locations found.")

    @staticmethod
    def get_gym_location_id_for_update():
        return input("Enter Gym Location ID to update: ")

    @staticmethod
    def display_gym_location_update_prompt(location):
        print(f"Updating details for {location.name}:")

    @staticmethod
    def get_new_value(current_value, prompt):
        return input(f"{prompt} (current: {current_value}): ") or current_value

    @staticmethod
    def display_gym_location_updated_success(location_id):
        print(f"Gym Location {location_id} updated successfully!")

    @staticmethod
    def display_gym_location_not_found():
        print("Gym Location not found!")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")
