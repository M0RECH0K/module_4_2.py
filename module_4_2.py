def test_function():
    def inner_function():
        print(f'Я в области видимости {test_function}')

    print(inner_function())


# test_function()

try:
    inner_function()
except NameError as a:
    print(f'Ошибка! Функция находится в другом пространстве {a}')
