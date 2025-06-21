"""Реализуйте класс HourClock, который будет изображать часы с одной лишь
часовой стрелкой. Текущее время (час) должно сообщать свойство hours. Это же
свойство должно позволять изменять положение часовой стрелки (посредством
сеттера). При изменении положения стрелки нужно контролировать, чтобы значение
оставалось в диапазоне 0..11 (часов)."""

# clock = HourClock()
# clock.hours  # 0
# # в начале часовая стрелка всегда на нуле
# clock.hours += 5
# # ^ эквивалентно clock.hours = clock.hours + 5
# clock.hours += 5
# clock.hours  # 10
# clock.hours += 5
# clock.hours  # 3
# clock.hours -= 4
# clock.hours  # 11
# clock.hours = 123
# clock.hours  # 3

"""Подсказки
Используйте модульную арифметику"""


class HourClock:
    def __init__(self):
        self.position = 0

    @property
    def hours(self):
        return self.position

    @hours.setter
    def hours(self, new_position):
        self.position = new_position % 12


clock = HourClock()
print(clock.__dict__)
print(clock.hours)  # 0
# в начале часовая стрелка всегда на нуле
clock.hours += 5
# ^ эквивалентно clock.hours = clock.hours + 5
clock.hours += 5
print(clock.hours)  # 10
clock.hours += 5
print(clock.hours)  # 3
clock.hours -= 4
print(clock.hours)  # 11
clock.hours = 123
print(clock.hours)  # 3
