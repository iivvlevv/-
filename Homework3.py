def filter_greater_than(arr, threshold):
    """
    Возвращает новый массив, содержащий только те элементы из arr, которые больше threshold.
    
    :param arr: Входной массив целых чисел.
    :param threshold: Пороговое значение.
    :return: Новый массив с элементами, превышающими threshold.
    """
    # Создаем пустой список для хранения результатов
    result = []
    
    # Переберите элементы массива и добавьте в результат те, которые больше threshold
    for num in arr:
        if num > threshold:
            result.append(num)
    
    # Возвращаем результирующий массив
    return result

# Пример использования
print(filter_greater_than([1, 5, 8, 3, 10], 5))  # Выводит: [8, 10]

# Альтернативная реализация с помощью list comprehension
def filter_greater_than_alt(arr, threshold):
    return [num for num in arr if num > threshold]

# Пример использования альтернативной реализации
print(filter_greater_than_alt([1, 5, 8, 3, 10], 5))  # Выводит: [8, 10]
