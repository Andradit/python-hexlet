"""Сэму и Фродо надо держаться вместе. Проверить, нет ли между ними других
персонажей."""


def solution(item: list) -> bool:
    sam = "Sam"
    frodo = "Frodo"
    for index, elem in enumerate(item):
        if elem == sam and (item.index(frodo) == index + 1 or item.index(
                frodo) == index - 1):
            return True
    return False


print(True if solution(["Sam", "Frodo", "Troll", "Barlog", "Human"]) is True
      else False)
print(not solution(["Orc", "Frodo", "Treant", "Saruman", "Sam"]))
print(solution(["Orc", "Sam", "Frodo", "Gandalf", "Legolas"]))
