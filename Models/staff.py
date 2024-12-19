from Models.enums import StaffRole

class Staff:
    def __init__(self, staff_id, name, role: StaffRole):
        self.staff_id = staff_id
        self.name = name
        self.role = role

    # Getters and Setters
    def get_staff_id(self):
        return self.staff_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_role(self):
        return self.role

    def set_role(self, role: StaffRole):
        if isinstance(role, StaffRole):
            self.role = role
        else:
            raise ValueError("Invalid staff role")