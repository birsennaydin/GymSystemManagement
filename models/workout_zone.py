from models.gym_location import GymLocation
from models.staff import Staff
from models.promotions import Promotion
from models.class_schedule import ClassSchedule  # Assuming we create this model later
from views.workout_zone_view import WorkoutZoneView


class WorkoutZone:
    id_counter = 1
    zones = []

    def __init__(self, name, zone_type, gym_location_id, staff_id, schedule=None, promotions=None):
        self._id = WorkoutZone.id_counter
        self._name = name
        self._zone_type = zone_type
        self._gym_location_id = gym_location_id
        self._staff_id = staff_id
        self._schedule = schedule if schedule is not None else []  # Schedule for classes in this zone
        self._promotions = promotions if promotions is not None else []  # Promotions for this zone

        WorkoutZone.id_counter += 1
        WorkoutZone.zones.append(self)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def zone_type(self):
        return self._zone_type

    @property
    def gym_location_id(self):
        return self._gym_location_id

    @property
    def staff_id(self):
        return self._staff_id

    @property
    def schedule(self):
        return self._schedule

    @property
    def promotions(self):
        return self._promotions

    @classmethod
    def get_all(cls):
        return cls.zones

    @classmethod
    def get_by_id(cls, id):
        return next((zone for zone in cls.zones if zone.id == id), None)

    @classmethod
    def get_by_gym_location(cls, gym_location_id):
        return [zone for zone in cls.zones if zone.gym_location_id == gym_location_id]

    @classmethod
    def get_by_zone_type(cls, zone_type):
        return [zone for zone in cls.zones if zone.zone_type == zone_type]

    @zone_type.setter
    def zone_type(self, value):
        """
        Setter for the zone_type property.
        Ensures the zone type is one of the valid options.
        """
        print(f"Zonetype setter: {value}")
        valid_zone_types = ['Cardio', 'Strength', 'Yoga', 'Flexibility']
        if value not in valid_zone_types:
            raise ValueError(f"Invalid zone type. Please choose from {', '.join(valid_zone_types)}.")
        self._zone_type = value

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value

    def get_zone_type_name(self):
        zone_types = {
            "Cardio": "Cardio",
            "Strength": "Strength",
            "Yoga": "Yoga",
            "Flexibility": "Flexibility"
        }
        print(f"Zone Type 76: {self.zone_type}")
        return zone_types.get(str(self.zone_type), "Unknown")

    def get_gym_location_name(self):
        gym_location = GymLocation.get_by_id(self.gym_location_id)
        return gym_location.name if gym_location else "Unknown"

    @staticmethod
    def list_workout_zones():
        """
        Lists all workout zones in the system with more meaningful information.
        """
        zones = WorkoutZone.get_all()
        if zones:
            for zone in zones:
                # Display workout zone with names instead of raw IDs
                print(
                    f"ID: {zone.id}, Name: {zone.name}, Zone Type: {zone.get_zone_type_name()}, Gym Location: {zone.get_gym_location_name()}")
        else:
            WorkoutZoneView.display_no_workout_zones_found()