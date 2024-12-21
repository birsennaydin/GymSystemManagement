# controllers/payment_controller.py
from models.payment import Payment
from views.payment_view import PaymentView

class PaymentController:
    @staticmethod
    def process_payments():
        while True:
            choice = PaymentView.display_payment_menu()

            if choice == "1":
                PaymentController.add_payment()
            elif choice == "2":
                PaymentController.list_payments()
            elif choice == "3":
                PaymentView.display_return_to_main_menu()
                break
            else:
                PaymentView.display_invalid_choice()

    @staticmethod
    def add_payment():
        member_id = PaymentView.get_member_id()
        amount = PaymentView.get_payment_amount()
        payment_method = PaymentView.get_payment_method()
        subscription_plan = PaymentView.get_subscription_plan()

        payment = Payment(
            member_id=member_id, 
            amount=amount, 
            payment_method=payment_method, 
            subscription_plan=subscription_plan
        )
        PaymentView.display_payment_success(payment)

    @staticmethod
    def list_payments():
        payments = Payment.get_all()
        if not payments:
            PaymentView.display_no_payments_found()
        else:
            for payment in payments:
                PaymentView.display_payment_list(payment)
