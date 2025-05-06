import pyfiglet
from rich.console import Console
from rich.text import Text

console = Console()

# Градиентный заголовок
ascii_title = pyfiglet.figlet_format("OZ OSINT", font="slant")
gradient_text = Text(ascii_title, style="bold")
gradient_text.stylize("gradient(blue, magenta)")

def show_banner():
    console.print(gradient_text)
    console.print("powered by ZYAMA NEVERMORSKY", style="bold magenta")

def format_data(label, value):
    if value:
        return f"[+] {label}: {value}"
    return ""

# Словарь для анкеты
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
    
    console.clear()
    show_profile()

def show_profile():
    if not any(profile.values()):
        console.print("\n[bold red]Данные человека еще не сохранены.[/bold red]")
        return
    console.print(f"\n[bold green]{profile['Цель'].upper()}[/bold green]")
    for key, value in profile.items():
        if key != "Цель":
            console.print(format_data(key, value))

def edit_profile():
    if not any(profile.values()):
        console.print("\n[bold red]Сначала введите данные![/bold red]")
        return
    input_profile()

def main_menu():
    while True:
        console.clear()
        show_banner()
        console.print("\n[bold cyan]Главное меню:[/bold cyan]")
        console.print("[1] Поиск по username [bold red][UNWORK][/bold red]")
        console.print("[2] Снос аккаунта [bold red][UNWORK][/bold red]")
        console.print("[3] Оформить данные")
        console.print("[4] Показать данные")
        console.print("[5] Редактировать данные")
        console.print("[6] Выход")

        choice = input("\nВыберите пункт: ")

        if choice == "1":
            console.print("\n[bold red]Функция пробива пока не реализована.[/bold red]")
        elif choice == "2":
            console.print("\n[bold red]Функция сноса пока не реализована.[/bold red]")
        elif choice == "3":
            input_profile()
        elif choice == "4":
            show_profile()
        elif choice == "5":    
            edit_profile()
        elif choice == "6":
            console.print("\n[bold red]Выход из программы...[/bold red]")
            break
        else:
            console.print("[bold red]Неверный выбор![/bold red]")

        input("\n[Нажмите Enter, чтобы вернуться в меню...]")

# Запуск
main_menu()
