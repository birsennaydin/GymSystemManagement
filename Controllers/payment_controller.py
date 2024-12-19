from Models.payment import Payment
from Models.enums import SubscriptionType


class PaymentController:
    def __init__(self):
        self.payments = []

    def add_payment(self):
        print("Enter new payment details:")
        payment_id = int(input("Payment ID (integer): "))
        member_id = int(input("Member ID (integer): "))
        amount = float(input("Amount (float): "))
        payment_date = input("Payment Date (YYYY-MM-DD): ")
        subscription_type = self.get_subscription_type()

        new_payment = Payment(payment_id, member_id, amount, payment_date, subscription_type)
        self.payments.append(new_payment)
        print(f"Payment for member {member_id} added successfully!")

    def update_payment(self, payment_id):
        payment = self.get_payment_by_id(payment_id)
        if payment:
            print(f"Updating details for payment {payment.get_payment_id()}:")
            payment.set_amount(float(input(f"New Amount (current: {payment.get_amount()}): ") or payment.get_amount()))
            payment.set_payment_date(
                input(f"New Payment Date (current: {payment.get_payment_date()}): ") or payment.get_payment_date())
            payment.set_subscription_type(self.get_subscription_type() or payment.get_subscription_type())
            print(f"Payment {payment_id} updated successfully!")
        else:
            print("Payment not found!")

    def get_payment_by_id(self, payment_id):
        for payment in self.payments:
            if payment.get_payment_id() == payment_id:
                return payment
        return None

    def list_payments(self):
        if not self.payments:
            print("No payments found.")
            return
        for payment in self.payments:
            print(f"ID: {payment.get_payment_id()}, Amount: {payment.get_amount()}, Date: {payment.get_payment_date()}")

    def get_subscription_type(self):
        print("Choose Subscription Type:")
        print("1. Monthly")
        print("2. Quarterly")
        print("3. Annual")
        choice = input("Enter choice (1/2/3): ")
        if choice == '1':
            return SubscriptionType.MONTHLY
        elif choice == '2':
            return SubscriptionType.QUARTERLY
        elif choice == '3':
            return SubscriptionType.ANNUAL
        else:
            print("Invalid choice, defaulting to Monthly.")
            return SubscriptionType.MONTHLY