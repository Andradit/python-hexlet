"""Реализуйте функцию transform(input_file, output_file, rules), которая
принимает на вход путь до текстового файла, путь по которому нужно записать 
результат и обрабатывает текст согласно словарю rules следующим образом:

word_min_len - отфильтровывает слова меньше минимальной длины
censored_words - список слов, которые нужно удалить из текста
capital_letters - список букв, которые нужно привести к заглавным, если слово на
них начинается"""

# The Python language was not named after a long snake but after the British
# comedy show Monty Python Flying Circus

# rules = {
#     'word_min_len': 3,
#     'censored_words': ['language', 'show'],
#     'capital_letters': ['l', 'a'],
# }
#
# transform('python.txt', 'out.txt', rules=rules)
# print(open('out.txt').read())

# string = ('Beautiful better\nExplicit better implicit\nSimple better
# complex\nComplex better complicated\nReadability counts\n'"Special cases
# aren't Special enough break rules\n"'Although Practicality beats
# Purity\n''Errors Should never Silently\n''Unless explicitly
# Silenced\n''ambiguity refuse temptation guess\n''There Should Preferably
# obvious\n'"Although obvious first unless you're Dutch\n"'better
# never\n''Although never often better right\n'"Namespaces honking great
# let's those\n")

'''Если в результате преобразования получилась пустая строка, то ее не нужно 
записывать в выходной файл.

Подсказки
Используйте потоковую обработку.
Каждое правило трансформера можно описать отдельной функцией и в итоговой
собрать пайплайн обработки'''

# input_file = open("input.txt", "r")
string = ("The Python language was not named after a long snake but "
          "after the British comedy show Monty Python Flying Circus")
print(string)

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")


# input_file.write('Beautiful better\nExplicit better implicit\nSimple better
# complex\nComplex better complicated\nReadability counts\n'"Special cases
# aren't Special enough break rules\n"'Although Practicality beats
# Purity\n''Errors Should never Silently\n''Unless explicitly
# Silenced\n''ambiguity refuse temptation guess\n''There Should Preferably
# obvious\n'"Although obvious first unless you're Dutch\n"'better
# never\n''Although never often better right\n'"Namespaces honking great
# let's those\n") input_file.close() output_file.close()


# string = ("The Python language was not named after a long snake but after "
#           "the "
#           "British comedy show Monty Python Flying Circus")


def word_min_len(length, text):
    res_text = []
    for line in text:
        new_line = ''
        for i in line.split():
            if len(i) > length:
                new_line += i + ' '
        res_text.append(new_line.strip())
    return res_text


#
#
# print(word_min_len(3, string))


def censored_words(del_words, text):
    result = []
    for line in text:
        new_line = ''
        for word in line.split():
            if word not in del_words:
                new_line += word + ' '
        result.append(line.strip())
    return result


#
#
# print(censored_words(['language', 'show'], string,))


def capital_letters(up_letters, text):
    result = []
    for line in text:
        new_line = ''
        for word in line.split():
            if word[0] in up_letters:
                new_line += word.title()
            else:
                new_line += word
            new_line += ' '
        result.append(new_line.strip())
    return result


#
#
# print(capital_letters(['l', 'a'], string,))

rules = {}
rules['word_min_len'] = 3
rules['censored_words'] = ['language', 'show']
rules['capital_letters'] = ['l', 'a']
print(rules)


# rules = {
#     word_min_len: 3,
#     censored_words: del_words,
#     'capital_letters': up_letters,
# }


def transform(in_file, out_file, rules):
    result = open(in_file).readlines()
    if 'word_min_len' in rules:
        result = word_min_len(rules['word_min_len'], result)
        print(result)
    if 'censored_words' in rules:
        result = censored_words(rules['censored_words'], result)
        print(result)
    if 'capital_letters' in rules:
        result = capital_letters(rules['capital_letters'], result)
        print(result)

    out = open(out_file, "w")
    print('\n'.join(result).strip('\n'))
    out.write('\n'.join(result) + '\n')

    return '\n'.join(result).strip('\n')


# print(string)
# print(transform("input.txt", "output.txt", rules))
# rules = (word_min_len | censored_words | capital_letters)

print(transform('input.txt', 'output.txt', rules=rules))
# print(open('out.txt').read())
