from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.theme import Theme
from rich.style import Style
from rich.color import Color

# Настроим консоль с пользовательской темой
custom_theme = Theme({
    "field": "bold cyan",
    "label": "bold magenta",
    "title": Style(color="magenta", bgcolor="yellow", bold=True),  # Простой стиль для заголовка
    "menu": "bold green",
    "input": "bold yellow"
})
console = Console(theme=custom_theme)

people_data = []  # Список для хранения информации о людях

def format_field(prompt, label, capitalize=False):
    console.print(f"[input]{prompt}[/input]", end=": ")
    value = input().strip()
    if not value:
        return None
    if capitalize:
        parts = value.lower().split()
        value = " ".join(part.capitalize() for part in parts)
    return f"[bold cyan][+] {label}:[/bold cyan] {value}"

def input_person():
    console.print("\n[input]Кто этот человек? (например: сам, мама, папа и т.д.)[/input]", end=": ")
    subject = input().strip().upper() or "ДАННЫЕ"

    fields = [
        ("Введите ФИО", "ФИО", True),
        ("Введите город", "Город", True),
        ("Введите номер телефона", "Номер телефона", False),
        ("Введите дату рождения", "Дата рождения", False),
        ("Введите адрес", "Адрес", False),
        ("Введите серию и номер паспорта", "Паспорт", False),
        ("Введите СНИЛС", "СНИЛС", False),
        ("Введите соц. сети", "Соц. сети", False),
    ]

    person = []
    for prompt, label, capitalize in fields:
        result = format_field(prompt, label, capitalize)
        if result:
            person.append(result)

    people_data.append((subject, person))
    console.print(f"\n[menu]Данные для [{subject}] успешно сохранены.[/menu]\n")

def display_people():
    if not people_data:
        console.print("[bold red]Нет сохранённых данных.[/bold red]")
        return
    for subject, info in people_data:
        title = Text(subject, style="title")
        body = "\n".join(info)
        panel = Panel(body, title=title, border_style="cyan", expand=False)
        console.print(panel)

def main_menu():
    while True:
        console.print("\n[menu]Выберите действие:[/menu]")
        console.print("[1] Ввести данные")
        console.print("[2] Показать все данные")
        console.print("[3] Выход")

        console.print("\n[input]Введите номер действия[/input]", end=": ")
        choice = input().strip()

        if choice == "1":
            input_person()
        elif choice == "2":
            display_people()
        elif choice == "3":
            console.print("[bold red]Выход из программы...[/bold red]")
            break
        else:
            console.print("[bold red]Неверный выбор. Попробуйте снова.[/bold red]")

if __name__ == "__main__":
    main_menu()
