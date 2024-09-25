import re


"""
Символьные классы:
"""
# Пример использования символьного класса [0-9] для поиска цифр
# text = "Hello from 2024"
# exp = r'[0-9]'
# result = re.findall(exp, text)
# print(result)
# ['2', '0', '2', '4']
# Возвращает список из всех найденных одиночных символов которые являются цифрами



"""
Символьные сокращения:
"""
# Пример использования  \d для поиска цифр
# text = "Hello from 2024"
# exp = r'\d'
# result = re.findall(exp, text)
# print(result)
# ['2', '0', '2', '4']
# Возвращает список из всех найденных одиночных символов которые являются цифрами

# Пример использования  \D для поиска любого символа кроме цифры
# text = "Hello from 2024"
# exp = r'\D'
# result = re.findall(exp, text)
# print(result)
# ['H', 'e', 'l', 'l', 'o', ' ', 'f', 'r', 'o', 'm', ' ']
# Возвращает список из всех найденных одиночных символов которые не являются цифрами

# Пример использования  . для поиска любого символа
# text = "Hello from 2024"
# exp = r'.'
# result = re.findall(exp, text)
# print(result)
# ['H', 'e', 'l', 'l', 'o', ' ', 'f', 'r', 'o', 'm', ' ', '2', '0', '2', '4']
# Возвращает список из всех найденных одиночных символов


"""
Квантификаторы:
"""
# Пример использования квантификаторов {3,4}, ?, +
# text = "Phone number: 123-456-7890 or 098-765-4321"
# exp = r'(?:\d{3,4}-?)+'
# result = re.findall(exp, text)
# print(result)
# ['123-456-7890', '098-765-4321']
# Возвращает список номеров телефона которые совпадают с шаблоном

# Пример жадного квантификатора {1,5}
# text = "0123456789"
# exp = r'\d{1,5}'
# result = re.findall(exp, text)
# print(result)
# ['01234', '56789']
# Он стремится вернуть совпадения как можно короче

# Пример сверх жадного квантификатора {1,5}+
# text = "0123456789"
# exp = r'\d{1,5}+'
# result = re.findall(exp, text)
# print(result)
# ['01234', '56789']
# Он стремится вернуть совпадения как можно короче

# Пример ленивого квантификатора {1,5}?
# text = "0123456789"
# exp = r'\d{1,5}?'
# result = re.findall(exp, text)
# print(result)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Он стремится вернуть совпадения как можно короче


"""
Границы слова:
"""
# Пример использования \b границы слова
# text = "She found the note in the Notebook on her desk."
# exp = r'\b[nN]ote\w*\b'
# result = re.findall(exp, text)
# print(result)
# ['note', 'Notebook']
# Возвращает список слов начинающихся note или Note


"""
Многострочный режим:
"""
# Пример многострочного режима
# text = """This is a line
# That starts with T
# Another line"""
# exp = r'^T.*$'
# result = re.findall(exp, text, re.MULTILINE)
# print(result)
# ['This is a line', 'That starts with T']
# Разделяет текст на отдельные строки по переводу строки и возвращает строки что начинаются с буквы T


"""
Поиск и замена:
"""
# Пример поиска и замены текста при помощи ссылки
# start_text = '''Это первая строка текста
# Это вторая строка текста
# И вот еще одна строка'''
# exp = r'^(.*)$'
# text = r'<!DOCTYPE html>\n<html lang="en">\n<head><title>Rime</title></head>\n<body>\n<h1>\1</h1>\n\n'
# result = re.sub(exp, text, start_text, count=1, flags=re.MULTILINE)
# print(result)
# Он заменяет первую строку в start_text на строку из text+первую строку
#<!DOCTYPE html>
# <html lang="en">
# <head><title>Rime</title></head>
# <body>
# <h1>Это первая строка текста</h1>
# Это вторая строка текста
# И вот еще одна строка


