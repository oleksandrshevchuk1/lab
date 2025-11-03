import time
from functools import wraps

_cache = {}


def cache_with_ttl(ttl_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Ключ кешу — це аргументи функції
            key = (args, tuple(kwargs.items()))

            # Перевіряємо чи є результат у кеші та чи не протермінований
            if key in _cache:
                result, timestamp = _cache[key]
                if time.time() - timestamp < ttl_seconds:
                    print("Використовуємо кеш")
                    return result
                else:
                    print("Кеш протермінований")

            result = func(*args, **kwargs)
            _cache[key] = (result, time.time())
            print("Зберегли результат у кеш")
            return result

        return wrapper

    return decorator
