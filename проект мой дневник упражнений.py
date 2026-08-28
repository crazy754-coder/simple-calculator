print("---ВАС ПРИВЕТСТВУЕТ ПРИЛОЖЕНИЕ МОЙ ДНЕВНИК УПРАЖНЕНИЙ---")


workouts = []
while True:
    command = input("Выберите что хотите сделать? : (добавить / показать / хватит)")
    if command == "добавить":
        workouts.append(input("введите упражнение :"))
        print("Вот ваши упражнения : ", workouts)
    elif command == "показать":
        if len(workouts) == 0:
            print("В списке ничего нету.")
        if len(workouts) > 0 :
            print("Вот ваш список упражнений : ", workouts)
    elif command == "хватит" :
        print("Хорошо,приходи еще!")
        break
    else:
        print("Я не понял команду,напиши что то из списка.")

   