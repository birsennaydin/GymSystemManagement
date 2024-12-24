# controllers/workout_zone_controller.py
from views.workout_zone_view import WorkoutZoneView
from models.workout_zone import WorkoutZone
from models.gym_location import GymLocation
from models.staff import Staff
from models.class_schedule import ClassSchedule
from models.promotions import Promotion

class WorkoutZoneController:
    @staticmethod
    def manage_workout_zones(user):
        from controllers.auth_controller import AuthController
        while True:
            choice = WorkoutZoneView.display_workout_zone_menu()

            if choice == "1":  # Add Workout Zone
                WorkoutZoneController.add_workout_zone()
            elif choice == "2":  # List Workout Zones
                WorkoutZoneController.list_workout_zones()
            elif choice == "3":  # Update Workout Zone
                WorkoutZoneController.update_workout_zone()
            elif choice == "4":  # Add Class Schedule
                WorkoutZoneController.add_class_schedule()
            elif choice == "5":  # Add Promotion
                WorkoutZoneController.add_promotion()
            elif choice == "6":  # Back to Main Menu
                WorkoutZoneView.display_return_to_main_menu()
                return AuthController.display_menu_based_on_role(user)
            else:
                WorkoutZoneView.display_invalid_choice()

    @staticmethod
    def add_workout_zone():
        """
        Adds a new workout zone to the system.
        """
        name = WorkoutZoneView.get_workout_zone_name()
        zone_type = WorkoutZoneView.get_zone_type()
        print(f"Save zone type: {zone_type}")
        # Get available gym locations
        gym_locations = GymLocation.get_all()
        WorkoutZoneView.display_gym_locations(gym_locations)

        selected_location_idx = int(WorkoutZoneView.get_selected_gym_location()) - 1
        if selected_location_idx < 0 or selected_location_idx >= len(gym_locations):
            print("Invalid selection. Returning to menu...")
            return

        gym_location = gym_locations[selected_location_idx]
        gym_location_id = gym_location.id  # Use the selected gym location's ID

        # Get available staff with TRAINER role only
        staff = Staff.get_by_role("TRAINER")
        if not staff:
            print("Error: No staff with TRAINER role available. Please ensure staff are assigned to this location.")
            return  # Return early if no trainer staff are available

        # List the staff with their details
        staff_details = [(s.id, s.name, GymLocation.get_by_id(s.gym_location_id).name) for s in staff]
        for staff_id, staff_name, gym_location in staff_details:
            print(f"ID: {staff_id}, Name: {staff_name}, Gym Location: {gym_location}")

        staff_id = int(input("Select Staff ID for the attendant: "))

        # Create the new workout zone
        new_zone = WorkoutZone(
            name=name,
            zone_type=zone_type,
            gym_location_id=gym_location_id,
            staff_id=staff_id
        )

        WorkoutZoneView.display_workout_zone_added_success(new_zone)

    @staticmethod
    def list_workout_zones():
        """
        Lists all workout zones in the system.
        """
        zones = WorkoutZone.get_all()
        if zones:
            for zone in zones:
                WorkoutZoneView.display_workout_zone_list(zone)
        else:
            WorkoutZoneView.display_no_workout_zones_found()

    @staticmethod
    def update_workout_zone():
        """
        Updates an existing workout zone.
        """
        print("\nSelect a workout zone to update:")
        WorkoutZoneController.list_workout_zones()  # List available workout zones
        zone_id = WorkoutZoneView.get_workout_zone_id_for_update()  # Ask for zone ID
        zone = WorkoutZone.get_by_id(int(zone_id))  # Fetch the selected zone

        if zone:
            WorkoutZoneView.display_workout_zone_update_prompt(zone)

            # Get updated zone type with proper mapping
            zone_type = WorkoutZoneView.get_zone_type()  # Fetch zone type using the updated method

            # Ensure zone_type is valid before assignment
            if zone_type not in ['Cardio', 'Strength', 'Yoga', 'Flexibility']:
                print(
                    f"Invalid zone type: {zone_type}. Zone type must be one of 'Cardio', 'Strength', 'Yoga', 'Flexibility'.")
                return  # Exit if invalid zone type

            # Get available staff with TRAINER role only
            staff = Staff.get_by_role("TRAINER")
            if not staff:
                print("Error: No staff with TRAINER role available. Please ensure staff are assigned to this location.")
                return  # Return early if no trainer staff are available

            # List the staff with their details
            staff_details = [(s.id, s.name, GymLocation.get_by_id(s.gym_location_id).name) for s in staff]
            for staff_id, staff_name, gym_location in staff_details:
                print(f"ID: {staff_id}, Name: {staff_name}, Gym Location: {gym_location}")

            staff_id = WorkoutZoneView.get_workout_staff_id_for_update()

            # Update the workout zone details
            zone.zone_type = zone_type  # Update the zone type
            zone.staff_id = staff_id

            WorkoutZoneView.display_workout_zone_updated_success(zone.id)  # Display success message
        else:
            WorkoutZoneView.display_workout_zone_not_found()

    @staticmethod
    def add_class_schedule():
        """
        Adds a class schedule to a workout zone.
        """
        # List all workout zones by name
        workout_zones = WorkoutZone.get_all()
        if workout_zones:
            print("Select a Workout Zone by Name:")
            for idx, zone in enumerate(workout_zones, 1):
                print(f"{idx}. {zone.name}")
            selected_zone_idx = int(input("Enter the number of the zone: ")) - 1

            if selected_zone_idx < 0 or selected_zone_idx >= len(workout_zones):
                print("Invalid selection. Returning to menu...")
                return

            selected_zone = workout_zones[selected_zone_idx]

            class_name, date_time, instructor = WorkoutZoneView.get_class_schedule_details()

            # Create the new class schedule
            new_schedule = ClassSchedule(
                workout_zone_id=selected_zone.id,
                class_name=class_name,
                date_time=date_time,
                instructor=instructor
            )

            WorkoutZoneView.display_class_schedule_added_success()
        else:
            print("No workout zones found.")

    @staticmethod
    def add_promotion():
        """
        Adds a promotion to a workout zone.
        """
        # List all workout zones by name
        workout_zones = WorkoutZone.get_all()
        if workout_zones:
            print("Select a Workout Zone by Name:")
            for idx, zone in enumerate(workout_zones, 1):
                print(f"{idx}. {zone.name}")
            selected_zone_idx = int(input("Enter the number of the zone: ")) - 1

            if selected_zone_idx < 0 or selected_zone_idx >= len(workout_zones):
                print("Invalid selection. Returning to menu...")
                return

            selected_zone = workout_zones[selected_zone_idx]

            promotion_type, description, start_date, end_date = WorkoutZoneView.get_promotion_details()

            # Create the new promotion
            new_promotion = Promotion(
                workout_zone_id=selected_zone.id,
                promotion_type=promotion_type,
                description=description,
                start_date=start_date,
                end_date=end_date
            )

            WorkoutZoneView.display_promotion_added_success()
        else:
            print("No workout zones found.")
