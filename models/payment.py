# models/payment.py
from models.enums import PaymentMethodEnum, SubscriptionType, DiscountStatus


class Payment:
    id_counter = 1
    payments = []

    def __init__(self, member_id, amount, payment_date, payment_method, subscription_plan, discount_applied,
                 transaction_id):
        self._id = Payment.id_counter
        self._member_id = None
        self._amount = None
        self._payment_date = None
        self._payment_method = None
        self._subscription_plan = None
        self._discount_applied = None
        self._transaction_id = None

        self.member_id = member_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.subscription_plan = subscription_plan
        self.discount_applied = discount_applied
        self.transaction_id = transaction_id

        Payment.id_counter += 1
        Payment.payments.append(self)

        # Calculate the discount
        self.apply_discount()

    @property
    def id(self):
        return self._id

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Member ID must be an integer.")
        self._member_id = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Amount must be a positive number.")
        self._amount = value

    @property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, value):
        if not value:
            raise ValueError("Payment date cannot be empty.")
        self._payment_date = value

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        if value not in [member.value for member in PaymentMethodEnum]:
            raise ValueError(
                f"Invalid payment method. Please choose from {', '.join([member.value for member in PaymentMethodEnum])}.")
        self._payment_method = value

    @property
    def subscription_plan(self):
        return self._subscription_plan

    @subscription_plan.setter
    def subscription_plan(self, value):
        if value not in [member.value for member in SubscriptionType]:
            raise ValueError(
                f"Invalid subscription plan. Please choose from {', '.join([member.value for member in SubscriptionType])}.")
        self._subscription_plan = value

    @property
    def discount_applied(self):
        return self._discount_applied

    @discount_applied.setter
    def discount_applied(self, value):
        if value not in [member.value for member in DiscountStatus]:
            raise ValueError(
                f"Invalid discount status. Please choose from {', '.join([member.value for member in DiscountStatus])}.")
        self._discount_applied = value

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        if not value:
            raise ValueError("Transaction ID cannot be empty.")
        self._transaction_id = value

    @classmethod
    def get_all(cls):
        return cls.payments

    @classmethod
    def get_by_id(cls, id):
        return next((payment for payment in cls.payments if payment.id == id), None)

    def apply_discount(self):
        """Apply discounts based on the subscription plan."""
        if self.discount_applied:
            # Define discount rates based on subscription type
            if self.subscription_plan == SubscriptionType.ANNUAL.value:
                discount_rate = 0.20  # 20% discount for annual subscription
            elif self.subscription_plan == SubscriptionType.QUARTERLY.value:
                discount_rate = 0.10  # 10% discount for quarterly subscription
            else:
                discount_rate = 0.0  # No discount for monthly subscription

            # Apply the discount to the amount
            self._amount -= self._amount * discount_rate