class WorkoutZone:
    def __init__(self, zone_id, zone_name, equipment, attendant_name):
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.equipment = equipment
        self.attendant_name = attendant_name

    # Getters and Setters
    def get_zone_id(self):
        return self.zone_id

    def set_zone_id(self, zone_id):
        self.zone_id = zone_id

    def get_zone_name(self):
        return self.zone_name

    def set_zone_name(self, zone_name):
        self.zone_name = zone_name

    def get_equipment(self):
        return self.equipment

    def set_equipment(self, equipment):
        self.equipment = equipment

    def get_attendant_name(self):
        return self.attendant_name

    def set_attendant_name(self, attendant_name):
        self.attendant_name = attendant_name
