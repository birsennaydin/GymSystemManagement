# views/appointment_view.py
class AppointmentView:
    @staticmethod
    def display_appointment_menu():
        print("\nAppointment Management Menu")
        print("1. Add Appointment")
        print("2. List Appointments")
        print("3. Update Appointments")
        print("4. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_member_id(members):
        print("\nSelect a Member:")
        for idx, member in enumerate(members, 1):
            print(f"{idx}. {member.name}")
        member_choice = int(input("Enter the number of the member: "))
        return members[member_choice - 1].id

    @staticmethod
    def get_appointment_id():
        return int(input("Enter appointment number: "))

    @staticmethod
    def get_trainer_id(staff):
        print("\nSelect a Trainer:")
        for idx, trainer in enumerate(staff, 1):
            print(f"{idx}. {trainer.name}")
        trainer_choice = int(input("Enter the number of the trainer: "))
        return staff[trainer_choice - 1].id

    @staticmethod
    def get_appointment_date():
        return input("Enter Appointment Date (YYYY-MM-DD HH:MM): ")

    @staticmethod
    def get_appointment_type():
        print("Choose Appointment Type:")
        print("1. Personal Training")
        print("2. Group Class")
        print("3. Consultation")
        choice = input("Enter choice (1/2/3): ").strip()

        # Map the number input to the corresponding appointment type string
        appointment_types = {
            "1": "Personal Training",
            "2": "Group Class",
            "3": "Consultation"
        }

        # Return the corresponding type, or "Unknown" if the input is invalid
        return appointment_types.get(choice, "Unknown")

    @staticmethod
    def get_status():
        print("Choose Appointment Status:")
        print("1. Scheduled")
        print("2. Completed")
        print("3. Cancelled")
        choice = input("Enter choice (1/2/3): ").strip()

        appointment_status = {
            "1": "Scheduled",
            "2": "Completed",
            "3": "Cancelled"
        }

        return appointment_status.get(choice, "Unknown")

    @staticmethod
    def display_appointment_success(appointment):
        print(f"Appointment for Member ID {appointment.member_id} with Trainer ID {appointment.trainer_id} scheduled successfully!")

    @staticmethod
    def display_appointment_list(appointment, member_name, trainer_name):
        print(
            f"Appointment ID: {appointment.id}, Member: {member_name}, Trainer: {trainer_name}, Date: {appointment.date}, Status: {appointment.status}")

    @staticmethod
    def display_no_appointments_found():
        print("No appointments found.")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")
