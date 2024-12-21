# views/appointment_view.py
class AppointmentView:
    @staticmethod
    def display_appointment_menu():
        print("\nAppointment Management Menu")
        print("1. Add Appointment")
        print("2. List Appointments")
        print("3. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_member_id():
        return input("Enter Member ID: ")

    @staticmethod
    def get_trainer_id():
        return input("Enter Trainer ID: ")

    @staticmethod
    def get_appointment_date():
        return input("Enter Appointment Date (YYYY-MM-DD): ")

    @staticmethod
    def get_appointment_type():
        print("Choose Appointment Type:")
        print("1. Personal Training")
        print("2. Group Class")
        print("3. Consultation")
        return input("Enter choice (1/2/3): ")

    @staticmethod
    def get_status():
        print("Choose Appointment Status:")
        print("1. Scheduled")
        print("2. Completed")
        print("3. Cancelled")
        return input("Enter choice (1/2/3): ")

    @staticmethod
    def display_appointment_success(appointment):
        print(f"Appointment for Member ID {appointment.member_id} with Trainer ID {appointment.trainer_id} scheduled successfully!")

    @staticmethod
    def display_appointment_list(appointment):
        print(f"Appointment ID: {appointment.id}, Member ID: {appointment.member_id}, Trainer ID: {appointment.trainer_id}, Date: {appointment.date}, Status: {appointment.status}")

    @staticmethod
    def display_no_appointments_found():
        print("No appointments found.")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")
