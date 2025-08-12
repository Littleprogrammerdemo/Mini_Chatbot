import random
import datetime
import re

# Базови отговори и категории
responses = {
    "greeting": [
        "Здравей! Радвам се да те видя! 😊",
        "Хей! Как минава денят ти?",
        "Привет! Какво ново?",
        "Йо! Как си днес?"
    ],
    "how_are_you": [
        "Добре съм, благодаря, че питаш! А ти?",
        "Чудесно, благодаря! А при теб как е?",
        "Всичко е наред, а при теб?",
        "Аз съм просто код, но се чувствам отлично!"
    ],
    "name": [
        "Аз съм твоят Python чатбот 🤖",
        "Можеш да ме наричаш Ботито.",
        "Просто ме наричай приятел!"
    ],
    "time": [
        lambda: f"Сега е {datetime.datetime.now().strftime('%H:%M:%S')}",
        lambda: f"Часът е {datetime.datetime.now().strftime('%H:%M')}"
    ],
    "date": [
        lambda: f"Днес е {datetime.datetime.now().strftime('%d.%m.%Y')}",
        lambda: f"Датата е {datetime.datetime.now().strftime('%A, %d %B %Y')}"
    ],
    "joke": [
        "Защо програмистите не обичат природата? – Има твърде много бъгове 🐛",
        "Какво казва един бит на друг? – Бъди позитивен! 😄",
        "Програмист влиза в бар... и поръчва 1 бира, 10 бири, 111 бири...",
        "Защо компютрите никога не се уморяват? Защото имат много процесори!"
    ],
    "weather": [
        "Аз не мога да проверя времето, но дано е слънчево при теб! ☀️",
        "За прогноза използвай телефон или сайт, аз съм просто бот.",
        "Надявам се времето да е добро, където и да си!"
    ],
    "thanks": [
        "Моля, винаги съм тук да помогна!",
        "Няма за какво!",
        "Радвам се, че помогнах!"
    ],
    "bye": [
        "Чао! Приятен ден!",
        "Довиждане и до скоро!",
        "Ще се видим пак! 👋"
    ],
    "default": [
        "Ммм... интересно! Разкажи ми още.",
        "Не съм сигурен, че разбрах, но звучи любопитно!",
        "О, това е интересно! 😊",
        "Опитай с други думи, не съм много добър с всичко още."
    ]
}

# Функция за разпознаване на ключови думи и шаблони
def get_response(user_input):
    user_input = user_input.lower()

    # Поздрави
    if re.search(r"\b(здравей|привет|хей|йо)\b", user_input):
        return random.choice(responses["greeting"])

    # Как си
    if re.search(r"\b(как си|как се чувстваш|какво правиш)\b", user_input):
        return random.choice(responses["how_are_you"])

    # Име
    if re.search(r"\b(име|как се казваш)\b", user_input):
        return random.choice(responses["name"])

    # Час/време
    if re.search(r"\b(час|време|кога е)\b", user_input):
        return random.choice(responses["time"])()

    # Дата/ден
    if re.search(r"\b(дата|ден|кой ден е)\b", user_input):
        return random.choice(responses["date"])()

    # Шега
    if re.search(r"\b(шега|виц|смешно|смях)\b", user_input):
        return random.choice(responses["joke"])

    # Време (понеже много хора питат)
    if re.search(r"\b(времето|какво е времето|прогноза)\b", user_input):
        return random.choice(responses["weather"])

    # Благодарности
    if re.search(r"\b(благодаря|мерси|благодя)\b", user_input):
        return random.choice(responses["thanks"])

    # Сбогуване
    if re.search(r"\b(чао|сбогом|довиждане|изход|прекрати)\b", user_input):
        return random.choice(responses["bye"])

    # Числови изрази и смятане (минимално)
    calc_match = re.search(r"(\d+)\s*([\+\-\*\/])\s*(\d+)", user_input)
    if calc_match:
        num1, op, num2 = calc_match.groups()
        num1, num2 = int(num1), int(num2)
        try:
            if op == '+':
                return f"Резултатът е {num1 + num2}"
            elif op == '-':
                return f"Резултатът е {num1 - num2}"
            elif op == '*':
                return f"Резултатът е {num1 * num2}"
            elif op == '/':
                return f"Резултатът е {num1 / num2:.2f}"
        except Exception:
            return "Имаше проблем със сметките."

    # Ако не разбира нищо конкретно
    return random.choice(responses["default"])

def main():
    print("🤖 Super Smart Python ChatBot — напиши 'чао' за изход")
    while True:
        user_text = input("Ти: ").strip()
        if re.search(r"\b(чао|сбогом|довиждане|изход|прекрати)\b", user_text.lower()):
            print("Бот:", random.choice(responses["bye"]))
            break
        print("Бот:", get_response(user_text))

if __name__ == "__main__":
    main()
