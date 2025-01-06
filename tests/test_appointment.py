import unittest
from models.appointment import Appointment
from models.enums import MembershipType, StaffRole
from models.member import Member
from models.staff import Staff
from views.appointment_view import AppointmentView


class TestAppointment(unittest.TestCase):

    def setUp(self):
        """This method will run before every test."""
        # Clear the appointments list before each test to avoid any conflicts.
        Appointment.appointments = []
        Appointment.id_counter = 1
        Member.members = []
        Staff.staff = []

    def test_create_appointment(self):
        """Test that an appointment is created successfully with valid details."""
        # Create a member and a trainer for the appointment
        member = Member(
            name="Birsen",
            email="birsen@example.com",
            phone="1234567890",
            membership_type=MembershipType.REGULAR,
            health_info="Healthy",
            status="Active",
            gym_location_id=1,
            user_id=101
        )

        trainer = Staff(name="Melis", role=StaffRole["TRAINER"] ,email="trainer@example.com", phone="1234567890", gym_location_id=1)

        # Create an appointment
        appointment = Appointment(
            member_id=member.id,
            trainer_id=trainer.id,
            date="2025-01-10 09:00",
            appointment_type="Personal Training",
            status="Scheduled"
        )

        self.assertEqual(len(Appointment.appointments), 1)  # One appointment should be created
        self.assertEqual(appointment.member_id, member.id)
        self.assertEqual(appointment.trainer_id, trainer.id)
        self.assertEqual(appointment.date, "2025-01-10 09:00")
        self.assertEqual(appointment.appointment_type, "Personal Training")
        self.assertEqual(appointment.status, "Scheduled")

    def test_invalid_appointment_type(self):
        """Test that creating an appointment with an invalid type raises a ValueError."""
        with self.assertRaises(ValueError):
            appointment = Appointment(
                member_id=1,
                trainer_id=1,
                date="2025-01-10 09:00",
                appointment_type="Invalid Type",  # Invalid appointment type
                status="Scheduled"
            )

    def test_invalid_appointment_status(self):
        """Test that creating an appointment with an invalid status raises a ValueError."""
        with self.assertRaises(ValueError):
            appointment = Appointment(
                member_id=1,
                trainer_id=1,
                date="2025-01-10 09:00",
                appointment_type="Personal Training",
                status="Invalid Status"  # Invalid appointment status
            )

    def test_get_all_appointments(self):
        """Test that the get_all method returns all appointments."""
        member = Member(
            name="Birsen",
            email="birsen@example.com",
            phone="9876543210",
            membership_type=MembershipType.REGULAR,
            health_info="Normal",
            status="Active",
            gym_location_id=2,
            user_id=102
        )

        trainer = Staff(name="Melis", role=StaffRole["TRAINER"], email="melis@example.com", phone="1234567890",
                        gym_location_id=1)

        Appointment(
            member_id=member.id,
            trainer_id=trainer.id,
            date="2025-01-10 09:00",
            appointment_type="Personal Training",
            status="Scheduled"
        )
        Appointment(
            member_id=member.id,
            trainer_id=trainer.id,
            date="2025-01-11 10:00",
            appointment_type="Group Class",
            status="Completed"
        )

        appointments = Appointment.get_all()
        self.assertEqual(len(appointments), 2)
        self.assertEqual(appointments[0].date, "2025-01-10 09:00")
        self.assertEqual(appointments[1].date, "2025-01-11 10:00")

    def test_get_appointment_by_id(self):
        """Test that an appointment can be retrieved by its ID."""
        member = Member(
            name="Birsen",
            email="birsen@example.com",
            phone="1234567890",
            membership_type=MembershipType.REGULAR,
            health_info="Healthy",
            status="Active",
            gym_location_id=1,
            user_id=101
        )

        trainer = Staff(name="Melis", role=StaffRole["TRAINER"], email="melis@example.com", phone="1234567890",
                        gym_location_id=1)

        appointment = Appointment(
            member_id=member.id,
            trainer_id=trainer.id,
            date="2025-01-10 09:00",
            appointment_type="Personal Training",
            status="Scheduled"
        )

        found_appointment = Appointment.get_by_id(appointment.id)
        self.assertEqual(found_appointment.id, appointment.id)
        self.assertEqual(found_appointment.member_id, member.id)

    def test_invalid_member_id(self):
        """Test that creating an appointment with an invalid member ID raises a ValueError."""
        with self.assertRaises(ValueError):
            appointment = Appointment(
                member_id="invalid_member_id",  # Invalid member ID type
                trainer_id=1,
                date="2025-01-10 09:00",
                appointment_type="Personal Training",
                status="Scheduled"
            )

    def tearDown(self):
        """This method will run after every test."""
        # Reset the appointments and other related lists after each test to maintain isolation
        Appointment.appointments = []
        Appointment.id_counter = 1
        Member.members = []
        Staff.staff = []


if __name__ == '__main__':
    unittest.main()
