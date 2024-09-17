import re

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

# Пример использования квантификаторов {3,4}, ?, +
# text = "Phone number: 123-456-7890 or 098-765-4321"
# exp = r'(?:\d{3,4}-?)+'
# result = re.findall(exp, text)
# print(result)
# ['123-456-7890', '098-765-4321']
# Возвращает список номеров телефона которые совпадают с шаблоном


# Пример использования \b границы слова
# text = "She found the note in the Notebook on her desk."
# exp = r'\b[nN]ote\w*\b'
# result = re.findall(exp, text)
# print(result)
# ['note', 'Notebook']
# Возвращает список слов начинающихся note или Note


# Пример многострочного режима
# text = """This is a line
# That starts with T
# Another line"""
# exp = r'^T.*$'
# result = re.findall(exp, text, re.MULTILINE)
# print(result)
# ['This is a line', 'That starts with T']
# Разделяет текст на отдельные строки по переводу строки и возвращает строки что начинаются с буквы T
