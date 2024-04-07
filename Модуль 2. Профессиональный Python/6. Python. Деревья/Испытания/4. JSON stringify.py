"""JavaScript содержит метод JSON.stringify() для приведения к строке любого
значения. Он работает следующим образом:"""

# JSON.stringify('hello'); // "hello" - для строковых значений добавляются кавычки
# JSON.stringify(true);    // true    - значение приведено к строке, но без кавычек
# JSON.stringify(5);       // 5
#
# const data = { hello: 'world', is: true, nested: { count: 5 } };
# JSON.stringify(data); // {"hello":"world","is":true,"nested":{"count":5}}
#
# JSON.stringify(data, null, 2); // null, 2 - указывают на два пробела перед ключом
# // ключам добавляются кавычки
# // в конце каждой строчки (линии) добавляется запятая, если имеется значение ниже
# // {
# //   "hello": "world",
# //   "is": true,
# //   "nested": {
# //     "count": 5
# //   }
# // }

"""Реализуйте функцию stringify(), похожую на JSON.stringify(), возвращающую 
строку, но со следующими отличиями:
    - ключи и строковые значения должны быть без кавычек;
    - строчка (линия) в строке заканчивается самим значением, без запятой.
    
Синтаксис:"""

# stringify(value[, replacer[, spaces_count]])

"""Параметры:

    value - значение, преобразуемое в строку;
    replacer - необязательный; строка – отступ для ключа; значение по 
    умолчанию – один пробел.
    spacesCount - необязательный; число – количество повторов отступа ключа; 
    значение по умолчанию – 1."""

# stringify('hello')  # значение приведено к строке, но не имеет кавычек
# # hello
# stringify(True)
# # True
# stringify(5)
# # 5
#
# data = {"hello": "world", "is": True, "nested": {"count": 5}}
# stringify(data)  # то же самое что stringify(data, ' ', 1)
# # {
# #  hello: world
# #  is: True
# #  nested: {
# #   count: 5
# #  }
# # }
#
# stringify(data, '|-', 2)  # символ, переданный вторым аргументом повторяется столько раз, сколько указано третьим аргументом
# # {
# # |-|-hello: world
# # |-|-is: True
# # |-|-nested: {
# # |-|-|-|-count: 5
# # |-|-}
# # }

"""Подсказки

    - чтобы лучше понять как работает JSON.stringify(), запускайте его с 
    разными данными и параметрами в консоли браузера;
    - проверки в тестах идут от простого к сложному:
        - проверка на примитивных типах;
        - проверка на "плоских" данных;
        - проверка на "вложенных" данных.
    - реализуйте функцию так же пошагово, проверяя, что изменения для сложных 
    кейсов не сломали более простые;
    - документация по JSON.stringify на MDN."""
import itertools

primitive = 'hello'
primitives = {"string": "value", "boolean": True, "number": 5}
data = {"hello": "world", "is": True, "nested": {"count": 5}}
nested = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}



def stringify(value, replacer=' ', spaces_сount=1):
    if not isinstance(value, dict):
        return str(value)

    def walk(node, depth=1):
        res_list = ['{']

        for key, v_value in node.items():
            res_list.append(
                f'''{replacer * depth}{key}: '''
                f'''{walk(v_value, depth + spaces_сount)
                if isinstance(v_value, dict) else v_value}'''
                )

        res_list.append(f'{replacer * (depth - spaces_сount)}{"}"}')
        result_string = '\n'.join(res_list)

        return result_string

    return walk(value, spaces_сount)

'SOLUTION'
# def stringify(value, replacer=' ', spaces_count=1):
#
#     def iter_(current_value, depth):
#         if not isinstance(current_value, dict):
#             return str(current_value)
#
#         deep_indent_size = depth + spaces_count
#         deep_indent = replacer * deep_indent_size
#         current_indent = replacer * depth
#         lines = []
#         for key, val in current_value.items():
#             lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
#         result = itertools.chain("{", lines, [current_indent + "}"])
#         return '\n'.join(result)
#
#     return iter_(value, 0)

# print(stringify(primitive))
# print('\n')
# print(stringify(primitives, '-', 4))
# print('\n')
# print(stringify(data, '-', 2))
# {
# |-|-hello: world
# |-|-is: True
# |-|-nested: {
# |-|-|-|-count: 5
# |-|-}
# }
# print('\n')
print(stringify(nested, '|-', 1))
