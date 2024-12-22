# views/gym_location_view.py
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
        return input("Enter City: ")

    @staticmethod
    def get_country():
        return input("Enter Country: ")

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
