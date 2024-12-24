# controllers/appointment_controller.py
from models.appointment import Appointment
from models.member import Member
from models.staff import Staff
from views.appointment_view import AppointmentView

class AppointmentController:
    @staticmethod
    def manage_appointments(user):
        from controllers.auth_controller import AuthController
        while True:
            choice = AppointmentView.display_appointment_menu()

            if choice == "1":
                AppointmentController.add_appointment()
            elif choice == "2":
                AppointmentController.list_appointments()
            elif choice == "3":
                AppointmentController.update_appointment()
            elif choice == "4":
                AppointmentView.display_return_to_main_menu()
                return AuthController.display_menu_based_on_role(user)
            else:
                AppointmentView.display_invalid_choice()

    @staticmethod
    def add_appointment():
        # Fetch all members and staff (trainers)
        members = Member.get_all()  # Assuming you have a method to fetch all members
        if not members:
            print("Error: No members found. Unable to add appointment.")
            return

        staff = Staff.get_by_role("TRAINER")  # Assuming you have a method to fetch staff with role 'TRAINER'
        if not staff:
            print("Error: No trainer staff found. Unable to add appointment.")
            return

        # Display member and trainer lists and get IDs
        member_id = AppointmentView.get_member_id(members)  # Select member from the list
        trainer_id = AppointmentView.get_trainer_id(staff)  # Select trainer from the list

        # Get appointment details from the user
        appointment_date = AppointmentView.get_appointment_date()
        appointment_type = AppointmentView.get_appointment_type()
        status = AppointmentView.get_status()

        # Create the new appointment
        appointment = Appointment(member_id=member_id, trainer_id=trainer_id, date=appointment_date,
                                  appointment_type=appointment_type, status=status)
        AppointmentView.display_appointment_success(appointment)

    @staticmethod
    def list_appointments():
        appointments = Appointment.get_all()
        if not appointments:
            AppointmentView.display_no_appointments_found()
        else:
            for appointment in appointments:
                # Fetch the Member and Trainer details based on their IDs
                member = Member.get_by_id(appointment.member_id)
                trainer = Staff.get_by_id(appointment.trainer_id)

                # Pass the member and trainer names to the display function
                AppointmentView.display_appointment_list(appointment, member.name, trainer.name)

    @staticmethod
    def update_appointment():
        """
        Updates an existing appointment.
        Allows the user to modify the appointment details.
        """
        AppointmentController.list_appointments()

        # List all appointments and get the appointment ID to update
        appointment_id = AppointmentView.get_appointment_id()

        appointment = Appointment.get_by_id(appointment_id)
        if not appointment:
            print("Appointment not found.")
            return

        # Update fields: date, trainer, status
        updated_date = AppointmentView.get_appointment_date() or appointment.date
        updated_trainer_id = AppointmentView.get_trainer_id(Staff.get_by_role("TRAINER")) or appointment.trainer_id
        updated_status = AppointmentView.get_status() or appointment.status

        # Update the appointment with new values
        appointment.date = updated_date
        appointment.trainer_id = updated_trainer_id
        appointment.status = updated_status

        print(f"Appointment {appointment.id} updated successfully.")
        AppointmentView.display_appointment_success(appointment)
