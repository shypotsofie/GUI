import FreeSimpleGUI as sg

class EngUkrDictionary:
    def __init__(self):
        self.dictionary = {}

    def add_translation(self, eng_word, ukr_word):
        eng_word = eng_word.lower()  # Переведення слова в нижній регістр
        ukr_word = ukr_word.lower()
        if eng_word not in self.dictionary:
            self.dictionary[eng_word] = []  # Якщо слова немає, створюємо порожній список
        if ukr_word not in self.dictionary[eng_word]:
            self.dictionary[eng_word].append(ukr_word)  # Додаємо переклад, якщо його ще немає

    def get_translations(self, eng_word):
        eng_word = eng_word.lower()
        if eng_word in self.dictionary:
            return self.dictionary[eng_word]
        else:
            return f"Слово '{eng_word}' не знайдено у словнику."

    def display_all(self):
        if not self.dictionary:
            return "Словник порожній."
        else:
            result = "Англо-український словник:\n"
            for eng_word, translations in self.dictionary.items():
                result += f"{eng_word}: {', '.join(translations)}\n"
            return result

def main():
    my_dict = EngUkrDictionary()

    layout = [
        [sg.Text("Англо-український словник")],
        [sg.Button("Додати переклад"), sg.Button("Отримати переклад")],
        [sg.Button("Вивести весь словник"), sg.Button("Вийти")],
        [sg.Text("Результат:")],
        [sg.Multiline("", size=(50, 15), key="result", disabled=True)],
        [sg.Text("Англійське слово:"), sg.InputText("", key="eng_word")],
        [sg.Text("Український переклад:"), sg.InputText("", key="ukr_word")],
    ]

    window = sg.Window("Англо-український словник", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вийти":
            break

        if event == "Додати переклад":
            eng_word = values["eng_word"]
            ukr_word = values["ukr_word"]
            if eng_word and ukr_word:
                my_dict.add_translation(eng_word, ukr_word)
                window["result"].update(f"Переклад '{ukr_word}' для слова '{eng_word}' додано.")
            else:
                window["result"].update("Будь ласка, введіть англійське слово та український переклад.")

        elif event == "Отримати переклад":
            eng_word = values["eng_word"]
            if eng_word:
                translations = my_dict.get_translations(eng_word)
                if isinstance(translations, list):
                    window["result"].update(f"Переклади для слова '{eng_word}': {', '.join(translations)}")
                else:
                    window["result"].update(translations)
            else:
                window["result"].update("Будь ласка, введіть англійське слово для перекладу.")

        elif event == "Вивести весь словник":
            result = my_dict.display_all()
            window["result"].update(result)

    window.close()

if __name__ == "__main__":
    main()