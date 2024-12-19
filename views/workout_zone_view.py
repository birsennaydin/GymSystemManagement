class WorkoutZoneView:
    @staticmethod
    def display_workout_zone_menu():
        print("\nWorkout Zone Management Menu")
        print("1. Add Zone")
        print("2. List Zones")
        print("3. Update Zone")
        print("4. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def display_workout_zone_details_prompt():
        print("Enter new workout zone details:")

    @staticmethod
    def get_zone_id():
        return int(input("Zone ID (integer): "))

    @staticmethod
    def get_zone_name():
        return input("Zone Name (string): ")

    @staticmethod
    def get_zone_equipment():
        return input("Equipment available (comma separated): ").split(',')

    @staticmethod
    def get_zone_attendant():
        return input("Attendant Name (string): ")

    @staticmethod
    def display_zone_added_success(name):
        print(f"Zone {name} added successfully!")

    @staticmethod
    def get_zone_id_for_update():
        return int(input("Enter Zone ID to update: "))

    @staticmethod
    def display_zone_name_update_prompt(zone):
        print(f"Updating details for {zone.get_name()}:")

    @staticmethod
    def get_new_value(current_value, prompt):
        new_value = input(f"{prompt} (current: {current_value}): ")
        return new_value or current_value

    @staticmethod
    def display_zone_updated_success(zone_id):
        print(f"Zone {zone_id} updated successfully!")

    @staticmethod
    def display_no_zones_found():
        print("No workout zones found.")

    @staticmethod
    def display_workout_zone_list(zones):
        print(
            f"ID: {zones.get_zone_id()}, Name: {zones.get_name()}, "
            f"Equipment: {zones.get_equipment_type().value}, Attendat: {zones.get_zones_attendant()}"
        )

    @staticmethod
    def display_membership_type_prompt():
        print("Choose Membership Type:")
        print("1. Regular")
        print("2. Premium")
        print("3. Trial")
        return input("Enter choice (1/2/3): ")

    @staticmethod
    def display_membership_type_invalid():
        print("Invalid choice. Defaulting to Regular.")

    @staticmethod
    def display_zones_not_found():
        print("Zones not found!")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")

    @staticmethod
    def get_health_info():
        return input("Enter Health Info: ")
