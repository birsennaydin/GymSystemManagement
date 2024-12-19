class Payment:
    def __init__(self, payment_id, member_id, amount, payment_date, subscription_type):
        self.payment_id = payment_id
        self.member_id = member_id
        self.amount = amount
        self.payment_date = payment_date
        self.subscription_type = subscription_type

    # Getters and Setters
    def get_payment_id(self):
        return self.payment_id

    def set_payment_id(self, payment_id):
        self.payment_id = payment_id

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_payment_date(self):
        return self.payment_date

    def set_payment_date(self, payment_date):
        self.payment_date = payment_date

    def get_subscription_type(self):
        return self.subscription_type

    def set_subscription_type(self, subscription_type):
        self.subscription_type = subscription_type