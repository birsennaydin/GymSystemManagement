from Models.staff import Staff
from Models.enums import StaffRole


class StaffController:
    def __init__(self):
        self.staff_list = []

    def add_staff(self):
        name = input("Enter staff name: ")
        role_input = input("Enter staff role (e.g., Trainer, Manager, Assistant): ")

        try:
            role = StaffRole[role_input.capitalize()]
        except KeyError:
            print(
                f"Invalid role: {role_input}. Please choose from the following: {', '.join([role.name for role in StaffRole])}")
            return

        staff_id = len(self.staff_list) + 1
        new_staff = Staff(staff_id, name, role)
        self.staff_list.append(new_staff)
        print(f"Staff {name} added successfully with ID {staff_id} and role {role.name}.")

    def update_staff(self):
        staff_id = int(input("Enter the staff ID to update: "))
        staff = self.get_staff_by_id(staff_id)

        if staff:
            name = input(f"Enter new name (current: {staff.get_name()}): ") or staff.get_name()
            role_input = input(f"Enter new role (current: {staff.get_role().name}): ") or staff.get_role().name

            try:
                role = StaffRole[role_input.capitalize()]
            except KeyError:
                print(
                    f"Invalid role: {role_input}. Please choose from the following: {', '.join([role.name for role in StaffRole])}")
                return

            staff.set_name(name)
            staff.set_role(role)
            print(f"Staff {staff_id} updated to {name} with role {role.name}.")
        else:
            print(f"Staff with ID {staff_id} not found.")

    def list_staff(self):
        if not self.staff_list:
            print("No staff members found.")
        else:
            for staff in self.staff_list:
                print(f"ID: {staff.get_staff_id()}, Name: {staff.get_name()}, Role: {staff.get_role().name}")

    def get_staff_by_id(self, staff_id):
        for staff in self.staff_list:
            if staff.get_staff_id() == staff_id:
                return staff
        return None
