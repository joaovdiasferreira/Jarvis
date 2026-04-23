from automatization.apps_init import chrome_init, app_init, lenovo_vantage_init


def execute_automation(command):
    if "abrir" in command:
        app = command.replace("abrir", "").strip()
        match app:
            case "chrome":
                chrome_init()
            case "lenovo app":
                lenovo_vantage_init()
            case _:
                app_init(app)

    if "desligar" in command:
        return "exit"

    return "Não entendi."