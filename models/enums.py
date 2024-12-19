from enum import Enum

class MembershipType(Enum):
    REGULAR = 'Regular'
    PREMIUM = 'Premium'
    TRIAL = 'Trial'

class StaffRole(Enum):
    MANAGER = 'Manager'
    TRAINER = 'Trainer'
    CLEANER = 'Cleaner'

class SubscriptionType(Enum):
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    ANNUAL = "Annual"

class CountryEnum(Enum):
    UNITED_KINGDOM = "United Kingdom"
    USA = "United States of America"
    CANADA = "Canada"
    GERMANY = "Germany"
    FRANCE = "France"
    TURKEY = "Turkey"
    AUSTRALIA = "Australia"
    SPAIN = "Spain"
    ITALY = "Italy"
    INDIA = "India"

class CityEnum(Enum):
    LONDON = "London"
    NEW_YORK = "New York"
    TORONTO = "Toronto"
    BERLIN = "Berlin"
    PARIS = "Paris"
    ISTANBUL = "Istanbul"
    SYDNEY = "Sydney"
    MADRID = "Madrid"
    MILAN = "Milan"
    MUMBAI = "Mumbai"

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
