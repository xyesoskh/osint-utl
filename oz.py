import pyfiglet
from rich.console import Console
from rich.text import Text
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetHistoryRequest
import asyncio

# Настройки Telethon
api_id = 29459757
api_hash = '7cc969764c4de8a52169570ac20000a8'
session_string = "1ApWapzMBu4Sbmc7c5s44pLQ22UEse-Uyc0U0xWkxcOshYoED_Fb71Sq54idI6hqSNWQVG_gCDQhnUQVAFd_fQMcbRbNWvmoqDM4uS02q-RTcvwQT3mDOGcabfPwYaPV8oXtHfNTOHHY8vukH6NP7gSUBA4itvhpGn74nC1SfngevCA_LfGpeoOtN_jZDMG_zlWtlpAHxlJl6w5zS7qIR6kwSvD-HfKBCKlHOAdgMndoFEda47mrj35Glz1v7OVgFcv2RhxKPWCOkcynMIwLDpDyCjj1k_1zr_LtAuaDgrLKJVz0h5Khj7122_7b0H2kypMDzGOp5fqATdKt5KeS3PzkawZENeH0="
client = TelegramClient(StringSession(session_string), api_id, api_hash)

console = Console()

def show_banner():
    try:
        with open("ascii-art.txt", "r", encoding="utf-8") as f:
            ascii_art = f.read()
        console.print(Text(ascii_art, style="bold magenta"))
    except FileNotFoundError:
        console.print("ASCII арт не найден.", style="bold red")
    console.print("powered by ZYAMA", style="bold magenta")

def format_data(label, value):
    return f"[+] {label}: {value}" if value else ""

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

async def sherlock_phone_lookup(phone: str):
    await client.start()
    entity = await client.get_entity("@osinthelper123_bot")

    sent_message = await client.send_message(entity, phone)

    timeout = 25  # максимум 25 секунд ожидания
    elapsed = 0
    interval = 2  # каждые 2 секунды проверяем историю

    last_result = None

    while elapsed < timeout:
        history = await client(GetHistoryRequest(
            peer=entity,
            limit=10,
            offset_id=0,
            offset_date=None,
            add_offset=0,
            max_id=0,
            min_id=sent_message.id,
            hash=0
        ))

        # Берём только сообщения, которые новее отправленного
        messages = sorted([m for m in history.messages if m.id > sent_message.id], key=lambda m: m.date)

        for msg in messages:
            # Пропускаем промежуточные статусы
            if msg.message and "подождите" not in msg.message.lower():
                if msg.message != last_result:
                    last_result = msg.message
                    return last_result

        await asyncio.sleep(interval)
        elapsed += interval

    return "❌ Ошибка: бот не прислал итог за 25 секунд."

def parse_bot_message(message: str):
    fields = {
        "ФИО": r"(?:Имя|ФИО):\s*(.+)",
        "Регион": r"Город:\s*(.+)",
        "Номер телефона": r"Телефон:\s*(.+)",
        "Телефонные Книги": r"Записан:\s*(.+)",
        "E-mail": r"Email:/s*(.+)",
        "Дата рождения": r"Дата рождения:\s*(.+)",
        "Адрес": r"Адрес:\s*(.+)",
        "Паспорт": r"Паспорт:\s*(.+)",
        "СНИЛС": r"СНИЛС:\s*(.+)",
        "Telegram": r"TG ID:\s*@?(\S+)",
        "Вконтакте": r"VK:\s*(.+)",
        "Одноклассники": r"OK:\s*(.+)",
        "TikTok": r"TT:\s*(.+)",
        "Instagram": r"Insta:\s*(.+)",
        "ФОТО": r"Фото:\s*(.+)"
    }

    parsed = {}

    for key, pattern in fields.items():
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            parsed[key] = match.group(1).strip()

    return parsed

def search_menu():
    console.clear()
    show_banner()
    console.print("\n[bold cyan]Меню поиска:[/bold cyan]")
    console.print("[1] Поиск по Telegram Username")
    console.print("[2] Поиск по Telegram ID")
    console.print("[3] Поиск по номеру телефона")
    console.print("[4] Поиск по email")
    console.print("[5] Поиск Соц. Сетей по нику")
    console.print("[0] Назад")

    choice = input("\nВыберите тип поиска: ")

    if choice == "0":
        return
    elif choice == "3":
        phone = input("\nВведите номер телефона (в формате +79991234567): ")
        if not phone.startswith("+7") and not phone.startswith("8"):
            console.print("[bold red]Формат неверен. Начинай с +7 или 8.[/bold red]")
            return
        try:
            console.print("[bold cyan]Поиск в базе...[/bold cyan]")
            result = asyncio.run(sherlock_phone_lookup(phone))
parsed = parse_bot_message(result)

if parsed:
    console.print(f"\n[bold green]Результаты для {phone}:[/bold green]")
    for key, value in parsed.items():
        console.print(f"[+] {key}: {value}")
else:
    console.print(result)
                console.print(f"\n[bold red]Ничего не найдено для {phone}.[/bold red]")
            else:
                console.print(f"\n[bold green]Результаты для {phone}:[/bold green]")
                console.print(result)
        except Exception as e:
            console.print(f"[bold red]Ошибка при запросе: {e}[/bold red]")
    else:
        console.print("\n[bold red]Неверный выбор![/bold red]")

    input("\n[Нажмите Enter, чтобы вернуться в меню...]")
    search_menu()

def main_menu():
    while True:
        show_banner()
        console.print("\n[bold cyan]Главное меню:[/bold cyan]")
        console.print("[1] Поиск")
        console.print("[2] GeoOSINT")
        console.print("[3] Снос аккаунта")
        console.print("[4] Ввод и оформление данных")
        console.print("[5] Выход")

        choice = input("\nВыберите пункт: ")

        if choice == "1":
            search_menu()
        elif choice == "2":
            console.print("\n[bold red]GeoOSINT пока не реализован.[/bold red]")
        elif choice == "3":
            console.print("\n[bold red]Снос аккаунта пока не реализован.[/bold red]")
        elif choice == "4":
            input_profile()
        elif choice == "5":
            console.print("\n[bold red]Выход из программы...[/bold red]")
            break
        else:
            console.print("[bold red]Неверный выбор![/bold red]")

        input("\n[Нажмите Enter, чтобы вернуться в меню...]")

if __name__ == "__main__":
    main_menu()