"""
Альтернативы:
"""
# Пример использования альтернатив (OR | or) с использованием захватывающих групп
# text = "You can say hello or Hello or HELLO!"
# exp = r'(HELLO|hello|Hello)' #важно что пробелы внутри этой конструкции считаются за часть текста!
# result = re.findall(exp, text)
# print(result)
# ['hello', 'Hello', 'HELLO']
# Возвращает совпадения по одному из указанных в захватывающей группе

# Пример использования альтернатив OR | or без использования захватывающих групп
# text = "You can say hello or Hello or HELLO!"
# exp = r'HELLO|hello|Hello' #важно что пробелы внутри этой конструкции считаются за часть текста!
# result = re.findall(exp, text)
# print(result)
# ['hello', 'Hello', 'HELLO']
# Возвращает совпадения по одному из указанных


"""
Захватывающие и незахватывающие группы:
"""
# Пример использования (?i:) игнорирования регистра символов
# text = "hello Hello HELLO"
# exp = r'(?i:hello)'
# result = re.findall(exp, text)
# print(result)
# ['hello', 'Hello', 'HELLO']
# Возвращает совпадения текста без учета регистра

# Пример использования именованных групп. (?P<name>)
# text = "Name: John Doe, Age: 30"
# exp = r'Name: (?P<name>\w+ \w+), Age: (?P<age>\d+)'
# match = re.search(exp, text)
# first_name = match.group('name')
# age = match.group('age')
# print(first_name, age)
# John Doe 30
# Используя две именованные пруппы <name> и <age> мы получаем значения совпадений


"""
Жадный и ленивый поиск:
"""
# Жадный поиск
# text = "Hello! My name is Tom!"
# exp = r'H.*!'
# result = re.findall(exp, text)
# print(result)
# ['Hello! My name is Tom!']
# Жадный поиск старается найти выражение длиннее.

# Ленивый поиск
# text = "Hello! My name is Tom!"
# exp = r'H.*?!'
# result = re.findall(exp, text)
# print(result)
# ['Hello!']
# Ленивый поиск старается найти самое короткое выражение


"""
Положительные и отрицательные проверки:
"""
# Положительная опережающая проверка
# text = "The Ancyent Marinere stoppeth one of three."
# exp = r'(?i)ancyent(?=\smarinere)'
# result = re.findall(exp, text)
# print(result)
# ['Ancyent']
# Возвращает все найденые 'Ancyent' после которых следует через пробел 'marinere'

# Отрицательная опережающая проверка / полная противоположность Положительной проверки
# text = "The Ancyent Marinere stoppeth one of three."
# exp = r'(?i)ancyent(?!\smarinere)'
# result = re.findall(exp, text)
# print(result)
# []
# Возвращает все найденые 'Ancyent' после которых НЕ следует через пробел 'marinere'

# Положительная ретроспективная проверка
# text = "The Ancyent Marinere stoppeth one of three."
# exp = r'(?i)(?<=ancyent\s)marinere'
# result = re.findall(exp, text)
# print(result)
# ['Marinere']
# Возвращает все найденые 'Marinere' перед которым следует через пробел 'Ancyent'

# Отрицательная ретроспективная проверка
# text = "The Ancyent Marinere stoppeth one of three."
# exp = r'(?i)(?<!ancyent\s)marinere'
# result = re.findall(exp, text)
# print(result)
# []
# Возвращает все найденые 'Marinere' перед которым НЕ следует через пробел 'Ancyent'


"""
Дополнительные опции:
"""
# Без использования дополнительных опций (?i)
# text = "WORLD World world"
# exp = r'\bworld\b'
# result = re.findall(exp, text)
# print(result)
# ['world']
# Игнорирует регистр литерала

# Использование опций в начеле регулярного выражения(?i)
# text = "WORLD World world"
# exp = r'(?i)\bworld\b'
# result = re.findall(exp, text)
# print(result)
# ['WORD', 'Word', 'word']
# Игнорирует регистр литерала

# Использование опций в незахватывающей группе (?i:word)
# text = "WORLD World world"
# exp = r'\b(?i:world)\b'
# result = re.findall(exp, text)
# print(result)
# ['WORLD', 'World', 'world']
# Игнорирует регистр литерала



