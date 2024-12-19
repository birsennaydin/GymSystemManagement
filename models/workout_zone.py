# models/workout_zone.py

class WorkoutZone:
    id_counter = 1
    zones = []

    def __init__(self, gym_location_id, name, zone_type, attendant_id, schedule):
        self._id = WorkoutZone.id_counter
        self._gym_location_id = None
        self._name = None
        self._type = None
        self._attendant_id = None
        self._schedule = None

        self.gym_location_id = gym_location_id
        self.name = name
        self.type = zone_type
        self.attendant_id = attendant_id
        self.schedule = schedule

        WorkoutZone.id_counter += 1
        WorkoutZone.zones.append(self)

    @property
    def id(self):
        return self._id

    @property
    def gym_location_id(self):
        return self._gym_location_id

    @gym_location_id.setter
    def gym_location_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Gym Location ID must be an integer.")
        self._gym_location_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Workout zone name cannot be empty.")
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if not value:
            raise ValueError("Zone type cannot be empty.")
        self._type = value

    @property
    def attendant_id(self):
        return self._attendant_id

    @attendant_id.setter
    def attendant_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Attendant ID must be an integer.")
        self._attendant_id = value

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        if not value:
            raise ValueError("Schedule cannot be empty.")
        self._schedule = value

    @classmethod
    def get_all(cls):
        return cls.zones

    @classmethod
    def get_by_id(cls, id):
        return next((zone for zone in cls.zones if zone.id == id), None)