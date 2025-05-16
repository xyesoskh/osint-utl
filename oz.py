import pyfiglet
from rich.console import Console
from rich.text import Text
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetHistoryRequest
import asyncio

# Настройки для Telethon
api_id = 29459757  # Твой API ID
api_hash = '7cc969764c4de8a52169570ac20000a8'  # Твой API Hash
session_string = "1ApWapzMBu4Sbmc7c5s44pLQ22UEse-Uyc0U0xWkxcOshYoED_Fb71Sq54idI6hqSNWQVG_gCDQhnUQVAFd_fQMcbRbNWvmoqDM4uS02q-RTcvwQT3mDOGcabfPwYaPV8oXtHfNTOHHY8vukH6NP7gSUBA4itvhpGn74nC1SfngevCA_LfGpeoOtN_jZDMG_zlWtlpAHxlJl6w5zS7qIR6kwSvD-HfKBCKlHOAdgMndoFEda47mrj35Glz1v7OVgFcv2RhxKPWCOkcynMIwLDpDyCjj1k_1zr_LtAuaDgrLKJVz0h5Khj7122_7b0H2kypMDzGOp5fqATdKt5KeS3PzkawZENeH0="  # 🔁 ВСТАВЬ СЮДА ПОЛНЫЙ session_string

client = TelegramClient(StringSession(session_string), api_id, api_hash)

# Инициализация консоли
console = Console()

def show_banner():
    try:
        with open("ascii-art.txt", "r", encoding="utf-8") as f:
            ascii_art = f.read()
        console.print(Text(ascii_art, style="bold magenta"))
    except FileNotFoundError:
        console.print("ASCII арт не найден. Убедитесь, что файл ascii-art.txt находится в той же папке.", style="bold red")
    console.print("powered by ZYAMA", style="bold magenta")

def format_data(label, value):
    if value:
        return f"[+] {label}: {value}"
    return ""

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
    await client.send_message(entity=entity, message=phone)
    await asyncio.sleep(4)  # Подожди ответ
    history = await client(GetHistoryRequest(
        peer=entity,
        limit=1,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))
    return history.messages[0].message

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
            console.print("[bold cyan]Запрос к Sherlock...[/bold cyan]")
            result = asyncio.run(sherlock_phone_lookup(phone))
            if "Не найдено" in result:
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
            console.print("\n[bold red]Функция GeoOSINT пока не реализована.[/bold red]")
        elif choice == "3":
            console.print("\n[bold red]Функция Снос аккаунта пока не реализована.[/bold red]")
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
