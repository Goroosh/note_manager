title1 = input('Заголовок ')
title2 = input('Заголовок ')
name = input('Имя? ')
created_date = input('Введите дату в формате 01.01.2025 или 01-01.2025 ')
info1 = created_date
issue_date = input('Введите дату в формате 01.01.2025 или 01-01.2025 ')
info2 = issue_date
status = input('Статус ')
content = input('Описание')
note = [
name,
content,
status,
info1 [0:5],
info2 [0:5],
[title1, title2]
]
print(note)