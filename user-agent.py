import random

def generate_user_agent():
    # Список версий браузеров
    versions = [
        "5.0",
        "4.0",
        "3.0",
        "2.0",
        "1.0"
    ]
    # Список платформ
    platforms = [
        "Windows NT 10.0",
        "Windows NT 6.3",
        "Windows NT 6.2",
        "Windows NT 6.1",
        "Windows NT 6.0",
        "Windows NT 5.1",
        "Windows NT 5.0",
        "Macintosh; Intel Mac OS X 10_15_7",
        "Macintosh; Intel Mac OS X 10_14_6",
        "Macintosh; Intel Mac OS X 10_13_6",
        "Macintosh; Intel Mac OS X 10_12_6",
        "Macintosh; Intel Mac OS X 10_11_6",
        "Macintosh; Intel Mac OS X 10_10_5",
        "Macintosh; Intel Mac OS X 10_9_5",
        "Macintosh; Intel Mac OS X 10_8_5",
        "Macintosh; Intel Mac OS X 10_7_5",
        "Macintosh; Intel Mac OS X 10_6_8",
        "Macintosh; Intel Mac OS X 10_5_8",
        "X11; Linux x86_64",
        "X11; Linux i686",
        "X11; FreeBSD amd64",
        "X11; FreeBSD i386",
        "X11; OpenBSD amd64",
        "X11; OpenBSD i386",
        "X11; NetBSD amd64",
        "X11; NetBSD i386",
        "X11; Linux armv7l",
        "X11; Linux armv8l",
    ]
    # Список браузеров
    browsers = [
        "Chrome",
        "Firefox",
        "Safari",
        "Opera",
        "Edge",
        "Internet Explorer"
    ]
    # Случайный выбор версии, платформы и браузера
    version = random.choice(versions)
    platform = random.choice(platforms)
    browser = random.choice(browsers)
    # Генерация пользовательского агента
    user_agent = f"Mozilla/{version} ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version}"
    return user_agent

# Пример использования
user_agent = generate_user_agent()
print("Сгенерированный пользовательский агент:", user_agent)
