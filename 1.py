from datetime import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        func_name = func.__name__
        result = func(*args, **kwargs)
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f'{date_time}: вызов функции {func_name} с аргументами {args} {kwargs}\n')
            file.write(f'{date_time}: функция {func_name} вернула значение {result}\n')
        return result
    return wrapper


@logger
def compare_str(s1, s2, reg=False, trim=True):
    """
    сравнение строки в разных режимах: с учетом и без учета регистра,
     а также учитывать или не учитывать пробелы вначале и в конце.
    :param s1:
    :param s2:
    :param reg: с учетом регистра
    :param trim: с удалением пробелов
    :return:
    """
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()

    return s1 == s2

print(compare_str(" Python", " PYTHON", True, False))