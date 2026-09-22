from input_handlers import input_patient


MENU = """
=== Меню ===
1. Добавить пациента
2. Просмотреть всех пациентов
0. Выход
"""


def show_patients(patients: list) -> None:
    if not patients:
        print("\nСписок пациентов пуст.")
        return

    print(f"\nВсего пациентов: {len(patients)}\n")

    i = 1
    for patient in patients:
        print(f"--- Пациент #{i} ---")
        print(patient)
        print()
        i += 1


def main():
    patients = []

    while True:
        print(MENU)
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            try:
                patient = input_patient()
                patients.append(patient)
                print("\nПациент добавлен.")
            except ValueError as error:
                print(f"\nОшибка: {error}")

        elif choice == "2":
            show_patients(patients)

        elif choice == "0":
            print("Выход.")
            break

        else:
            print("\nНеверный пункт меню.")


if __name__ == "__main__":
    main()