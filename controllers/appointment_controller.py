# controllers/appointment_controller.py
from models.appointment import Appointment
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
                AppointmentView.display_return_to_main_menu()
                return AuthController.display_menu_based_on_role(user)
            else:
                AppointmentView.display_invalid_choice()

    @staticmethod
    def add_appointment():
        member_id = AppointmentView.get_member_id()
        trainer_id = AppointmentView.get_trainer_id()
        appointment_date = AppointmentView.get_appointment_date()
        appointment_type = AppointmentView.get_appointment_type()
        status = AppointmentView.get_status()

        appointment = Appointment(member_id=member_id, trainer_id=trainer_id, date=appointment_date, type=appointment_type, status=status)
        AppointmentView.display_appointment_success(appointment)

    @staticmethod
    def list_appointments():
        appointments = Appointment.get_all()
        if not appointments:
            AppointmentView.display_no_appointments_found()
        else:
            for appointment in appointments:
                AppointmentView.display_appointment_list(appointment)
