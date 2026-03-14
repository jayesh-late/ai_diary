from fastapi import Request,status
from fastapi.responses import JSONResponse
from pyasn1_modules.rfc7906 import aa_userCertificate
from starlette.responses import Response
from app.core.exceptions import (
    HabitNotFoundException,
    HabitLogNotFoundException,
    UnauthorizedAccessException,
    UserNotFoundException,
    InvalidCredentialsException,
    DiaryEntryNotFound,
    EmailNotAcceptableException,
    InvalidAppleTokenException,
    InvalidGoogleTokenException,
    SubscriptionPlanNotFoundException,

)

async def habit_not_found_handler(request:Request,exc:HabitNotFoundException)->Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail":"Habit not found"
        }
    )

async def habit_log_not_found_handler(request:Request,exc:HabitLogNotFoundException)->Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail":"Habit log not found"
        }
    )

async def diary_entry_not_found(request:Request,exc:DiaryEntryNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail":"Entry not found"
        }
    )

async def unauthorized_access_handler(request:Request,exc:UnauthorizedAccessException)->Response:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "detail":"Unauthorized access"
        }
    )

async def user_not_found_handler(request:Request,exc:UserNotFoundException)->Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail":"User not found"
        }
    )

async def invalid_credentials_handler(request:Request,exc:InvalidCredentialsException)->Response:
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "detail":"Invalid credential"
        }
    )

async def email_not_acceptable_handler(request:Request, exc:EmailNotAcceptableException):
    return JSONResponse(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        content={
            "detail":"Already registered email"
        }
    )

async def invalid_apple_token_handler(request:Request,exc:InvalidAppleTokenException):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "detail":"Invalid apple token"
        }
    )

async def invalid_google_token_handler(request:Request,exc:InvalidGoogleTokenException):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"detail":"Invalid google token"}
    )

async def subscription_plan_not_found_handler(request:Request,exc:SubscriptionPlanNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail":"Subscription plan not found"}
    )