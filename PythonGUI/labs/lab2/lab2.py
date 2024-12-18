import FreeSimpleGUI as sg

def calculate_average(numbers):
    """Обчислює середнє арифметичне списку чисел."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def main():
    # Створення макету вікна
    layout = [
        [sg.Text("Введіть числа через пробіл:")],
        [sg.InputText(key='-INPUT-')],
        [sg.Button('Обчислити'), sg.Button('Вихід')],
        [sg.Text(size=(20, 1), key='-OUTPUT-')]
    ]

    # Створення вікна
    window = sg.Window('Обчислення середнього', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Вихід':
            break
        if event == 'Обчислити':
            try:
                numbers = list(map(float, values['-INPUT-'].split()))
                average = calculate_average(numbers)
                window['-OUTPUT-'].update(f"Середнє значення: {average}")
            except ValueError:
                window['-OUTPUT-'].update("Помилка: введіть лише числові значення, розділені пробілами.")

    window.close()

if __name__ == "__main__":
    main()