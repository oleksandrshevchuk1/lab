students_spusok= {}
while True:
    print("Виберіть дію:")
    print("1.Додати нового студента")
    print("2.Вивести журнал студентів")
    print("3.Вивести середній бал студентів")
    print("4.Вивести категорії студентів за оцінками")
    print("Щоб вийти з програми введіть (stop)")
    vubir = input("введіть дію:")
    if vubir == "1":
        name = input("Введіть ім'я студента: ")
        mark = int(input("Введіть оцінку студента: "))
        if mark < 1 or mark > 12:
            print("Такої оцінки не існує")
        else:
            students_spusok[name] = mark
    elif vubir == "2":
        if not students_spusok:
            print("Список студентів порожній.")
        else:
            print("Список успішності студентів:")
            for name, mark in students_spusok.items():
                print(f"{name}: {mark}")
    elif vubir == "3":
        if not students_spusok:
            print("Список студентів порожній.")
        else:
            ball = sum(students_spusok.values()) / len(students_spusok)
            print(f"Середній бал серед студентів - {ball}")
    elif vubir == "4":
        if not students_spusok:
            print("Список студентів порожній.")
        else:
            excellent = []
            good = []
            struggling = []
            failed = []
            for name in students_spusok:
                mark = students_spusok[name]
                if 10 <= mark <= 12:
                    excellent.append(name)
                elif 7 <= mark <= 9:
                    good.append(name)
                elif 4 <= mark <= 6:
                    struggling.append(name)
                elif 1 <= mark <= 3:
                    failed.append(name)
            print(f"Відмінники (10-12): {len(excellent)} ( {', '.join(excellent)})")
            print(f"Хорошисти (7-9): {len(good)} ( {', '.join(good)})")
            print(f"Відстаючі (4-6): {len( struggling)} ( {', '.join( struggling) })")
            print(f"Не здали (1-3): {len(failed)} ({', '.join(failed) })")
    elif vubir() == "stop":
        print("Дякую що відвідали нашу програму")
        break
    else:
        print("Ви ввели неправильну дію. Спробуйте ще раз")
