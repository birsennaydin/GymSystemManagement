# views/workout_zone_view.py
class WorkoutZoneView:
    @staticmethod
    def display_workout_zone_menu():
        """
        Displays the workout zone management menu.
        """
        print("\nWorkout Zone Management Menu")
        print("1. Add Workout Zone")
        print("2. List Workout Zones")
        print("3. Update Workout Zone")
        print("4. Add Class Schedule")
        print("5. Add Promotion")
        print("6. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_workout_zone_name():
        return input("Enter Workout Zone Name: ")

    @staticmethod
    def get_zone_type():
        print("Choose Zone Type:")
        print("1. Cardio")
        print("2. Strength")
        print("3. Yoga")
        print("4. Flexibility")
        return input("Enter zone type (1/2/3/4): ")

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
        print(f"Current Name: {zone.name}")
        print(f"Current Zone Type: {zone.zone_type}")

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

    @staticmethod
    def display_gym_locations(gym_locations):
        print("Choose a Gym Location:")
        for idx, location in enumerate(gym_locations, 1):
            print(f"{idx}. {location.name} - {location.city}, {location.country}")

    @staticmethod
    def get_selected_gym_location():
        return input("Enter the number of the gym location: ")

    @staticmethod
    def display_class_schedule_menu():
        print("\nClass Schedule Management")
        print("1. Add New Class Schedule")
        print("2. View Class Schedules")
        print("3. Back to Workout Zone Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_class_schedule_details():
        class_name = input("Enter Class Name: ")
        date_time = input("Enter Class Date & Time (YYYY-MM-DD HH:MM): ")
        instructor = input("Enter Instructor Name: ")
        return class_name, date_time, instructor

    @staticmethod
    def display_class_schedule_added_success():
        print("Class schedule added successfully!")

    @staticmethod
    def display_promotion_menu():
        print("\nPromotion Management")
        print("1. Add New Promotion")
        print("2. View Promotions")
        print("3. Back to Workout Zone Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_promotion_details():
        promotion_type = input("Enter Promotion Type (e.g., Seasonal, Discount): ")
        description = input("Enter Promotion Description: ")
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")
        return promotion_type, description, start_date, end_date

    @staticmethod
    def display_promotion_added_success():
        print("Promotion added successfully!")
