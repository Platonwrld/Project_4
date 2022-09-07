import json

""" Метод для сериализации данных из txt в json """

arr = []

with open('mat.txt', encoding='utf-8') as r:

    for i in r:
        n = i.lower().split('\n')[0]

        if n != '':
            arr.append(n)

with open('mat.json', 'w', encoding='utf-8') as e:
    json.dump(arr, e) 