# views/payment_view.py
class PaymentView:
    @staticmethod
    def display_payment_menu():
        print("\nPayment and Subscription Menu")
        print("1. Add Payment")
        print("2. List Payments")
        print("3. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_member_id():
        return input("Enter Member ID: ")

    @staticmethod
    def get_payment_amount():
        return input("Enter Payment Amount: ")

    @staticmethod
    def get_payment_method():
        return input("Enter Payment Method (Credit Card, Bank Transfer, etc.): ")

    @staticmethod
    def get_subscription_plan():
        print("Choose Subscription Plan:")
        print("1. Monthly")
        print("2. Quarterly")
        print("3. Annual")
        return input("Enter choice (1/2/3): ").strip()

    @staticmethod
    def display_payment_success(payment):
        print(f"Payment of {payment.amount} processed successfully!")

    @staticmethod
    def display_payment_list(payment):
        print(f"ID: {payment.id}, Member ID: {payment.member_id}, Amount: {payment.amount}, Payment Method: {payment.payment_method}, Subscription Plan: {payment.subscription_plan}")

    @staticmethod
    def display_no_payments_found():
        print("No payments found.")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")
