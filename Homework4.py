def find_min_max(arr):
    """
    Возвращает пару значений — минимальное и максимальное значение в массиве.
    
    :param arr: Входной массив целых чисел.
    :return: Кортеж (min_value, max_value) или None, если массив пуст.
    """
    if not arr:
        return None  # Возвращаем None для пустого массива
    
    # Инициализируем минимальное и максимальное значения первым элементом массива
    min_value = max_value = arr[0]
    
    # Переберите остальные элементы массива для поиска минимального и максимального
    for num in arr[1:]:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num
    
    # Возвращаем кортеж с минимальным и максимальным значениями
    return min_value, max_value

# Пример использования
print(find_min_max([1, 5, 8, 3, 10]))  # Выводит: (1, 10)
print(find_min_max([]))  # Выводит: None

# Альтернативная реализация с помощью встроенных функций min() и max()
def find_min_max_alt(arr):
    if not arr:
        return None  # Возвращаем None для пустого массива
    return min(arr), max(arr)

# Пример использования альтернативной реализации
print(find_min_max_alt([1, 5, 8, 3, 10]))  # Выводит: (1, 10)
print(find_min_max_alt([]))  # Выводит: None
