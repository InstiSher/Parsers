# Инфа про Парсер

Парсинг сайта с курсами валют, а именно Оф.Рос.Центрального банка, В нем нет ничего сложного, правда это ещё не все так как находится в стадии быстрого доступа, сейчас мы просто получаем данные, теперо нужно думать как их конвертировать правиьным образом, а также как к ним быстро обращаться

Все это лишь часть для моего телеграмм бота по конверовке валют. А так же я столкнулся с очень интересной проблемой советуя вам про неё прочитать

# Шикарная проблема JSON файла

Прикиньте, если даже открытие файла имеет кодировку отличающуюся от стандарта 'utf-8', то открытие и последующие сборы файла из него должны быть в той же кодировке файла json

Ибо выходит следующая ошибка: json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)


```python
with open('money.json', 'w', encoding="utf-16") as json_file:
  json.dump(money_data, json_file, indent=4)

with open('money.json') as f:
  data = json.load(f)
  print(data)
```

Да, выйдет ошибка для этого нужно всего лишь убрать в открытии файла кодировку. При чем с кодировкой или без вы не увидите разницу в самом файле json, в нем русские буквы будут следующие: "u0440\u...", так как для файла json, в функцию json.dump() Нужно записывать ensure_ascii=False

```python
with open('money.json', 'w') as json_file:
  json.dump(money_data, json_file, ensure_ascii=False, indent=4)
```

Так вот решение было простым и вот оно:

```python
with open('money.json', 'w') as json_file:
  json.dump(money_data, json_file, indent=4)

with open('money.json') as f:
  data = json.load(f)
  print(data)
```