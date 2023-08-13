"""Вам необходимо реализовать функцию duplicate(), которая должна принимать в качестве аргумента список и удваивать этот список "по месту".Вам нужно будет изменять исходный объект списка. Помним, список передается по ссылке. Удваивание здесь означает, что после применения к нему функции список должен иметь копию всех элементов, добавленную в конец как в примере ниже.
"""

# BEGIN (write your solution here)
def duplicate(items):
    items *= 2
# END

# def duplicate(items):   ---> solution
#     items.extend(items)

# def duplicate(items): ---> extend
#     for n in items[:]:
#         items.append(n)


items = [1, 2]
duplicate(items)  # ничего не возвращается!
print(items)  # => [1, 2, 1, 2]"""
