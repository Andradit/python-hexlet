'''Данные об email-адресах студентов хранятся в словаре:'''

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin',
                      'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin',
                        'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

'''Нужно дополнить код таким образом, чтобы он вывел все адреса в алфавитном
порядке и в формате имя_пользователя@домен.'''


item_of_emails = []

for key, value in emails.items():
    for i in value:
        item_of_emails.append(i + '@' + key)
print('\n'.join(item_of_emails))
print(sorted(item_of_emails))
