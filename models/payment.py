# models/payment.py
from models.enums import PaymentMethodEnum, SubscriptionType


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
        if value not in PaymentMethodEnum.__members__:
            raise ValueError(
                f"Invalid payment method. Please choose from {', '.join(PaymentMethodEnum.__members__.keys())}.")
        self._payment_method = value

    @property
    def subscription_plan(self):
        return self._subscription_plan

    @subscription_plan.setter
    def subscription_plan(self, value):
        if value not in SubscriptionType.__members__:
            raise ValueError(
                f"Invalid subscription plan. Please choose from {', '.join(SubscriptionType.__members__.keys())}.")
        self._subscription_plan = value

    @property
    def discount_applied(self):
        return self._discount_applied

    @discount_applied.setter
    def discount_applied(self, value):
        if not isinstance(value, bool):
            raise ValueError("Discount applied must be a boolean value (True/False).")
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
