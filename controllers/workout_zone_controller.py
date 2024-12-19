from models.workout_zone import WorkoutZone
from views.workout_zone_view import WorkoutZoneView

class WorkoutZoneController:
    def __init__(self):
        self.zones = []

    def manage_zones(self):
        while True:
            choice = WorkoutZoneView.display_workout_zone_menu()

            if choice == "1":
                self.add_zone()
            elif choice == "2":
                self.list_zones()
            elif choice == "3":
                zone_id = WorkoutZoneView.get_zone_id_for_update()
                self.update_zone(zone_id)
            elif choice == "4":
                WorkoutZoneView.display_return_to_main_menu()
                break
            else:
                WorkoutZoneView.display_invalid_choice()

    def add_zone(self):
        WorkoutZoneView.display_workout_zone_details_prompt()
        zone_id = WorkoutZoneView.get_zone_id()
        zone_name = WorkoutZoneView.get_zone_name()
        equipment = WorkoutZoneView.get_zone_equipment()
        attendant_name = WorkoutZoneView.get_zone_attendant()

        new_zone = WorkoutZone(zone_id, zone_name, equipment, attendant_name)
        self.zones.append(new_zone)
        WorkoutZoneView.display_zone_added_success(zone_name)

    def update_zone(self, zone_id):
        zone = self.get_zone_by_id(zone_id)
        if zone:
            print(f"Updating details for {zone.get_zone_name()}:")
            zone.set_zone_name(input(f"New Zone Name (current: {zone.get_zone_name()}): ") or zone.get_zone_name())
            zone.set_equipment(input(f"New Equipment (current: {', '.join(zone.get_equipment())}): ").split(
                ',') or zone.get_equipment())
            zone.set_attendant_name(
                input(f"New Attendant Name (current: {zone.get_attendant_name()}): ") or zone.get_attendant_name())
            print(f"Workout Zone {zone_id} updated successfully!")
        else:
            print("Zone not found!")

    def get_zone_by_id(self, zone_id):
        for zone in self.zones:
            if zone.get_zone_id() == zone_id:
                return zone
        return None

    def list_zones(self):
        if not self.zones:
            print("No zones found.")
            return
        for zone in self.zones:
            print(
                f"ID: {zone.get_zone_id()}, Name: {zone.get_zone_name()}, Equipment: {', '.join(zone.get_equipment())}")