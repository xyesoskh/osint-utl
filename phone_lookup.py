# phone_lookup.py

import subprocess
import csv

def scan_phoneinfoga(phone: str) -> str:
    try:
        result = subprocess.run(["phoneinfoga", "scan", "-n", phone], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"[PhoneInfoga] Ошибка: {e}"

def search_local_csv(phone: str, filename="phones.csv") -> list:
    results = []
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if phone in row.get("phone", ""):
                    results.append(row)
    except FileNotFoundError:
        results.append({"error": "Локальная база не найдена."})
    return results
