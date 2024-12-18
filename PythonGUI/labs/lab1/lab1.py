import FreeSimpleGUI as sg


def task1():
    """
    Виконує завдання 1: арифметичні операції.
    """
    a = 2
    b = 5
    c = a + b
    g = a - b
    h = a * b
    l = a / b
    return f"Результати:\nДодавання: {c}\nВіднімання: {g}\nМноження: {h}\nДілення: {l}"


def task2(first_m, second_m_kg, second_m_g, other_kg, other_g):
    """
    Виконує завдання 2: розрахунок сумарної ваги мішків.
    """
    sum_of_8_mishkiv = (other_kg * 1000 + other_g) * 8
    first_m_gram = first_m * 1000
    second_m_full_y_gramah = second_m_kg * 1000 + second_m_g
    sum_total_gram = sum_of_8_mishkiv + first_m_gram + second_m_full_y_gramah
    return f"Сумарно в грамах: {sum_total_gram}"


def task3(total_cakes, multiplier):
    """
    Виконує завдання 3: розрахунок кількості тістечок, проданих на перерві.
    """

    def cakes_sold_first_break(total_cakes, multiplier):
        cakes_first_break = total_cakes / (7 * multiplier + 1)
        return cakes_first_break

    result = cakes_sold_first_break(total_cakes, multiplier)
    return f"На першій перерві продали {result} тістечок."


def main():
    layout = [
        [sg.Text("Виберіть завдання (1-3):")],
        [sg.Button("Завдання 1"), sg.Button("Завдання 2"), sg.Button("Завдання 3")],
        [sg.Text("Результат:")],
        [sg.Multiline("", size=(60, 10), key="result", disabled=True)],
        [sg.Button("Вихід")]
    ]

    window = sg.Window("Завдання", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вихід":
            break

        if event == "Завдання 1":
            window["result"].update(task1())

        elif event == "Завдання 2":
            # Використовуємо input для отримання значень
            layout_task2 = [
                [sg.Text("Ваги мішків:")],
                [sg.Text("Вага першого мішка (кг):"), sg.InputText(key="first_m")],
                [sg.Text("Вага другого мішка (кг):"), sg.InputText(key="second_m_kg")],
                [sg.Text("Вага другого мішка (г):"), sg.InputText(key="second_m_g")],
                [sg.Text("Вага інших мішків (кг):"), sg.InputText(key="other_kg")],
                [sg.Text("Вага інших мішків (г):"), sg.InputText(key="other_g")],
                [sg.Button("Обчислити"), sg.Button("Назад")]
            ]

            window_task2 = sg.Window("Завдання 2: Розрахунок ваги мішків", layout_task2)

            while True:
                event_task2, values_task2 = window_task2.read()

                if event_task2 == sg.WINDOW_CLOSED or event_task2 == "Назад":
                    break

                if event_task2 == "Обчислити":
                    try:
                        first_m = int(values_task2["first_m"])
                        second_m_kg = int(values_task2["second_m_kg"])
                        second_m_g = int(values_task2["second_m_g"])
                        other_kg = int(values_task2["other_kg"])
                        other_g = int(values_task2["other_g"])

                        result_task2 = task2(first_m, second_m_kg, second_m_g, other_kg, other_g)
                        window["result"].update(result_task2)
                        window_task2.close()

                    except ValueError:
                        sg.popup_error("Будь ласка, введіть числові значення.")

        elif event == "Завдання 3":
            # Використовуємо input для отримання значень
            layout_task3 = [
                [sg.Text("Введіть загальну кількість тістечок:")],
                [sg.InputText(key="total_cakes")],
                [sg.Text("Введіть у скільки разів більше тістечок продали на другій перерві:")],
                [sg.InputText(key="multiplier")],
                [sg.Button("Обчислити"), sg.Button("Назад")]
            ]

            window_task3 = sg.Window("Завдання 3: Розрахунок тістечок", layout_task3)

            while True:
                event_task3, values_task3 = window_task3.read()

                if event_task3 == sg.WINDOW_CLOSED or event_task3 == "Назад":
                    break

                if event_task3 == "Обчислити":
                    try:
                        total_cakes = int(values_task3["total_cakes"])
                        multiplier = int(values_task3["multiplier"])

                        result_task3 = task3(total_cakes, multiplier)
                        window["result"].update(result_task3)
                        window_task3.close()

                    except ValueError:
                        sg.popup_error("Будь ласка, введіть числові значення.")

    window.close()


if __name__ == "__main__":
    main()
