class UserNotFound(Exception):
    """Exception raised when a user is not found in the database."""

    def _init_(self, user_id):
        self.user_id = user_id
        super()._init_(f"User with ID {user_id} not found in the database.")


class OrderNotFound(Exception):
    """Exception raised when an order is not found in the database."""

    def _init_(self, user_id, order_id):
        self.user_id = user_id
        self.order_id = order_id
        super()._init_(f"Order with ID {order_id} for user {user_id} not found in the database.")


class UnauthorizedAccess(Exception):
    """Exception raised when user is not Authorized."""


    def _init_(self, message="Unauthorized access"):
        self.message = message
        super()._init_(self.message)