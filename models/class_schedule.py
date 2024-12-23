class ClassSchedule:
    id_counter = 1
    schedules = []

    def __init__(self, workout_zone_id, class_name, date_time, instructor):
        self._id = ClassSchedule.id_counter
        self._workout_zone_id = workout_zone_id
        self._class_name = class_name
        self._date_time = date_time
        self._instructor = instructor

        ClassSchedule.id_counter += 1
        ClassSchedule.schedules.append(self)

    @property
    def id(self):
        return self._id

    @property
    def workout_zone_id(self):
        return self._workout_zone_id

    @property
    def class_name(self):
        return self._class_name

    @property
    def date_time(self):
        return self._date_time

    @property
    def instructor(self):
        return self._instructor

    @classmethod
    def get_all(cls):
        return cls.schedules

    @classmethod
    def get_by_workout_zone(cls, workout_zone_id):
        return [schedule for schedule in cls.schedules if schedule.workout_zone_id == workout_zone_id]
