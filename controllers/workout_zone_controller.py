# controllers/workout_zone_controller.py
from models.workout_zone import WorkoutZone
from views.workout_zone_view import WorkoutZoneView

class WorkoutZoneController:
    @staticmethod
    def manage_zones():
        while True:
            choice = WorkoutZoneView.display_workout_zone_menu()

            if choice == "1":
                WorkoutZoneController.add_workout_zone()
            elif choice == "2":
                WorkoutZoneController.list_workout_zones()
            elif choice == "3":
                WorkoutZoneController.update_workout_zone()
            elif choice == "4":
                WorkoutZoneView.display_return_to_main_menu()
                break
            else:
                WorkoutZoneView.display_invalid_choice()

    @staticmethod
    def add_workout_zone():
        name = WorkoutZoneView.get_workout_zone_name()
        zone_type = WorkoutZoneView.get_zone_type()
        gym_location = WorkoutZoneView.get_gym_location()

        workout_zone = WorkoutZone(name=name, zone_type=zone_type, gym_location_id=gym_location)
        WorkoutZoneView.display_workout_zone_added_success(workout_zone)

    @staticmethod
    def list_workout_zones():
        zones = WorkoutZone.get_all()
        if not zones:
            WorkoutZoneView.display_no_workout_zones_found()
        else:
            for zone in zones:
                WorkoutZoneView.display_workout_zone_list(zone)

    @staticmethod
    def update_workout_zone():
        zone_id = WorkoutZoneView.get_workout_zone_id_for_update()
        zone = WorkoutZone.get_by_id(zone_id)

        if not zone:
            WorkoutZoneView.display_workout_zone_not_found()
        else:
            WorkoutZoneView.display_workout_zone_update_prompt(zone)
            name = WorkoutZoneView.get_new_value(zone.name, "Name")
            zone_type = WorkoutZoneView.get_new_value(zone.zone_type, "Zone Type")

            zone.name = name
            zone.zone_type = zone_type
            WorkoutZoneView.display_workout_zone_updated_success(zone.id)
