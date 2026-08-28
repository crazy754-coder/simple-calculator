def menu():
    print("---Проверю ваше число---")
    print("1. Делится ли число на 2?")
    print("2. Делится ли число на 4?")
    print("3. Делится ли число на 6?")
    print("4. Делится ли число на 8?")
    print("5. Выход")

def chislo1():
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print("Число делится на 2!")
    else:
        print("Число не делится на 2!")

def chislo2():
    number = int(input("Введите число: "))
    if number % 4 == 0:
        print("Число делится на 4!")
    else:
        print("Число не делится на 4!")

def chislo3():
    number = int(input("Введите число: "))
    if number % 6 == 0:
        print("Число делится на 6!")
    else:
        print("Число не делится на 6!")

def chislo4():
    number = int(input("Введите число: "))
    if number % 8 == 0:
        print("Число делится на 8!")
    else:
        print("Число не делится на 8!")

def main():
    while True:
        menu()
        choice = input("Выберите пункт меню: ")  # Добавлен input для выбора
        
        if choice == "1":
            chislo1()
        elif choice == "2":
            chislo2()
        elif choice == "3":
            chislo3()
        elif choice == "4":
            chislo4()
        elif choice == "5":
            print("Выход")
            break
        else:
            print("Выберите из списка.")

if __name__ == "__main__":
    main()