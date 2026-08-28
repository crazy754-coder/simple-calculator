print("---КАЛЬКУЛЯТОР---")

def show_menu():
    print("1. Сложить")
    print("2. Вычесть")
    print("3. Умножить")
    print("4. Разделить")
    print("5. Выход")

def stac():
    a = int(input("Введите 1 число для сложения : "))
    b = int(input("Введите 2 число для сложения : "))
    return a + b

def subtraction():
    a = int(input("Введите 1 число для вычитания : "))
    b = int(input("Введите 2 число для вычитания : "))
    return a - b

def multiply():
    a = int(input("Введите 1 число для умножения : "))
    b = int(input("Введите 2 число для умножения : "))
    return a * b

def division():
    a = int(input("Введите 1 число для деления : "))
    b = int(input("Введите 2 число для деления : "))
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def main():
    while True:
        show_menu()
        choice = input("Введите что хотите сделать (1-5): ")
        
        if choice == "1":
            result = stac()
            print(f"Результат: {result}")
        elif choice == "2":
            result = subtraction()
            print(f"Результат: {result}")
        elif choice == "3":
            result = multiply()
            print(f"Результат: {result}")
        elif choice == "4":
            result = division()
            print(f"Результат: {result}")
        elif choice == "5":
            print("Вы вышли из калькулятора.")
            break  # Выход из программы
        else:
            print("Не понял ваш запрос, попробуйте снова.")

if __name__ == "__main__":
    main()