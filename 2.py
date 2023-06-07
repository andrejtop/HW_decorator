import os
from datetime import datetime

path = 'main.txt'

def logger(path):
    def __logger(func):
        def new_function(*args, **kwargs):
            date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            func_name = func.__name__
            result = func(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'{date_time}: вызов функции {func_name} с аргументами {args} {kwargs}\n')
                file.write(f'{date_time}: функция {func_name} вернула значение {result}\n')
            return result
        return new_function
    return __logger

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'

@logger(path)
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

if __name__ == '__main__':
    test_2()
    print(compare_str(" Python", " PYTHON", True, False))