import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import FreeSimpleGUI as sg

def analyze_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
    except requests.exceptions.RequestException as e:
        return f"Не вдалося отримати сторінку: {e}"

    soup = BeautifulSoup(html_content, 'html.parser')

    text = soup.get_text()
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)

    result = "Частота появи слів у тексті новини:\n"
    for word, count in word_counts.most_common(10):
        result += f"{word}: {count}\n"

    tags = [tag.name for tag in soup.find_all()]
    tag_counts = Counter(tags)

    result += "\nЧастота появи HTML-тегів:\n"
    for tag, count in tag_counts.most_common(10):
        result += f"<{tag}>: {count}\n"

    links = soup.find_all('a')
    result += f"\nКількість посилань на сторінці: {len(links)}\n"

    images = soup.find_all('img')
    result += f"Кількість зображень на сторінці: {len(images)}\n"

    return result

def main():
    layout = [
        [sg.Text("Введіть URL сторінки новин для аналізу:")],
        [sg.InputText(key="url")],
        [sg.Button("Аналізувати")],
        [sg.Text("Результат:")],
        [sg.Multiline("", size=(60, 20), key="result", disabled=True)],
        [sg.Button("Вихід")]
    ]

    window = sg.Window("Аналіз веб-сторінки", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вихід":
            break

        if event == "Аналізувати":
            url = values["url"]
            if url:
                result = analyze_webpage(url)
                window["result"].update(result)
            else:
                sg.popup_error("Будь ласка, введіть URL сторінки.")

    window.close()

if __name__ == "__main__":
    main()
