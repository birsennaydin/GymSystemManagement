# views/workout_zone_view.py
class WorkoutZoneView:
    @staticmethod
    def display_workout_zone_menu():
        print("\nWorkout Zone Management Menu")
        print("1. Add Workout Zone")
        print("2. List Workout Zones")
        print("3. Update Workout Zone")
        print("4. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_workout_zone_name():
        return input("Enter Workout Zone Name: ")

    @staticmethod
    def get_zone_type():
        return input("Enter Zone Type: ")

    @staticmethod
    def display_workout_zone_added_success(zone):
        print(f"Workout Zone {zone.name} added successfully!")

    @staticmethod
    def display_workout_zone_list(zone):
        print(f"ID: {zone.id}, Name: {zone.name}, Zone Type: {zone.zone_type}, Gym Location ID: {zone.gym_location_id}")

    @staticmethod
    def display_no_workout_zones_found():
        print("No workout zones found.")

    @staticmethod
    def get_workout_zone_id_for_update():
        return input("Enter Workout Zone ID to update: ")

    @staticmethod
    def display_workout_zone_update_prompt(zone):
        print(f"Updating details for {zone.name}:")

    @staticmethod
    def get_new_value(current_value, prompt):
        return input(f"{prompt} (current: {current_value}): ") or current_value

    @staticmethod
    def display_workout_zone_updated_success(zone_id):
        print(f"Workout Zone {zone_id} updated successfully!")

    @staticmethod
    def display_workout_zone_not_found():
        print("Workout Zone not found!")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")
