from models.appointment import Appointment

class AppointmentController:
    def __init__(self):
        self.appointments = []

    def add_appointment(self):
        print("Enter new appointment details:")
        appointment_id = int(input("Appointment ID (integer): "))
        member_id = int(input("Member ID (integer): "))
        appointment_type = input("Appointment Type (Personal Training/Group Class/Nutrition Consultation): ")
        appointment_date = input("Appointment Date (YYYY-MM-DD): ")

        new_appointment = Appointment(appointment_id, member_id, appointment_type, appointment_date)
        self.appointments.append(new_appointment)
        print(f"Appointment for member {member_id} added successfully!")

    def update_appointment(self, appointment_id):
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            print(f"Updating details for appointment {appointment.get_appointment_id()}:")
            appointment.set_appointment_type(input(f"New Appointment Type (current: {appointment.get_appointment_type()}): ") or appointment.get_appointment_type())
            appointment.set_appointment_date(input(f"New Appointment Date (current: {appointment.get_appointment_date()}): ") or appointment.get_appointment_date())
            print(f"Appointment {appointment_id} updated successfully!")
        else:
            print("Appointment not found!")

    def get_appointment_by_id(self, appointment_id):
        for appointment in self.appointments:
            if appointment.get_appointment_id() == appointment_id:
                return appointment
        return None

    def list_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return
        for appointment in self.appointments:
            print(f"ID: {appointment.get_appointment_id()}, Member ID: {appointment.get_member_id()}, Date: {appointment.get_appointment_date()}")