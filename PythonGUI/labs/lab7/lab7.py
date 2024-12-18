import FreeSimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import re

def plot_graph():
    def y_function(x):
        return  5 * np.sin(1/x) * np.cos((x**2 + 1/x)**2)

    # Створення даних
    x = np.linspace(1.01, 4, 100)
    y = y_function(x)

    # Побудова графіка
    plt.figure(figsize=(9, 7))
    plt.plot(x, y)
    plt.xlabel("$x$")
    plt.ylabel("$Y(x)$")
    plt.grid(True)
    plt.legend()
    plt.savefig("graph.png")  # Збереження графіка у файл
    plt.show()

def plot_letter_histogram():
    def letter_histogram(text, filename="letter.png"):
        # Підрахунок частоти літер
        letter_counts = {}
        for letter in text.lower():
            if letter.isalpha():
                letter_counts[letter] = letter_counts.get(letter, 0) + 1

        # Візуалізація
        plt.figure(figsize=(10, 6))
        plt.bar(letter_counts.keys(), letter_counts.values())
        plt.xlabel('Літера')
        plt.ylabel('Частота')
        plt.title('Частота появи літер')
        plt.savefig(filename)
        plt.show()

    # Приклад використання:
    text = "Це приклад тексту для аналізу частоти літер."
    letter_histogram(text)

def plot_sentence_types():
    # Текст для аналізу
    text = """
    звичайне речення. питальне? окличне! з трикрапкою... питальне? питальне? питальне? з трикрапкою... з трикрапкою...
    """

    # Розділення тексту на речення
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    types = {"звичайні": 0, "питальні": 0, "окличні": 0, "з трикрапкою": 0}

    # Аналіз типів речень
    for sentence in sentences:
        if "..." in sentence:
            types["з трикрапкою"] += 1
        elif sentence.endswith("?"):
            types["питальні"] += 1
        elif sentence.endswith("!"):
            types["окличні"] += 1
        else:
            types["звичайні"] += 1

    # Дані для гістограми
    categories = list(types.keys())
    frequencies = list(types.values())

    # Побудова гістограми
    plt.bar(categories, frequencies)
    plt.title("Частота типів речень у тексті")
    plt.xlabel("Типи речень")
    plt.ylabel("Кількість")
    plt.savefig("sentence_types_fixed.png")  # Збереження графіка
    plt.show()

def main():
    layout = [
        [sg.Text("Виберіть завдання (1-3):")],
        [sg.Button("Завдання 1"), sg.Button("Завдання 2"), sg.Button("Завдання 3")],
        [sg.Text("Результат:")],
        [sg.Multiline("", size=(60, 20), key="result", disabled=True)],
        [sg.Button("Вихід")]
    ]

    window = sg.Window("Графіки та аналізи", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вихід":
            break

        if event == "Завдання 1":
            try:
                plot_graph()  # Завдання 1
                window["result"].update("Графік функції побудовано.")
            except Exception as e:
                window["result"].update(f"Помилка: {str(e)}")

        elif event == "Завдання 2":
            try:
                plot_letter_histogram()  # Завдання 2
                window["result"].update("Гістограма частоти літер побудована.")
            except Exception as e:
                window["result"].update(f"Помилка: {str(e)}")

        elif event == "Завдання 3":
            try:
                plot_sentence_types()  # Завдання 3
                window["result"].update("Гістограма типів речень побудована.")
            except Exception as e:
                window["result"].update(f"Помилка: {str(e)}")

    window.close()

if __name__ == "__main__":
    main()
