import pytest

from registration_service import (
    RegistrationService,
    InvalidEmailError,
    UnderageError
)


@pytest.fixture
def registration_service():
    """
    Shared fixture for creating the service instance.
    """
    return RegistrationService()


def test_successful_registration(registration_service):
    result = registration_service.register_user(
        "john_doe@example.com",
        25
    )

    assert result is True


def test_valid_boundary_age_18(registration_service):
    result = registration_service.register_user(
        "adult@example.com",
        18
    )

    assert result is True


def test_null_email_raises_error(registration_service):
    with pytest.raises(InvalidEmailError) as exc_info:
        registration_service.register_user(None, 25)

    assert "Invalid email provided" in str(exc_info.value)


def test_empty_email_raises_error(registration_service):
    with pytest.raises(InvalidEmailError) as exc_info:
        registration_service.register_user("   ", 25)

    assert "Invalid email provided" in str(exc_info.value)


def test_invalid_email_format_raises_error(registration_service):
    with pytest.raises(InvalidEmailError) as exc_info:
        registration_service.register_user("invalid-email", 25)

    assert "Invalid email provided" in str(exc_info.value)


def test_underage_user_raises_error(registration_service):
    with pytest.raises(UnderageError) as exc_info:
        registration_service.register_user(
            "teen@example.com",
            16
        )

    assert "at least 18 years old" in str(exc_info.value)


def test_negative_age_assertion(registration_service):
    with pytest.raises(AssertionError) as exc_info:
        registration_service.register_user(
            "test@example.com",
            -1
        )

    assert "age cannot be negative" in str(exc_info.value)
