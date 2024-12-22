# controllers/user_controller.py
from controllers.auth_controller import AuthController
from models.user import User
from models.staff import Staff
from models.member import Member
from models.gym_location import GymLocation  # Import GymLocation model
from views.user_view import UserView

class UserController:
    @staticmethod
    def manage_users(user):
        """
        Manages user-related actions like add, update, delete, and list.
        """
        while True:
            choice = UserView.display_user_menu()
            if choice == "1":  # List Users
                UserController.list_users()
            elif choice == "2":  # Return to main menu
                UserView.display_return_to_main_menu()
                return AuthController.display_menu_based_on_role(user)
            else:
                UserView.display_invalid_choice()

    @staticmethod
    def list_users():
        """
        Lists all users in the system.
        """
        users = User.get_all()
        if users:
            for user in users:
                UserView.display_user(user)
        else:
            UserView.display_no_users_found()
