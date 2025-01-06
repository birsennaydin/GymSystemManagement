# main.py
from gym_system import GymSystem
from models.member import Member
from models.staff import Staff
from models.user import User  # Import the User model

def main():
    # Create the default Manager user if it doesn't already exist
    User.create_default_user()

    # Create the default Members for default users
    Member.create_default_member()

    # Create the default trainer staff for Member roles
    Staff.create_default_staff()

    # Now, run the gym system
    system = GymSystem()
    system.run()

if __name__ == "__main__":
    main()
