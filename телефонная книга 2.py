def show_menu():
    print("\n--- Телефонная книга (словари) ---")
    print("1. Добавить контакт")
    print("2. Показать все контакты")
    print("3. Найти контакт")
    print("4. Выйти")
    print("5. Удалить контакт")

def add_contact(book):
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    contact = {
        "name": name,
        "phone": phone
    }
    book.append(contact)
    print("✅ Контакт добавлен!")

def show_contacts(book):
    if len(book) == 0:
        print("📭 Список контактов пуст.")
    else:
        print("\n📋 Ваши контакты:")
        for contact in book:
            print(f" - {contact['name']}: {contact['phone']}")

def find_contact(book):
    search_name = input("Введите имя для поиска: ")
    found = False
    for contact in book:
        if contact["name"] == search_name:
            print(f"📞 Найден: {contact['name']} — {contact['phone']}")
            found = True
    if not found:
        print("❌ Контакт не найден.")

def delete_contact(book):
    search_name = input("Введите имя для удаления: ")
    found = False
    for contact in book:
        if contact["name"] == search_name:
            book.remove(contact)
            print("🗑️ Контакт удалён!")
            found = True
            break
    if not found:
        print("❌ Контакт не найден.")

def main():
    phone_book = []
    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ")
        if choice == "1":
            add_contact(phone_book)
        elif choice == "2":
            show_contacts(phone_book)
        elif choice == "3":
            find_contact(phone_book)
        elif choice == "4":
            print("👋 До свидания!")
            break
        elif choice == "5":
            delete_contact(phone_book)
        else:
            print("❌ Неверный ввод")

if __name__ == "__main__":
    main()