"""# Реализуйте функцию get_range(), которая для заданного положительного
числа аргумента n должна возвращать список чисел от нуля до n, не включая само
число n. Если при вызове было передано отрицательное число или ноль, функция
должна возвращать пустой список.

# Для решения используйте цикл while и метод списка append."""


# BEGIN (write your solution here)
def get_range(n):
    if n <= 0:
        return []
    i = 0
    result = []
    while i < n:
        result.append(i)
        i += 1
    return result
# END


print(get_range(7))
