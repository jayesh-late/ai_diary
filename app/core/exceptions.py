class HabitNotFoundException(Exception):
    """Raised when habit does not exist"""
    pass

class HabitLogNotFoundException(Exception):
    """Raised when habit log are missing"""
    pass

class DiaryEntryNotFound(Exception):
    """Raised when entry is missing"""
    pass

class UserNotFoundException(Exception):
    """Raised when user does not exist"""
    pass

class InvalidCredentialsException(Exception):
    """Raised when login credentials are invalid"""
    pass

class UnauthorizedAccessException(Exception):
    """Raised when user tries to access restricted resources"""
    pass

class EmailNotAcceptableException(Exception):
    """Raised when email are already registered"""
    pass

class InvalidGoogleTokenException(Exception):
    """Raised when google token is invalid"""
    pass

class InvalidAppleTokenException(Exception):
    """Raised when apple token is invalid"""
    pass

class SubscriptionPlanNotFoundException(Exception):
    """Raised when does not exist any subscription plan"""
    pass