from collections import deque


def is_palindrome(input_string: str) -> bool:
    # Видаляємо пробіли та приводимо до нижнього регістру
    filtered_string = "".join(input_string.split()).lower()

    # Створюємо deque
    char_deque = deque(filtered_string)

    # Порівнюємо символи з двох сторін deque
    while len(char_deque) > 1:

        # Виймаємо символ зліва та справа
        left_char = char_deque.popleft()
        right_char = char_deque.pop()

        # Якщо символи не співпадають - це не паліндром
        if left_char != right_char:
            return False

    # Якщо ми вийшли з циклу без невідповідностей, це паліндром
    return True

# Приклади використання:
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Madam"))
print(is_palindrome("Hello"))
print(is_palindrome("Was it a car or a cat I saw"))
