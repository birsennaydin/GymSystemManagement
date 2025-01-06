import unittest
from models.payment import Payment
from models.enums import PaymentMethodEnum, SubscriptionType, DiscountStatus
from models.member import Member
from views.payment_view import PaymentView


class TestPayment(unittest.TestCase):

    def setUp(self):
        """This method will run before every test."""
        # Clear the payments list before each test to avoid any conflicts.
        Payment.payments = []
        Payment.id_counter = 1
        Member.members = []

    def test_create_payment(self):
        """Test that a payment is created successfully with valid details."""
        member = Member(
            name="Birsen",
            email="birsen@example.com",
            phone="1234567890",
            membership_type="Regular",
            health_info="Healthy",
            status="Active",
            gym_location_id=1,
            user_id=101
        )

        payment = Payment(
            member_id=member.id,
            amount=100.0,
            payment_date="2025-01-10 09:00",
            payment_method=PaymentMethodEnum.CREDIT_CARD.value,
            subscription_plan=SubscriptionType.MONTHLY.value,
            discount_applied=DiscountStatus.NO.value,
            transaction_id="1234567890"
        )

        self.assertEqual(len(Payment.payments), 1)  # One payment should be created
        self.assertEqual(payment.member_id, member.id)
        self.assertEqual(payment.amount, 100.0)
        self.assertEqual(payment.payment_method, PaymentMethodEnum.CREDIT_CARD.value)
        self.assertEqual(payment.subscription_plan, SubscriptionType.MONTHLY.value)
        self.assertEqual(payment.discount_applied, DiscountStatus.NO.value)
        self.assertEqual(payment.transaction_id, "1234567890")

    def test_invalid_payment_method(self):
        """Test that creating a payment with an invalid payment method raises a ValueError."""
        with self.assertRaises(ValueError):
            payment = Payment(
                member_id=1,
                amount=50.0,
                payment_date="2025-01-10 09:00",
                payment_method="InvalidMethod",  # Invalid payment method
                subscription_plan=SubscriptionType.MONTHLY.value,
                discount_applied=DiscountStatus.NO.value,
                transaction_id="1234567890"
            )

    def test_invalid_subscription_plan(self):
        """Test that creating a payment with an invalid subscription plan raises a ValueError."""
        with self.assertRaises(ValueError):
            payment = Payment(
                member_id=1,
                amount=50.0,
                payment_date="2025-01-10 09:00",
                payment_method=PaymentMethodEnum.CREDIT_CARD.value,
                subscription_plan="InvalidPlan",  # Invalid subscription plan
                discount_applied=DiscountStatus.NO.value,
                transaction_id="1234567890"
            )

    def test_invalid_discount_status(self):
        """Test that creating a payment with an invalid discount status raises a ValueError."""
        with self.assertRaises(ValueError):
            payment = Payment(
                member_id=1,
                amount=50.0,
                payment_date="2025-01-10 09:00",
                payment_method=PaymentMethodEnum.CREDIT_CARD.value,
                subscription_plan=SubscriptionType.MONTHLY.value,
                discount_applied="InvalidStatus",  # Invalid discount status
                transaction_id="1234567890"
            )

    def test_apply_discount(self):
        """Test that the discount is applied correctly based on the subscription plan."""
        member = Member(
            name="Jane Doe",
            email="jane.doe@example.com",
            phone="9876543210",
            membership_type="Regular",
            health_info="Healthy",
            status="Active",
            gym_location_id=1,
            user_id=102
        )

        # Test for annual subscription (20% discount)
        payment = Payment(
            member_id=member.id,
            amount=100.0,
            payment_date="2025-01-10 09:00",
            payment_method=PaymentMethodEnum.CREDIT_CARD.value,
            subscription_plan=SubscriptionType.ANNUAL.value,
            discount_applied=DiscountStatus.YES.value,
            transaction_id="1234567891"
        )
        self.assertEqual(payment.amount, 80.0)  # 20% discount applied

        # Test for quarterly subscription (10% discount)
        payment = Payment(
            member_id=member.id,
            amount=100.0,
            payment_date="2025-01-10 09:00",
            payment_method=PaymentMethodEnum.CREDIT_CARD.value,
            subscription_plan=SubscriptionType.QUARTERLY.value,
            discount_applied=DiscountStatus.YES.value,
            transaction_id="1234567892"
        )
        self.assertEqual(payment.amount, 90.0)  # 10% discount applied

        # Test for monthly subscription (no discount)
        payment = Payment(
            member_id=member.id,
            amount=100.0,
            payment_date="2025-01-10 09:00",
            payment_method=PaymentMethodEnum.CREDIT_CARD.value,
            subscription_plan=SubscriptionType.MONTHLY.value,
            discount_applied=DiscountStatus.NO.value,
            transaction_id="1234567893"
        )
        self.assertEqual(payment.amount, 100.0)  # No discount applied

    def test_get_all_payments(self):
        """Test that the get_all method returns all payments."""
        member = Member(
            name="Alice",
            email="alice@example.com",
            phone="9876543210",
            membership_type="Regular",
            health_info="Normal",
            status="Active",
            gym_location_id=2,
            user_id=103
        )
        Payment(
            member_id=member.id,
            amount=50.0,
            payment_date="2025-01-10 09:00",
            payment_method=PaymentMethodEnum.CREDIT_CARD.value,
            subscription_plan=SubscriptionType.MONTHLY.value,
            discount_applied=DiscountStatus.NO.value,
            transaction_id="1234567890"
        )
        Payment(
            member_id=member.id,
            amount=150.0,
            payment_date="2025-01-11 10:00",
            payment_method=PaymentMethodEnum.PAYPAL.value,
            subscription_plan=SubscriptionType.ANNUAL.value,
            discount_applied=DiscountStatus.YES.value,
            transaction_id="1234567891"
        )

        payments = Payment.get_all()
        self.assertEqual(len(payments), 2)
        self.assertEqual(payments[0].amount, 50.0)
        #There is a discount for annual members
        self.assertEqual(payments[1].amount, 120.0)

    def test_get_payment_by_id(self):
        """Test that a payment can be retrieved by its ID."""
        member = Member(
            name="Birsen",
            email="birsen@example.com",
            phone="1234567890",
            membership_type="Premium",
            health_info="Healthy",
            status="Active",
            gym_location_id=3,
            user_id=104
        )
        payment = Payment(
            member_id=member.id,
            amount=75.0,
            payment_date="2025-01-10 09:00",
            payment_method=PaymentMethodEnum.PAYPAL.value,
            subscription_plan=SubscriptionType.QUARTERLY.value,
            discount_applied=DiscountStatus.YES.value,
            transaction_id="1234567894"
        )

        found_payment = Payment.get_by_id(payment.id)
        self.assertEqual(found_payment.id, payment.id)
        self.assertEqual(found_payment.member_id, member.id)

    def tearDown(self):
        """This method will run after every test."""
        # Reset the payments and other related lists after each test to maintain isolation
        Payment.payments = []
        Payment.id_counter = 1
        Member.members = []


if __name__ == '__main__':
    unittest.main()
