from fastapi import  FastAPI
from app.core.exceptions import (HabitNotFoundException,
                                 HabitLogNotFoundException,
                                 UnauthorizedAccessException,
                                 UserNotFoundException,
                                 InvalidCredentialsException,
                                 DiaryEntryNotFound,
                                 EmailNotAcceptableException,
                                 InvalidGoogleTokenException,
                                 InvalidAppleTokenException,
                                 SubscriptionPlanNotFoundException, )

from app.core.exception_handlers import (habit_not_found_handler,
                                         habit_log_not_found_handler,
                                         unauthorized_access_handler,
                                         user_not_found_handler,
                                         invalid_credentials_handler,
                                         diary_entry_not_found,
                                         email_not_acceptable_handler,
                                         invalid_google_token_handler,
                                         invalid_apple_token_handler,
                                         subscription_plan_not_found_handler, )

def register_exception_handlers(app:FastAPI):
    app.add_exception_handler(
        HabitNotFoundException,
        habit_not_found_handler
    )

    app.add_exception_handler(
        HabitLogNotFoundException,
        habit_log_not_found_handler
    )

    app.add_exception_handler(
        DiaryEntryNotFound,
        diary_entry_not_found
    )

    app.add_exception_handler(
        UserNotFoundException,
        user_not_found_handler
    )

    app.add_exception_handler(
        InvalidCredentialsException,
        invalid_credentials_handler
    )

    app.add_exception_handler(
        UnauthorizedAccessException,
        unauthorized_access_handler
    )

    app.add_exception_handler(
        EmailNotAcceptableException,
        email_not_acceptable_handler
    )

    app.add_exception_handler(
        InvalidGoogleTokenException,
        invalid_google_token_handler
    )

    app.add_exception_handler(
        InvalidAppleTokenException,
        invalid_apple_token_handler
    )

    app.add_exception_handler(
        SubscriptionPlanNotFoundException,
        subscription_plan_not_found_handler
    )