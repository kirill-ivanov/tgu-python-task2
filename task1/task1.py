import cowsay
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

def main():
    try:
        message = input("Введите ваше сообщение: ")
        cowsay.cow(message)
        logging.info("Программа успешно выполнена")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")

if __name__ == "__main__": main()
