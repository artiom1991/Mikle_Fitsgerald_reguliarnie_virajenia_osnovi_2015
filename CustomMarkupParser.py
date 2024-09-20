import re

MD = "./examples/example.md"
HTML = "./examples/example.html"
NOT_MD = "./examples/example.customMarkup"


def readFile(filename):
    text_list = []
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            text_list.append(line.strip())
    return text_list


def writeFile(filename, content_list):
    with open(filename, "w", encoding="utf8") as file:
        for line in content_list:
            file.write(line + '\n')


def parseText(text_list):
    token_md = []
    token_html = []
    specification = [
        (r'^\s*h1:\s*(.+)', r'# \1  ', r'<h1>\1</h1>'),
        (r'^\s*h2:\s*(.+)', r'## \1  ', r'<h2>\1</h2>'),
        (r'^\s*h3:\s*(.+)', r'### \1  ', r'<h3>\1</h3>'),
        (r'^\s*h4:\s*(.+)', r'#### \1  ', r'<h4>\1</h4>'),
        (r'^\s*h5:\s*(.+)', r'##### \1  ', r'<h5>\1</h5>'),
        (r'^\s*h6:\s*(.+)', r'###### \1  ', r'<h6>\1</h6>'),
        (r'^\s*bold:\s*(.+)', r'__\1__  ', r'<b>\1</b>'),
        (r'^\s*italic:\s*(.+)', r'*\1*  ', r'<i>\1</i>'),
    ]
    for line in text_list:
        for el in specification:
            if re.match(el[0], line):
                token_md.append(re.sub(el[0], el[1], line))
                token_html.append(re.sub(el[0], el[2], line))

    print(token_html)
    print(token_md)
    writeFile(MD, token_md)
    writeFile(HTML, token_html)


get_text = readFile(NOT_MD)
parseText(get_text)
