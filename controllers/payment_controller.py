import uuid
from datetime import datetime

from models.member import Member
from models.payment import Payment
from views.payment_view import PaymentView

class PaymentController:
    @staticmethod
    def process_payments(user):
        from controllers.auth_controller import AuthController
        while True:
            choice = PaymentView.display_payment_menu()

            if choice == "1":
                PaymentController.add_payment()
            elif choice == "2":
                PaymentController.list_payments()
            elif choice == "3":
                PaymentView.display_return_to_main_menu()
                return AuthController.display_menu_based_on_role(user)
            else:
                PaymentView.display_invalid_choice()

    @staticmethod
    def add_payment():
        members = Member.get_all()  # Fetch all members
        member_id = PaymentView.get_member_id(members)  # Select member from the list
        amount = PaymentView.get_payment_amount()
        payment_method = PaymentView.get_payment_method()  # Get the payment method
        subscription_plan = PaymentView.get_subscription_plan()

        # Collect discount applied (ask the user if discount was applied)
        discount_applied = PaymentView.get_discount_applied()

        # Get the transaction ID, if left blank, generate a system ID
        transaction_id = PaymentView.get_transaction_id()  # User can input transaction ID

        # Get the current date and time for payment date
        payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current date in the format YYYY-MM-DD HH:MM:SS

        # Create the new payment record
        payment = Payment(
            member_id=member_id,
            amount=amount,
            payment_date=payment_date,  # Current date and time
            payment_method=payment_method,
            subscription_plan=subscription_plan,
            discount_applied=discount_applied,
            transaction_id=transaction_id  # Pass the transaction ID here
        )

        # Show success message
        PaymentView.display_payment_success(payment)

    @staticmethod
    def list_payments():
        payments = Payment.get_all()
        if not payments:
            PaymentView.display_no_payments_found()
        else:
            for payment in payments:
                PaymentView.display_payment_list(payment)
