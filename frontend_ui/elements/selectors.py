
class MainPageSelectors:

    # header selectors
    logo = {
        "selector": "#id_logo",
        "description": "Логотип"
    }

    button_enter = {
        "selector": "#id_button",
        "role": "button",
        "description": "Кнопка 'Войти'",
        "text": "Войти"
    }

    email_field = {
        "selector": "#email_input",
        "role": "textbox",
        "description": "Поле ввода email",
        "placeholder": "Введите email",
        "type": "email",
        "required": True
    }

    password_field = {
        "selector": "#password_input",
        "role": "textbox",
        "description": "Поле ввода пароля",
        "placeholder": "Введите пароль",
        "type": "password",
        "required": True
    }
