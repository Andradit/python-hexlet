"""В этом упражнении вам предстоит реализовать функцию merge(file1, file2,
out), которая мержит (совмещает) два текстовых файла file1 и file2 и
записывает результат по указанному пути out.

В случае, если в файлах не совпадают строки, то нужно:

- вывести строки первого файла, отметив их как >>>file1>>>
- вывести разделитель =====
- вывести строки второго, отметив их как <<<file2<<<
Например:"""

# cat file1.txt
#
# Hello from Hexlet
# Python is awesome
# Javascript is not about coffee
# Use context managers
#
# cat file2.txt
#
# Hello from Hexlet
# Python is a snake
# Javascript is a language
# Use context managers

# merge('file1.txt', 'file2.txt', 'out.txt')

# Hello from Hexlet
# >>>file1>>>
# Python is awesome
# Javascript is not about coffee
# =====
# Python is a snake
# Javascript is a language
# <<<file2<<<
# Use context managers


""">>>file1>>>
Hello from Hexlet
=====
Hello World
<<<file2<<<
Python is awesome
>>>file1>>>
Python also is a snake
And also a comedy show
Use context managers
=====
And also a comedy show
Python also is a snake
Use Force
<<<file2<<<"""

"""Подсказки.

- используйте контекстные менеджеры для управления открытием и закрытием файлов;
- для упрощения предположим, что файлы имеют одинаковое количество строк."""

file_1 = open('file1.txt', 'r')
file_2 = open('file2.txt', 'r')
output = open('out.txt', 'w')


def merge(file1, file2, out):
    with (open(file1, 'r') as input_file_1, open(file2, 'r') as input_file_2):
        with open(out, 'w') as output_file:
            diff_1 = []
            diff_2 = []
            for line_1, line_2 in zip(input_file_1, input_file_2):
                # print(f'{diff_1=}, {diff_2=}, {line_1=}, {line_2=}')
                if line_1 != line_2:
                    diff_1.append(line_1)
                    diff_2.append(line_2)
                else:
                    if diff_1 and diff_2:
                        output_file.write(
                            f'>>>file1>>>\n{"".join(diff_1)}=====\n'
                            f'{"".join(diff_2)}<<<file2<<<\n')
                        diff_1 = []
                        diff_2 = []
                    output_file.write(line_1)
            if diff_1 and diff_2:
                output_file.write(f'>>>file1>>>\n{"".join(diff_1)}=====\n'
                                  f'{"".join(diff_2)}<<<file2<<<\n')


'SOLUTION'

# def merge(file1, file2, out):
#     with (
#         open(file1, 'r') as f1,
#         open(file2, 'r') as f2,
#         open(out, 'w') as fout,
#     ):
#         diff1 = []
#         diff2 = []
#         for line1, line2 in zip(f1, f2):
#             if line1 == line2:
#                 if diff1 or diff2:
#                     fout.write(make_diff_view(diff1, diff2))
#                     diff1 = []
#                     diff2 = []
#                 fout.write(line1)
#             else:
#                 diff1.append(line1)
#                 diff2.append(line2)
#         if diff1 or diff2:
#             fout.write(make_diff_view(diff1, diff2))
#
#
# def make_diff_view(diff1, diff2):
#     template = f">>>file1>>>\n{''.join(diff1)}=====\n{''.join(diff2)}<<<file2<<<\n"  # noqa: E501
#     return template

print(merge('file1.txt', 'file2.txt', 'out.txt'))
