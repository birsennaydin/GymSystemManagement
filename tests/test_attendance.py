import unittest
from models.attendance import Attendance
from models.member import Member
from models.class_schedule import ClassSchedule
from models.enums import AttendanceStatusEnum


class TestAttendance(unittest.TestCase):

    def setUp(self):
        """This method will run before every test."""
        # Clear the attendance records list before each test to avoid any conflicts.
        Attendance.records = []
        Attendance.id_counter = 1
        Member.members = []
        ClassSchedule.schedules = []

    def test_create_attendance(self):
        """Test that an attendance record is created successfully with valid details."""
        member = Member(
            name="Birsen",
            email="birsen@example.com",
            phone="1234567890",
            membership_type="Regular",
            health_info="Healthy",
            status="Active",
            gym_location_id=1,
            user_id=101
        )
        class_schedule = ClassSchedule(
            workout_zone_id=1,
            class_name="Yoga Class",
            date_time="2025-01-10 09:00",
            instructor="Jane Trainer"
        )

        attendance = Attendance(
            member_id=member.id,
            class_id=class_schedule.id,
            attendance_date="2025-01-10 09:00",
            status=AttendanceStatusEnum.PRESENT.value
        )

        self.assertEqual(len(Attendance.records), 1)  # One attendance record should be created
        self.assertEqual(attendance.member_id, member.id)
        self.assertEqual(attendance.class_id, class_schedule.id)
        self.assertEqual(attendance.status, AttendanceStatusEnum.PRESENT.value)

    def test_invalid_attendance_status(self):
        """Test that creating an attendance record with an invalid status raises a ValueError."""
        member = Member(
            name="Birsen",
            email="birsen@example.com",
            phone="9876543210",
            membership_type="Premium",
            health_info="Normal",
            status="Active",
            gym_location_id=1,
            user_id=102
        )
        class_schedule = ClassSchedule(
            workout_zone_id=1,
            class_name="Strength Class",
            date_time="2025-01-11 10:00",
            instructor="Bob Trainer"
        )

        with self.assertRaises(ValueError):
            attendance = Attendance(
                member_id=member.id,
                class_id=class_schedule.id,
                attendance_date="2025-01-11 10:00",
                status="InvalidStatus"  # Invalid status
            )

    def test_get_attendance_by_id(self):
        """Test that an attendance record can be retrieved by its ID."""
        member = Member(
            name="Birsen",
            email="birsen@example.com",
            phone="1234567890",
            membership_type="Premium",
            health_info="Healthy",
            status="Active",
            gym_location_id=1,
            user_id=103
        )
        class_schedule = ClassSchedule(
            workout_zone_id=1,
            class_name="Yoga Class",
            date_time="2025-01-12 11:00",
            instructor="Sarah Trainer"
        )

        attendance = Attendance(
            member_id=member.id,
            class_id=class_schedule.id,
            attendance_date="2025-01-12 11:00",
            status=AttendanceStatusEnum.PRESENT.value
        )

        found_attendance = Attendance.get_by_id(attendance.id)
        self.assertEqual(found_attendance.id, attendance.id)
        self.assertEqual(found_attendance.member_id, member.id)

    def test_get_all_attendance_records(self):
        """Test that all attendance records can be retrieved."""
        member = Member(
            name="Melis",
            email="melis@example.com",
            phone="9876543210",
            membership_type="Regular",
            health_info="Normal",
            status="Active",
            gym_location_id=2,
            user_id=104
        )
        class_schedule = ClassSchedule(
            workout_zone_id=2,
            class_name="Strength Class",
            date_time="2025-01-13 12:00",
            instructor="Mike Trainer"
        )

        attendance1 = Attendance(
            member_id=member.id,
            class_id=class_schedule.id,
            attendance_date="2025-01-13 12:00",
            status=AttendanceStatusEnum.PRESENT.value
        )
        attendance2 = Attendance(
            member_id=member.id,
            class_id=class_schedule.id,
            attendance_date="2025-01-14 13:00",
            status=AttendanceStatusEnum.ABSENT.value
        )

        records = Attendance.get_all()
        self.assertEqual(len(records), 2)

    def test_invalid_member_id(self):
        """Test that creating an attendance record with an invalid member ID raises a ValueError."""
        with self.assertRaises(ValueError):
            attendance = Attendance(
                member_id="invalid_member_id",  # Invalid member ID type
                class_id=1,
                attendance_date="2025-01-10 09:00",
                status=AttendanceStatusEnum.PRESENT.value
            )

    def test_invalid_class_id(self):
        """Test that creating an attendance record with an invalid class ID raises a ValueError."""
        with self.assertRaises(ValueError):
            attendance = Attendance(
                member_id=1,
                class_id="invalid_class_id",  # Invalid class ID type
                attendance_date="2025-01-10 09:00",
                status=AttendanceStatusEnum.PRESENT.value
            )

    def tearDown(self):
        """This method will run after every test."""
        # Reset the attendance records and other related lists after each test to maintain isolation
        Attendance.records = []
        Attendance.id_counter = 1
        Member.members = []
        ClassSchedule.schedules = []


if __name__ == '__main__':
    unittest.main()
