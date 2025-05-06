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
    console.print("powered by ZYAMA", style="bold magenta")

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
    "Соц. сети": None,
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
    profile["Соц. сети"] = input("Соц. сети: ")
    console.print("\n[bold green]Анкета создана![/bold green]")

def show_profile():
    if not any(profile.values()):
        console.print("\n[bold red]Анкета ещё не создана.[/bold red]")
        return
    console.print(f"\n[bold green]{profile['Цель'].upper()}[/bold green]")
    for key, value in profile.items():
        if key != "Цель":
            console.print(format_data(key, value))

def edit_profile():
    if not any(profile.values()):
        console.print("\n[bold red]Сначала создайте анкету![/bold red]")
        return
    input_profile()

def main_menu():
    while True:
        show_banner()
        console.print("\n[bold cyan]Главное меню:[/bold cyan]")
        console.print("[1] Снос аккаунта [bold red][UNWORK][/bold red]")
        console.print("[2] Создать анкету")
        console.print("[3] Показать анкету")
        console.print("[4] Редактировать анкету")
        console.print("[5] Выход")

        choice = input("\nВыберите пункт: ")

        if choice == "2":
            input_profile()
        elif choice == "3":
            show_profile()
        elif choice == "4":
            edit_profile()
        elif choice == "5":
            console.print("\n[bold red]Выход из программы...[/bold red]")
            break
        elif choice == "1":
            console.print("\n[bold red]Функция UNWORK пока не реализована.[/bold red]")
        else:
            console.print("[bold red]Неверный выбор![/bold red]")

        input("\n[Нажмите Enter, чтобы вернуться в меню...]")
        console.clear()

# Запуск
main_menu()
