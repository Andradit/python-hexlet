"""Вам дан класс Counter, реализующий счетчик с инкрементом и декрементом. Вам
нужно реализовать класс-потомок LimitedCounter, который будет отличаться от
Counter тем, что при инициализации будет принимать в качестве аргумента лимит —
максимальное возможное значение счетчика.

Требования к классу LimitedCounter:

    - класс должен максимально использовать методы предка, если таковые
    переопределяет;
    - минимальное значение счетчика Counter — 0, должно оставаться таковым и для
    LimitedCounter"""

# counter = LimitedCounter(limit=10)
# counter.inc()
# counter.inc(7)
# counter.value  # 8
# counter.dec(10)
# counter.value  # 0
# counter.inc(7)
# counter.inc(7)
# counter.value  # 10

"""Подсказки
Задание можно решить разными способами. Нет единственного верного решения. Так
что творите!"""


class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


# BEGIN (write your solution here)
class LimitedCounter(Counter):
    def __init__(self, limit=0):
        super().__init__()
        self.limit = limit

    def inc(self, amount=1):
        super().inc(amount)
        if self.value > self.limit:
            self.value = self.limit

    def dec(self, amount=1):
        super().dec(amount)


# END

counter = LimitedCounter(limit=10)
print(counter.value)
counter.inc()
counter.inc(7)
print(counter.value)  # 8
counter.dec(10)
print(counter.value)  # 0
counter.inc(7)
counter.inc(7)
print(counter.value)  # 10


"SOLUTION"

# BEGIN

"""Решение основано на замене атрибута value на свойство, setter которого
ограничивает значение счетчика. Такой подход позволяет сохранить свойства класса 
даже если пользователь будет менять значение счетчика через присваивание
напрямую атрибуту value.

Если вы просто унаследуете Counter и переопределите метод inc, то такое решение
тоже будет правильным. Данное решение нарочно демонстрирует альтернативный
подход :)"""

# class LimitedCounter(Counter):
"""A counter with limited maximal value."""
#     def __init__(self, limit):
"""Initialize a new counter with some limit."""
#         self.limit = limit
"""Свойство должно где-то хранить фактическое значение счетчика, для чего
вводится "скрытый" ("приватный") атрибут _actual_value:"""
#         self._actual_value = 0
"""Инициализация методом родителя делается в конце, потому что предок уже в
__init__ присваивает атрибуту value значение 0. А это значит, что будет вызван
setter, который использует атрибуты limit и _actual_value."""
#         super().__init__()
#
#     @property
#     def value(self):
#         return self._actual_value
#
#     @value.setter
#     def value(self, new_value):
#         self._actual_value = min(max(new_value, 0), self.limit)
# END