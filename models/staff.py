from models.enums import UserRole

class Staff:
    id_counter = 1
    staff_members = []

    def __init__(self, name, role, email, phone, gym_location_id):
        self._id = Staff.id_counter
        self._name = None
        self._role = None
        self._email = None
        self._phone = None
        self._gym_location_id = None

        self.name = name
        self.role = role  # Role burada "Admin", "Trainer", "Attendant", "Member" olabilir
        self.email = email
        self.phone = phone
        self.gym_location_id = gym_location_id

        Staff.id_counter += 1
        Staff.staff_members.append(self)

    @property
    def id(self):
        return self._id

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        print(f"Staff Role detail: {value}")
        if value not in ['MANAGER', 'TRAINER', 'ATTENDANT']:
            raise ValueError("Invalid role. Please choose from Admin, Trainer, Attendant.")
        self._role = value

    @classmethod
    def get_all(cls):
        return cls.staff_members

    @classmethod
    def get_by_id(cls, id):
        return next((staff for staff in cls.staff_members if staff.id == id), None)
