import re


class InvalidEmailError(ValueError):
    """
    Raised when the provided email is invalid.
    """

    def __init__(self, email: str):
        message = f"Invalid email provided: {email}"
        super().__init__(message)


class UnderageError(RuntimeError):
    """
    Raised when the user is below the minimum age requirement.
    """

    def __init__(self, age: int):
        message = f"User must be at least 18 years old. Provided age: {age}"
        super().__init__(message)


class RegistrationService:

    EMAIL_REGEX = r"^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    def register_user(self, email: str, age: int) -> bool:

        # Internal invariant assertion
        assert age >= 0, "System invariant violated: age cannot be negative"

        # Validate email presence
        if email is None or email.strip() == "":
            raise InvalidEmailError(email)

        # Validate email format
        if not re.match(self.EMAIL_REGEX, email):
            raise InvalidEmailError(email)

        # Validate age restriction
        if age < 18:
            raise UnderageError(age)

        # Registration successful
        return True
