import os
import subprocess
import FreeSimpleGUI as sg

LABS_DIR = "labs"

def get_lab_list():
    if not os.path.exists(LABS_DIR):
        return []
    return [d for d in os.listdir(LABS_DIR) if os.path.isdir(os.path.join(LABS_DIR, d))]

def get_lab_description(lab_name):
    readme_path = os.path.join(LABS_DIR, lab_name, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as file:
            return file.read()
    return "Опис відсутній."

def run_lab(lab_name):
    lab_path = os.path.join(LABS_DIR, lab_name, f"{lab_name}.py")
    if os.path.exists(lab_path):
        try:
            subprocess.Popen(["python", lab_path])
        except Exception as e:
            sg.popup_error(f"Помилка запуску лабораторної роботи: {e}", title="Помилка")
    else:
        sg.popup_error(f"Файл {lab_name}.py не знайдено!", title="Помилка")

sg.theme("Python")

lab_list = get_lab_list()

layout = [
    [sg.Listbox(values=lab_list, size=(30, 10), key="lab_list", enable_events=True)],
    [sg.Multiline("Опис лабораторної роботи буде відображено тут.", size=(50, 10), key="opus", disabled=True)],
    [sg.Button("Запустити", key="run"), sg.Button("Вихід", key="exit")]
]

window = sg.Window("Лабораторні роботи", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "exit":
        break

    if event == "lab_list":
        selected_lab = values["lab_list"]
        if selected_lab:
            description = get_lab_description(selected_lab[0])
            window["opus"].update(description)

    if event == "run":
        selected_lab = values["lab_list"]
        if selected_lab:
            run_lab(selected_lab[0])
        else:
            sg.popup_error("Виберіть лабораторну роботу перед запуском.", title="Помилка")

window.close()
