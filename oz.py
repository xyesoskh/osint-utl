import pyfiglet
from rich.console import Console
from rich.text import Text

# Настройка консоли
console = Console()

# Генерация текста с pyfiglet для заголовка
ascii_title = pyfiglet.figlet_format("NOVA OSINT", font="slant")

# Создание текста с плавным градиентом
gradient_text = Text(ascii_title, style="bold")
gradient_text.stylize("gradient(blue, magenta)")

# Вывод заголовка с градиентом
console.print(gradient_text)
console.print("powered by ZYAMA NEVERMORSKY", style="bold magenta")

# Функция для оформления и вывода данных
def format_data(label, value):
    if value is not None:
        return f"[+] {label}: {value}"
    return ""

# Сбор данных
print("Введите информацию для создания профиля:")

fio = input("Введите ФИО: ")
city = input("Введите город: ")
phone_number = input("Введите номер телефона: ")
dob = input("Введите дату рождения (дд.мм.гггг): ")
address = input("Введите адрес: ")
passport = input("Введите серию и номер паспорта: ")
snils = input("Введите СНИЛС: ")
socials = input("Введите соц. сети: ")

# Добавление цели
goal = input("Введите цель (например, мама, папа, или само): ")

# Печать оформленных данных
console.print(f"\n[bold green]Цель: {goal}[/bold green]")

# Вывод всех данных с форматированием
console.print(format_data("ФИО", fio))
console.print(format_data("Город", city))
console.print(format_data("Номер телефона", phone_number))
console.print(format_data("Дата рождения", dob))
console.print(format_data("Адрес", address))
console.print(format_data("Паспорт", passport))
console.print(format_data("СНИЛС", snils))
console.print(format_data("Соц. сети", socials))

# Главное меню
menu_options = [
    "[1] Показать профиль",
    "[2] Внести изменения",
    "[3] Выход"
]

# Отображение меню
console.print("\n[bold cyan]Меню:[/bold cyan]")
for option in menu_options:
    console.print(option)

# Выбор опции меню
choice = input("Выберите опцию: ")

if choice == "1":
    console.print("\n[bold blue]Профиль пользователя:[/bold blue]")
    console.print(format_data("ФИО", fio))
    console.print(format_data("Город", city))
    console.print(format_data("Номер телефона", phone_number))
    console.print(format_data("Дата рождения", dob))
    console.print(format_data("Адрес", address))
    console.print(format_data("Паспорт", passport))
    console.print(format_data("СНИЛС", snils))
    console.print(format_data("Соц. сети", socials))

elif choice == "2":
    console.print("\n[bold yellow]Внесите изменения в профиль:[/bold yellow]")
    # Повторный ввод данных для изменений
    fio = input("Введите новое ФИО: ")
    city = input("Введите новый город: ")
    phone_number = input("Введите новый номер телефона: ")
    dob = input("Введите новую дату рождения: ")
    address = input("Введите новый адрес: ")
    passport = input("Введите новый паспорт: ")
    snils = input("Введите новый СНИЛС: ")
    socials = input("Введите новые соц. сети: ")
    console.print("\n[bold green]Данные обновлены![/bold green]")

elif choice == "3":
    console.print("\n[bold red]Выход из программы...[/bold red]")

else:
    console.print("\n[bold red]Неверный выбор! Попробуйте снова.[/bold red]")
