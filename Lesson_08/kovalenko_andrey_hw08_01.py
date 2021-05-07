'''
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:

email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}

email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
 ...
 raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
'''

import re


def email_parse(mail_addr='email@email.com'):
    if re.match(r"^[\w-]+@([\w-]+\.)+[\w-]{2,4}$", mail_addr) is not None:
        print({'username': mail_addr.split('@')[0], 'domain': mail_addr.split('@')[-1]})
    else:
        raise ValueError(f'Wrong email: {mail_addr}')


email_parse('test123@mail.ru')
