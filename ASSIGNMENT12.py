from abc import ABC, abstractmethod


# =========================
# ORDER TYPES
# =========================

class Order(ABC):

    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    @abstractmethod
    def get_total(self):
        pass


class RegularOrder(Order):

    def get_total(self):
        return self.amount


class DiscountOrder(Order):

    def get_total(self):
        return self.amount * 0.9   # 10% discount


class PriorityOrder(Order):

    def get_total(self):
        return self.amount + 100   # extra priority fee


# =========================
# PAYMENT METHODS
# =========================

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class WalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


# =========================
# NOTIFICATIONS
# =========================

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):

    def send(self, message):
        print(f"Email: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"SMS: {message}")


# =========================
# STORAGE
# =========================

class Storage(ABC):

    @abstractmethod
    def save(self, order):
        pass


class DatabaseStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved in Database")


class FileStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved in File")


# =========================
# ORDER SERVICE
# =========================

class OrderService:

    def __init__(self, payment, notification, storage):
        self.payment = payment
        self.notification = notification
        self.storage = storage

    def place_order(self, order):

        total = order.get_total()

        print(f"\nProcessing Order {order.order_id}")

        # payment
        self.payment.pay(total)

        # save order
        self.storage.save(order)

        # notification
        self.notification.send("Order placed successfully")


# =========================
# MAIN
# =========================

# Create Order
order = DiscountOrder(101, 2000)

# Inject dependencies
payment = UPIPayment()
notification = EmailNotification()
storage = DatabaseStorage()

# Place order
service = OrderService(payment, notification, storage)

service.place_order(order)
