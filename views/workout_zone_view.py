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
        """
        Displays the available zone types and prompts the user to select one.
        """
        print("Choose Zone Type:")
        print("1. Cardio")
        print("2. Strength")
        print("3. Yoga")
        print("4. Flexibility")
        choice = input("Enter zone type (1/2/3/4): ").strip()
        zone_types = {
            "1": "Cardio",
            "2": "Strength",
            "3": "Yoga",
            "4": "Flexibility"
        }
        return zone_types.get(choice, "Unknown")

    @staticmethod
    def display_workout_zone_added_success(zone):
        print(f"Workout Zone {zone.name}, Zone type: {zone.zone_type} added successfully!")

    @staticmethod
    def display_workout_zone_list(zone):
        print(f"ID: {zone.id}, Name: {zone.name}, Zone Type: {zone.get_zone_type_name()}, Gym Location: {zone.get_gym_location_name()}")

    @staticmethod
    def display_no_workout_zones_found():
        print("No workout zones found.")

    @staticmethod
    def get_workout_zone_id_for_update():
        return input("Enter Workout Zone ID to update: ")

    @staticmethod
    def get_workout_staff_id_for_update():
        return input("Select Staff ID for the attendant: ")

    @staticmethod
    def display_workout_zone_update_prompt(zone):
        """
        Displays the current details of a workout zone to be updated.
        """
        print(f"Updating details for {zone.name}:")
        print(f"Current Name: {zone.name}")
        print(f"Current Zone Type: {zone.get_zone_type_name()}")

    @staticmethod
    def get_new_value(current_value, prompt):
        """
        Prompts the user to update a value and returns the new value, or the current value if no update.
        """
        new_value = input(f"{prompt} (current: {current_value}): ").strip()
        return new_value if new_value else current_value

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
    def display_staff_list(staff_list):
        """
        Displays the list of staff members.
        """
        if not staff_list:
            print("No staff members to display.")
        else:
            for staff in staff_list:
                print(
                    f"ID: {staff.get_staff_id()}, Name: {staff.get_name()}, Role: {staff.get_role().name}, Email: {staff.email}, Phone: {staff.phone}")

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
