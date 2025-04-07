class Stack:
    def __init__(self, size=10):
        """
        Инициализация стека с фиксированным размером.

        :param size: Размер стека. По умолчанию — 10 элементов.
        """
        self.size = size
        self.stack = [None] * size  # Инициализация массива с None значениями
        self.top_index = -1  # Индекс вершины стека

    def push(self, value):
        """
        Добавление элемента в стек.

        :param value: Значение, которое нужно добавить.
        :raises IndexError: Если стек переполнен.
        """
        if self.top_index == self.size - 1:
            raise IndexError("Стек переполнен. Невозможно добавить элемент.")
        self.top_index += 1
        self.stack[self.top_index] = value

    def pop(self):
        """
        Удаление элемента из стека и возвращение его значения.

        :return: Значение удаленного элемента.
        :raises IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Стек пуст. Невозможно удалить элемент.")
        value = self.stack[self.top_index]
        self.stack[self.top_index] = None
        self.top_index -= 1
        return value

    def top(self):
        """
        Возвращение элемента на вершине стека без удаления.

        :return: Значение элемента на вершине стека.
        :raises IndexError: Если стек пуст.
        """
        if self.is_empty():
            raise IndexError("Стек пуст. Нет элемента на вершине.")
        return self.stack[self.top_index]

    def is_empty(self):
        """
        Проверка, пуст ли стек.

        :return: True, если стек пуст; False иначе.
        """
        return self.top_index == -1


# Пример использования
if __name__ == "__main__":
    stack = Stack()

    # Добавление элементов
    for i in range(5):
        stack.push(i)
        print(f"Добавлен элемент: {i}")

    # Проверка вершины стека
    print(f"Элемент на вершине: {stack.top()}")

    # Удаление элементов
    while not stack.is_empty():
        print(f"Удален элемент: {stack.pop()}")

    # Попытка удаления из пустого стека
    try:
        stack.pop()
    except IndexError as e:
        print(f"Ошибка: {e}")
