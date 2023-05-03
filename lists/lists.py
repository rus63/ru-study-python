class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        max_value = -999999
        replaced_list = []
        for item in input_list:
            if item > max_value:
                max_value = item
            else:
                continue
        for item in range(len(input_list)):
            if input_list[item] > 0:
                replaced_list.append(max_value)
            else:
                replaced_list.append(input_list[item])
        return replaced_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        def binary_search(input_list: list[int], left: int, right: int, query: int) -> int:
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if query == input_list[mid]:
                return mid
            if query < input_list[mid]:
                return binary_search(input_list, left, right - 1, query)
            else:
                return binary_search(input_list, mid + 1, right, query)

        return binary_search(input_list, 0, len(input_list) - 1, query)
