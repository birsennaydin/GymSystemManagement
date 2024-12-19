class GymLocationView:
    @staticmethod
    def display_gym_location_menu():
        print("\nGym Location Management:")
        print("1. Add a new gym location")
        print("2. List all gym locations")
        print("3. Select a gym location")
        print("4. Return to main menu")

        return input("Enter your choice: ").strip()

    @staticmethod
    def get_new_location_input():
        try:
            location_id = int(input("Enter location ID: "))
            location_name = input("Enter location name: ")
            print("Available cities: [London, Manchester, Birmingham]")
            city = input("Enter city: ").strip()
            print("Available countries: [UK, USA, Canada]")
            country = input("Enter country: ").strip()
            return location_id, location_name, city, country
        except ValueError as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def display_locations(locations):
        if not locations:
            print("No gym locations available.")
            return

        print("Available Gym Locations:")
        for location in locations:
            print(
                f"ID: {location.get_location_id()}, "
                f"Name: {location.get_location_name()}, "
                f"City: {location.get_city().value}, "
                f"Country: {location.get_country().value}"
            )

    @staticmethod
    def select_location():
        try:
            return int(input("Enter the ID of the location you want to select: "))
        except ValueError:
            print("Invalid input. Please enter a valid location ID.")
            return None
