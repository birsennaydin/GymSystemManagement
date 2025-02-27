# models/enums.py
from enum import Enum

class MembershipType(Enum):
    REGULAR = 'Regular'
    PREMIUM = 'Premium'
    TRIAL = 'Trial'

class StaffRole(Enum):
    MANAGER = 'MANAGER'
    TRAINER = 'TRAINER'
    ATTENDANT = 'ATTENDANT'

class UserRole(Enum):
    MANAGER = 'MANAGER'  # Admin ve Manager aynı yetkilerle Manager rolüne döndü
    TRAINER = 'TRAINER'
    ATTENDANT = 'ATTENDANT'
    MEMBER = 'MEMBER'

class SubscriptionType(Enum):
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    ANNUAL = "Annual"

class DiscountStatus(Enum):
    YES = "Yes"
    NO = "No"

class CountryEnum(Enum):
    UNITED_KINGDOM = "United Kingdom"
    USA = "United States of America"
    CANADA = "Canada"
    GERMANY = "Germany"
    FRANCE = "France"
    TURKEY = "Turkey"

class CityEnum(Enum):
    LONDON = "London"
    NEW_YORK = "New York"
    TORONTO = "Toronto"
    BERLIN = "Berlin"
    PARIS = "Paris"
    ISTANBUL = "Istanbul"

class GymTypeEnum(Enum):
    FITNESS = "Fitness"
    YOGA = "Yoga"
    PILATES = "Pilates"
    CROSSFIT = "CrossFit"
    BOXING = "Boxing"
    MARTIAL_ARTS = "Martial Arts"

class PaymentMethodEnum(Enum):
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    PAYPAL = "PayPal"
    CASH = "Cash"

class AttendanceStatusEnum(Enum):
    PRESENT = "Present"
    ABSENT = "Absent"
    LATE = "Late"
