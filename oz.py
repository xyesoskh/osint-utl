import pyfiglet
from rich.console import Console
from rich.text import Text

console = Console()

# Градиентный заголовок
ascii_title = pyfiglet.figlet_format("OZ OSINT", font="slant")
gradient_text = Text(ascii_title, style="bold")
gradient_text.stylize("gradient(blue, magenta)")

def show_banner():
    console.clear()
    console.print(gradient_text)
    console.print("powered by ZYAMA NEVERMORSKY", style="bold magenta")

def format_data(label, value):
    if value:
        return f"[+] {label}: {value}"
    return ""

# Данные пользователя
profile = {
    "ФИО": None,
    "Город": None,
    "Номер телефона": None,
    "Дата рождения": None,
    "Адрес": None,
    "Паспорт": None,
    "СНИЛС": None,
    "TG": None,
    "VK": None,
    "OK": None,
    "TT": None,
    "ФОТО": None,
    "Цель": None
}

def input_profile():
    console.print("\n[bold cyan]Введите информацию:[/bold cyan]")
    profile["Цель"] = input("Кто (например, мама, папа, сам): ")
    profile["ФИО"] = input("ФИО: ")
    profile["Город"] = input("Город: ")
    profile["Номер телефона"] = input("Номер телефона: ")
    profile["Дата рождения"] = input("Дата рождения (дд.мм.гггг): ")
    profile["Адрес"] = input("Адрес: ")
    profile["Паспорт"] = input("Серия и номер паспорта: ")
    profile["СНИЛС"] = input("СНИЛС: ")
    profile["TG"] = input("TG: ")
    profile["VK"] = input("VK: ")
    profile["OK"] = input("OK: ")
    profile["TT"] = input("TT: ")
    profile["ФОТО"] = input("ФОТО: ")
    console.print("\n[bold green]Данные человека сохранены![/bold green]\n")
    show_profile()

def show_profile():
    if not any(profile.values()):
        console.print("\n[bold red]Данные человека ещё не сохранены.[/bold red]")
        return
    console.print(f"\n[bold green]{profile['Цель'].upper()}[/bold green]")
    for key, value in profile.items():
        if key != "Цель":
            line = format_data(key, value)
            if line:
                console.print(line)

def report_menu():
    console.clear()
    show_banner()
    console.print("\n[bold red]Снос аккаунта (жалоба):[/bold red]")
    console.print("[1] Спам")
    console.print("[2] Мошенничество")
    console.print("[3] Призыв к насилию")
    console.print("[4] Прочее")
    console.print("[0] Назад")

    choice = input("\nВыберите причину жалобы: ")

    reasons = {
        "1": "Спам",
        "2": "Мошенничество",
        "3": "Призыв к насилию",
        "4": "Прочее"
    }

    if choice in reasons:
        console.print(f"\n[bold green]Жалоба отправлена по причине: {reasons[choice]}[/bold green]")
    elif choice == "0":
        return
    else:
        console.print("\n[bold red]Неверный выбор![/bold red]")

    input("\n[Нажмите Enter, чтобы вернуться в меню...]")
    report_menu()

def search_menu():
    console.clear()
    show_banner()
    console.print("\n[bold cyan]Меню поиска:[/bold cyan]")
    console.print("[1] Поиск по номеру телефона")
    console.print("[2] Поиск по email")
    console.print("[3] Поиск по нику")
    console.print("[4] По Telegram ID")
    console.print("[0] Назад")

    choice = input("\nВыберите тип поиска: ")

    if choice == "0":
        return
    elif choice in ["1", "2", "3", "4"]:
        console.print(f"\n[bold red]Функция {choice} пока не реализована.[/bold red]")
    else:
        console.print("\n[bold red]Неверный выбор![/bold red]")

    input("\n[Нажмите Enter, чтобы вернуться в меню...]")
    search_menu()

def main_menu():
    while True:
        show_banner()
        console.print("\n[bold cyan]Главное меню:[/bold cyan]")
        console.print("[1] Поиск")
        console.print("[2] GeoOSINT [UNWORK]")
        console.print("[3] Снос аккаунта [UNWORK]")
        console.print("[4] Ввод и оформление данных")
        console.print("[5] Выход")

        choice = input("\nВыберите пункт: ")

        if choice == "1":
            search_menu()
        elif choice == "2":
            console.print("\n[bold red]Функция GeoOSINT пока не реализована.[/bold red]")
        elif choice == "3":
            report_menu()
        elif choice == "4":
            input_profile()
        elif choice == "5":
            console.print("\n[bold red]Выход из программы...[/bold red]")
            break
        else:
            console.print("[bold red]Неверный выбор![/bold red]")

        input("\n[Нажмите Enter, чтобы вернуться в меню...]")

# Запуск программы
main_menu()
