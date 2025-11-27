
class MainPageSelectors:

    # header selectors
    button_logo = {
        "data-testid": "logo",
        "selector": ".max-w-[80px].md:max-w-[140px]",
        "description": "Кнопка logo"
    }

    button_favorite = {
        "data-testid": "logo",
        "selector": "",
        "description": "Кнопка favorite"

    }

    button_enter = {
        "data-testid": "logo",
        "selector": "#id_button",
        "role": "button",
        "description": "Кнопка 'Войти'",
        "text": "Войти"
    }

    email_field = {
        "selector": "#email_input",
        "data-testid": "logo",
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
