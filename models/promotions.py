class Promotion:
    id_counter = 1
    promotions = []

    def __init__(self, workout_zone_id, promotion_type, description, start_date, end_date):
        self._id = Promotion.id_counter
        self._workout_zone_id = workout_zone_id
        self._promotion_type = promotion_type
        self._description = description
        self._start_date = start_date
        self._end_date = end_date

        Promotion.id_counter += 1
        Promotion.promotions.append(self)

    @property
    def id(self):
        return self._id

    @property
    def workout_zone_id(self):
        return self._workout_zone_id

    @property
    def promotion_type(self):
        return self._promotion_type

    @property
    def description(self):
        return self._description

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @classmethod
    def get_all(cls):
        return cls.promotions

    @classmethod
    def get_by_workout_zone(cls, workout_zone_id):
        return [promo for promo in cls.promotions if promo.workout_zone_id == workout_zone_id]
