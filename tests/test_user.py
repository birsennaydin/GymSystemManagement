# tests/test_user.py
import unittest
from models.user import User
from models.enums import UserRole


class TestUser(unittest.TestCase):

    def setUp(self):
        """This method will run before every test."""
        # Clear the users list before each test to avoid any conflicts.
        User.users = []
        User.id_counter = 1

    def test_create_user(self):
        """Test that a user is created successfully with valid details."""
        user = User(email="testuser@example.com", password="password123", role="MEMBER")

        self.assertEqual(len(User.users), 1)  # One user should be created
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.role, UserRole.MEMBER)  # Role should be correctly assigned

    def test_duplicate_email(self):
        """Test that trying to create a user with a duplicate email raises an error."""
        User(email="testuser@example.com", password="password123", role="MEMBER")

        with self.assertRaises(ValueError):
            User(email="testuser@example.com", password="password123", role="MEMBER")

    def test_invalid_role(self):
        """Test that creating a user with an invalid role raises an error."""
        with self.assertRaises(ValueError):
            User(email="invalidrole@example.com", password="password123", role="INVALID_ROLE")

    def test_get_user_by_email(self):
        """Test that a user can be retrieved by email."""
        user = User(email="testuser@example.com", password="password123", role="MEMBER")

        found_user = User.get_by_email("testuser@example.com")
        self.assertEqual(found_user.email, "testuser@example.com")
        self.assertEqual(found_user.role, UserRole.MEMBER)

    def test_get_user_by_id(self):
        """Test that a user can be retrieved by their ID."""
        user = User(email="testuser@example.com", password="password123", role="MEMBER")

        found_user = User.get_by_id(user.id)
        self.assertEqual(found_user.email, "testuser@example.com")
        self.assertEqual(found_user.role, UserRole.MEMBER)

    def test_create_default_users(self):
        """Test that default users are created when the users list is empty."""
        User.create_default_user()

        # Check that default users are created
        self.assertEqual(len(User.users), 2)  # We expect 4 default users
        self.assertTrue(any(user.email == "manager@stmarys.com" for user in User.users))
        self.assertTrue(any(user.email == "member@stmarys.com" for user in User.users))

    def test_user_role_as_enum(self):
        """Test that the user role is correctly set as an enum."""
        user = User(email="trainer@example.com", password="password123", role=UserRole.TRAINER)

        self.assertEqual(user.role, UserRole.TRAINER)  # Ensure role is set as enum

    def test_invalid_email(self):
        """Test that a user cannot be created with an empty email."""
        with self.assertRaises(ValueError):
            User(email="", password="password123", role="MEMBER")

    def test_invalid_password(self):
        """Test that a user cannot be created with an empty password."""
        with self.assertRaises(ValueError):
            User(email="user@example.com", password="", role="MEMBER")

    def tearDown(self):
        """This method will run after every test."""
        # Reset the users list after each test to maintain isolation
        User.users = []
        User.id_counter = 1


if __name__ == '__main__':
    unittest.main()
