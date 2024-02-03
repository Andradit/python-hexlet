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

import itertools
from itertools import zip_longest

import shutil


# file_1.close()
# file_2.close()

def merge(file1, file2, out):
    with (open(file1, 'r') as f_1, open(file2, 'r') as f_2):
        with open(out, 'w') as o:
            diff_1 = []
            diff_2 = []
            for line_1, line_2 in zip_longest(f_1, f_2):
                print(f'{diff_1=}, {diff_2=}, {line_1=}, {line_2=}')
                if line_1 != line_2:
                    diff_1.append(line_1)
                    diff_2.append(line_2)
                else:
                    if diff_1 and diff_2:
                        o.write(f'>>>file1>>>\n{"".join(diff_1)}=====\n{"".join(diff_2)}<<<file2<<<\n')
                        diff_1 = []
                        diff_2 = []
                    o.write(line_1)
            if diff_1 and diff_2:
                o.write(f'>>>file1>>>\n{"".join(diff_1)}=====\n{"".join(diff_2)}<<<file2<<<\n')




    # open(out, 'w').writelines(strings_of_file1)
    # print(strings_of_file1)
    # print(strings_of_file2)
    # a = ''
    # b = ''
    # c = ''
    # d = ''
    # res = (f'{a}>>>file1>>>\n{b}=====\n'
    #        f'{c}<<<file2<<<{d}')
    # # res_1 = []
    # # res_2 = []
    # # res_3 = []
    # for index, line_1 in enumerate(strings_of_file1):
    #     # if strings_of_file2[index] == line_1:
    #     #     d += strings_of_file2[index]
    #     if line_1 != strings_of_file2[index]:
    #         b += line_1
    #         c += strings_of_file2[index]
    # if line_1 == strings_of_file2[index]:
    #     # res_1.append(line_1)
    #     a += line_1
    #     d += line_1

    # return f'{a}\n>>>file1>>>\n{b}=====\n{c}<<<file2<<<\n{d}'

    # res_1.extend(res_2)
    # res = [x for x in itertools.chain(res_1, res_2, res_3)]
    # print(res)

    # print(f'>>>file1>>>\n{line_1}=====\n'
    #       f'{strings_of_file2[index]}<<<file2<<<')
    # res = ['>>>file1>>>\n']
    # for index_1, line_1 in enumerate(strings_of_file1):
    #     if line_1 in strings_of_file2:
    #         res.insert(index_1, line_1)
    #
    #     if line_1 not in strings_of_file2:
    #
    #         res.append(line_1)
    #
    #     res.append(line_1)

    # res += '>>>file1>>>\n'
    # elif line_1 not in strings_of_file2:
    #     res += line_1
    # for line_2 in strings_of_file2:
    #     if line_2 in strings_of_file1:
    #         res += line_2
    #         res += '<<<file2<<<\n' + '=====\n'
    #     if line_2 not in strings_of_file1:
    #         res += line_2

    # for line_2 in strings_of_file2:
    # else:
    #     res += '>>>file1>>>\n' + '====='
    # return res

    # print(res)
    # if line_2 not in strings_of_file1:
    #     res += line_2
    #     res += '<<<file2<<<'

    # print(strings_of_file1)
    # print(strings_of_file2)
    # result_1 = open(out, 'w').writelines(res)
    # return result_1


print(merge('file1.txt', 'file2.txt', 'out.txt'))
