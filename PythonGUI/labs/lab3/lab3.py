import os
import FreeSimpleGUI as sg

def write_to_file(group_name, student_name, average_grade):
    file_name = f"{group_name}.txt"
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"{student_name},{average_grade}\n")
    return f"Дані записано до файлу {file_name}."

def read_file(group_name):
    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        return f"Файл {file_name} не існує."

def search_in_file(group_name, student_name):
    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            found = False
            for line in file:
                name, grade = line.strip().split(',')
                if name == student_name:
                    found = True
                    return f"Знайдено: {name} - {grade}"
            if not found:
                return f"Студента {student_name} не знайдено в файлі {file_name}."
    else:
        return f"Файл {file_name} не існує."

def sort_file_by_grade(group_name):
    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            students = [line.strip().split(',') for line in file]
        students.sort(key=lambda x: float(x[1]), reverse=True)
        with open(file_name, 'w', encoding='utf-8') as file:
            for name, grade in students:
                file.write(f"{name},{grade}\n")
        return f"Файл {file_name} відсортовано за середнім балом."
    else:
        return f"Файл {file_name} не існує."

def list_files():
    files = [f for f in os.listdir() if f.endswith('.txt')]
    if files:
        return "\n".join(files)
    else:
        return "Файлів не знайдено."

def main():
    layout = [
        [sg.Text("Меню:")],
        [sg.Button("Додати студента"), sg.Button("Переглянути дані групи")],
        [sg.Button("Знайти студента в групі"), sg.Button("Відсортувати дані групи за середнім балом")],
        [sg.Button("Показати всі файли"), sg.Button("Вийти")],
        [sg.Text("Результат:")],
        [sg.Multiline("", size=(50, 15), key="result", disabled=True)],
        [sg.Text("Група:"), sg.InputText("", key="group_name")],
        [sg.Text("Ім'я студента:"), sg.InputText("", key="student_name")],
        [sg.Text("Середній бал:"), sg.InputText("", key="average_grade")]
    ]

    window = sg.Window("Управління студентськими файлами", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вийти":
            break

        result = ""
        if event == "Додати студента":
            group = values["group_name"]
            name = values["student_name"]
            grade = values["average_grade"]
            if group and name and grade:
                result = write_to_file(group, name, grade)
            else:
                result = "Будь ласка, введіть всі дані (групу, ім'я студента, середній бал)."

        elif event == "Переглянути дані групи":
            group = values["group_name"]
            if group:
                result = read_file(group)
            else:
                result = "Будь ласка, введіть назву групи."

        elif event == "Знайти студента в групі":
            group = values["group_name"]
            name = values["student_name"]
            if group and name:
                result = search_in_file(group, name)
            else:
                result = "Будь ласка, введіть назву групи та ім'я студента."

        elif event == "Відсортувати дані групи за середнім балом":
            group = values["group_name"]
            if group:
                result = sort_file_by_grade(group)
            else:
                result = "Будь ласка, введіть назву групи."

        elif event == "Показати всі файли":
            result = list_files()

        window["result"].update(result)

    window.close()

if __name__ == "__main__":
    main()