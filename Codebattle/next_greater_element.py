"""Дан массив, верните 'следующий больший элемент для каждого элемента.
'Следующий больший элемент' для элемента x - это первый наибольший элемент в
массиве справа от x. Для элементов, у которых нет большего элемента справа,
'следующий больший элемент' считать равным -1."""


def solution(integers: list[int]) -> list[int]:
    result = []
    for i, elem in enumerate(integers):
        for next_elem in integers[i:]:
            if next_elem > elem:
                result.append(next_elem)
                break
            if next_elem == integers[-1]:
                result.append(-1)
    return result






print(solution([13, 7, 6, 12]))  # [-1, 12, 12, -1]
print(solution([4, 5, 2, 25]))  # [5, 25, 25, -1]
print(solution([3, 6, 8, 2, 1, 5, 12, 4, 9]))  # [6, 8, 12, 5, 5, 12, -1, 9, -1]
print(solution([3, 1, 2, 4]))  # [4, 2, 4, -1]
