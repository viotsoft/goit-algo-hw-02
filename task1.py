from queue import Queue
import time
import random

# Створення черги заявок
request_queue = Queue()

# Генеруємо нову заявку з унікальним ідентифікатором


def generate_request():
    request_id = int(time.time() * 1000)
    new_request = {"id": request_id, "timestamp": time.time()}

# Додаємо заявку до черги
    request_queue.put(new_request)
    print(f"Заявка {request_id} додана до черги")

 # Виймаємо одну заявку з черги


def process_request():
    if not request_queue.empty():
        # Виймаємо одну заявку з черги
        current_request = request_queue.get()
        # Імітуємо обробку заявки
        print(f"Обробка заявки {current_request['id']}...")
        time.sleep(1)
        print(f"Заявка {current_request['id']} оброблена.")
    else:
        print("Черга порожня. Немаэ заявок для обробки")


def main_loop():
    # Для демонстрації обмежимо кількість ітерацій цикла
    for _ in range(5):

        # Генеруємо випадкову кількість нових заявок за ітерацію (0-2)
        for _ in range(random.randint(0, 2)):
            generate_request()

        # Обробляємо одну заявку за ітерацію
        process_request()

        # Невелика затримка перед наступною ітерацією
        time.sleep(2)


if __name__ == "__main__":
    main_loop()

# Для зупинки черги виконайте Ctrl + C