import json
import os

# ==== ФАЙЛИ ====
GAME_STATS_FILE = "game_stats.json"
CONTACTS_FILE = "contacts.json"
CLIENTS_FILE = "clients.json"

# ==== ДОПОМІЖНІ ФУНКЦІЇ ====
def load_json(file_path, default):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return default

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# ==== 1. СТАТИСТИКА ГРИ ====
def update_game_stats():
    name = input("Ім'я гравця: ")
    result = input("Результат (win/loss): ").strip().lower()
    stats = load_json(GAME_STATS_FILE, {})
    if name not in stats:
        stats[name] = {"wins": 0, "losses": 0}
    if result == "win":
        stats[name]["wins"] += 1
    elif result == "loss":
        stats[name]["losses"] += 1
    else:
        print("Невідомий результат.")
        return
    save_json(GAME_STATS_FILE, stats)
    print("Оновлено!")

# ==== 2. КОНТАКТИ ====
def add_contact():
    name = input("Ім'я контакту: ")
    phone = input("Номер телефону: ")
    contacts = load_json(CONTACTS_FILE, {})
    contacts[name] = phone
    save_json(CONTACTS_FILE, contacts)
    print("Контакт збережено.")

def view_contacts():
    contacts = load_json(CONTACTS_FILE, {})
    if not contacts:
        print("Контактів не знайдено.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# ==== 3. КЛІЄНТИ ====
def add_client():
    name = input("Ім'я клієнта: ")
    email = input("Email клієнта: ")
    clients = load_json(CLIENTS_FILE, [])
    clients.append({"name": name, "email": email})
    save_json(CLIENTS_FILE, clients)
    print("Клієнт доданий.")

def search_client():
    name = input("Введіть ім'я для пошуку: ")
    clients = load_json(CLIENTS_FILE, [])
    found = [c for c in clients if c["name"].lower() == name.lower()]
    for client in found:
        print(client)
    if not found:
        print("Клієнта не знайдено.")

def update_client():
    name = input("Ім'я клієнта: ")
    new_email = input("Новий email: ")
    clients = load_json(CLIENTS_FILE, [])
    for c in clients:
        if c["name"].lower() == name.lower():
            c["email"] = new_email
            print("Оновлено.")
    save_json(CLIENTS_FILE, clients)

def delete_client():
    name = input("Ім'я для видалення: ")
    clients = load_json(CLIENTS_FILE, [])
    clients = [c for c in clients if c["name"].lower() != name.lower()]
    save_json(CLIENTS_FILE, clients)
    print("Клієнта видалено.")

# ==== МЕНЮ ====
def main_menu():
    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Оновити статистику гри")
        print("2. Додати контакт")
        print("3. Переглянути контакти")
        print("4. Додати клієнта")
        print("5. Знайти клієнта")
        print("6. Оновити клієнта")
        print("7. Видалити клієнта")
        print("0. Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            update_game_stats()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            view_contacts()
        elif choice == "4":
            add_client()
        elif choice == "5":
            search_client()
        elif choice == "6":
            update_client()
        elif choice == "7":
            delete_client()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main_menu()
