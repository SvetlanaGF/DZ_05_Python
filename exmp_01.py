# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

print('Уберем из текста заданное слово')
first_text = input("Введите текст через пробел: \n")
excluded_text = input("\nВведите текст, который следует удалить:\n")

list = [i for i in first_text.split() if excluded_text not in i]
print(f"\nИсходный текст: {first_text}")
print(f'Результат: {" ".join(list)}')