from datetime import datetime

def logger_with_path(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            func_name = func.__name__
            result = func(*args, **kwargs)
            with open(path, 'a') as f:
                f.write(f'{date_time}: вызов функции {func_name} с аргументами {args} {kwargs}\n')
                f.write(f'{date_time}: функция {func_name} вернула значение {result}\n')
            return result
        return wrapper
    return decorator
