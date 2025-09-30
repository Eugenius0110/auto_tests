from pydantic import BaseModel, field_validator, Field
from typing import List, Optional
from endpoints.check_status_code_and_model import BaseApi

class ResetPassword200(BaseModel):
    detail: str = Field(min_length=1)
    @field_validator('detail')
    @classmethod
    def field_data(cls, value: str):
        data = "Если пользователь существует, на его почту отправлен код."
        return BaseApi.field_data(value, data)


class ResetPasswordEmailNotExist400(BaseModel):
    email: List[str] = Field(min_length=1)
    @field_validator('email')
    @classmethod
    def field_data(cls, value: str):
        data = ["Пользователь с таким email не найден."]
        return BaseApi.field_data(value, data)


class ResetPasswordEmailIncorrect400(BaseModel):
    email: List[str] = Field(min_length=1)
    @field_validator('email')
    @classmethod
    def field_data(cls, value: str):
        data = ["Введите правильный адрес электронной почты."]
        return BaseApi.field_data(value, data)


class ResetPasswordLimitAttempt429(BaseModel):
    detail: str = Field(min_length=1)
    @field_validator('detail')
    @classmethod
    def field_data(cls, value: str):
        data = "Превышено количество попыток. Попробуйте позже."
        return BaseApi.field_data(value, data)


class VerifyResetCode200(BaseModel):
    detail: str = Field(min_length=1)
    user_id: Optional[str]
    @field_validator('detail')
    @classmethod
    def field_data(cls, value: str):
        data = "Код подтверждения верный."
        return BaseApi.field_data(value, data)


class VerifyResetCodeWrong400(BaseModel):
    non_field_errors: List[str] = Field(min_length=1)
    @field_validator('non_field_errors')
    @classmethod
    def field_data(cls, value: str):
        data = ["Неверный или истекший код подтверждения."]
        return BaseApi.field_data(value, data)


class SetNewPassword200(BaseModel):
    detail: str = Field(min_length=1)
    access_token: str = Field(min_length=1)
    refresh_token: str = Field(min_length=1)
    @field_validator('detail')
    @classmethod
    def field_data(cls, value: str):
        data = "Если пользователь существует, на его почту отправлен код."
        return BaseApi.field_data(value, data)


class SetPasswordNotConfirm400(BaseModel):
    new_password_confirm: List[str] = Field(min_length=1)
    @field_validator('new_password_confirm')
    @classmethod
    def field_data(cls, value: str):
        data = "Если пользователь существует, на его почту отправлен код."
        return BaseApi.field_data(value, data)


class SetPasswordCodeWrong400(BaseModel):
    pass
