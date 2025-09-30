from pydantic import BaseModel, field_validator, Field
from typing import List, Optional
from endpoints.check_status_code_and_model import BaseApi



class LoginSuccess200(BaseModel):
    access_token: str = Field(min_length=1)
    refresh_token: str = Field(min_length=1)


class LoginEmailNotExist400(BaseModel):
    non_field_errors: List[str] = Field(min_length=1)
    @field_validator('non_field_errors')
    @classmethod
    def field_data(cls, value: str, data):
        data = ["Неверный email или пароль."]
        return BaseApi.field_data(value, data)


class LoginPasswordIncorrect400(BaseModel):
    non_field_errors: List[str] = Field(min_length=1)
    @field_validator('non_field_errors')
    @classmethod
    def field_data(cls, value: str, data):
        data = ["Неверный email или пароль."]
        return BaseApi.field_data(value, data)


class LoginEmailEmpty400(BaseModel):
    email: List[str] = Field(min_length=1)
    @field_validator('email')
    @classmethod
    def field_data(cls, value: str, data):
        data = ["Это поле не может быть пустым."]
        return BaseApi.field_data(value, data)


class LogoutSuccess200(BaseModel):
    detail: str = Field(min_length=1)
    @field_validator('detail')
    @classmethod
    def field_data(cls, value: str, data):
        data = "Вы успешно вышли из аккаунта."
        return BaseApi.field_data(value, data)


class LogoutError400(BaseModel):
    detail: str = Field(min_length=1)
    @field_validator('detail')
    @classmethod
    def field_data(cls, value: str, data):
        data = "Необходим refresh-токен."
        return BaseApi.field_data(value, data)


class RefreshTokenSuccess200(BaseModel):
    access_token: str = Field(min_length=1)

