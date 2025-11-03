from decorator.cache_decorator import cache_with_ttl
import time

# Використовуємо наш декоратор із TTL 5 секунд
@cache_with_ttl(ttl_seconds=5)
def add_numbers(a, b):
    print(f"Обчислюємо {a} + {b}")
    return a + b

# Виклики функції
print(add_numbers(2, 3))  # Перше обчислення
time.sleep(2)
print(add_numbers(2, 3))  # Використає кеш
time.sleep(5)
print(add_numbers(2, 3))  # Кеш протермінувався, обчислюємо заново

