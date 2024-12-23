import uuid

from models.enums import PaymentMethodEnum
from models.member import Member


class PaymentView:
    @staticmethod
    def display_payment_menu():
        print("\nPayment and Subscription Menu")
        print("1. Add Payment")
        print("2. List Payments")
        print("3. Back to Main Menu")
        return input("Enter your choice: ").strip()

    @staticmethod
    def get_member_id(members):
        print("\nSelect a Member:")
        for idx, member in enumerate(members, 1):
            print(f"{idx}. {member.name}")
        member_choice = int(input("Enter the number of the member: "))
        return members[member_choice - 1].id  # Return the selected member's ID

    @staticmethod
    def get_payment_amount():
        return float(input("Enter Payment Amount: "))

    @staticmethod
    def get_payment_method():
        # Display valid payment methods from the enum
        print("Choose Payment Method:")
        for idx, method in enumerate(PaymentMethodEnum, 1):
            print(f"{idx}. {method.value}")

        choice = input("Enter choice (1/2/3/4): ").strip()

        # Validate the user input and return the corresponding PaymentMethodEnum value
        try:
            # Map the input to the enum, using zero-based indexing (subtract 1 from the choice)
            selected_method = list(PaymentMethodEnum)[int(choice) - 1]
            return selected_method.value
        except (IndexError, ValueError):
            print("Invalid choice. Please select a valid payment method.")
            return PaymentView.get_payment_method()

    @staticmethod
    def get_subscription_plan():
        print("Choose Subscription Plan:")
        print("1. Monthly")
        print("2. Quarterly")
        print("3. Annual")
        choice = input("Enter choice (1/2/3): ").strip()

        payment_types = {
            "1": "Monthly",
            "2": "Quarterly",
            "3": "Annual"
        }

        return payment_types.get(choice, "Unknown")

    @staticmethod
    def get_discount_applied():
        print("Was a discount applied?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter choice (1/2): ").strip()

        discount_types = {
            "1": "Yes",
            "2": "No"
        }

        return discount_types.get(choice, "Unknown")

    @staticmethod
    def get_transaction_id():
        return str(uuid.uuid4())


    @staticmethod
    def display_payment_success(payment):
        print(f"Payment of {payment.amount} processed successfully!")

    @staticmethod
    def display_payment_list(payment):
        # Assuming you want to display the member name and payment details
        member_name = Member.get_by_id(payment.member_id).name  # Get the member name from the ID
        print(f"Payment ID: {payment.id}, Member: {member_name}, Amount: {payment.amount}, Payment Method: {payment.payment_method}, Subscription Plan: {payment.subscription_plan}, Discount Applied: {payment.discount_applied}, Transaction ID: {payment.transaction_id}")

    @staticmethod
    def display_no_payments_found():
        print("No payments found.")

    @staticmethod
    def display_invalid_choice():
        print("Invalid choice. Please try again.")

    @staticmethod
    def display_return_to_main_menu():
        print("Returning to Main Menu...")
