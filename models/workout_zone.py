from models.gym_location import GymLocation
from models.staff import Staff
from models.promotions import Promotion
from models.class_schedule import ClassSchedule  # Assuming we create this model later

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
