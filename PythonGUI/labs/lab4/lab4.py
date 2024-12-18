import random
import FreeSimpleGUI as sg

def task1():
    words1 = ["Amazing", "Incredible", "Beautiful", "Wonderful", "Famous"]
    words2 = ["day", "evening", "moment", "time", "space"]
    words3 = ["is coming", "is approaching", "is starting", "is ending", "is continuing"]

    def generate_phrase():
        first_word = random.choice(words1)
        second_word = random.choice(words2)
        third_word = random.choice(words3)
        return f"{first_word} {second_word} {third_word}"

    random_phrase = generate_phrase()
    return f"Згенерована фраза: {random_phrase}"

def task2():
    file_path = "book.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            characters_with_spaces = len(text)
            characters_without_spaces = len(text.replace(" ", ""))
            return (f"Кількість символів з пробілами: {characters_with_spaces}\n"
                    f"Кількість символів без пробілів: {characters_without_spaces}")
    except FileNotFoundError as e:
        return f"Помилка: файл не знайдено. Шлях: {e.filename}"
    except Exception as e:
        return f"Сталася непередбачена помилка: {e}"

def task3():
    def sentence_analysis(text):
        sentences = text.split('. ') + text.split('! ') + text.split('? ') + text.split('… ')
        total_sentences = len(sentences)
        exclamatory_sentences = text.count('!')
        question_sentences = text.count('?')
        ellipsis_sentences = text.count('…')
        return (f"Загальна кількість речень: {total_sentences}\n"
                f"Кількість окличних речень: {exclamatory_sentences}\n"
                f"Кількість питальних речень: {question_sentences}\n"
                f"Кількість речень з трикрапкою: {ellipsis_sentences}")

    text = "Привіт! Як справи? Це приклад тексту... Він містить різні типи речень! Ще одне речення?"
    return sentence_analysis(text)

def main():
    layout = [
        [sg.Text("Виберіть завдання для виконання:")],
        [sg.Button("Завдання 1"), sg.Button("Завдання 2"), sg.Button("Завдання 3")],
        [sg.Text("Результат:")],
        [sg.Multiline("", size=(60, 20), key="result", disabled=True)],
        [sg.Button("Вихід")]
    ]

    window = sg.Window("Вибір завдання", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вихід":
            break

        if event == "Завдання 1":
            result = task1()
            window["result"].update(result)
        elif event == "Завдання 2":
            result = task2()
            window["result"].update(result)
        elif event == "Завдання 3":
            result = task3()
            window["result"].update(result)

    window.close()

if __name__ == "__main__":
    main()