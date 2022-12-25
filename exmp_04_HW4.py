# 4- Шифр Цезаря - это способ шифрования, 
# где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать
# "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

def input_list_element(path, elements):
    with open(path, 'w', encoding='utf-8') as file_key:
        """Запись в файл символов, используемых для шифрования"""
        file_key.writelines(elements)

# def input_encodig_text(path, elements):
#     with open(path, 'w', encoding='utf-8') as file_key:
#         """Запись в файл шифрованного текста"""
#         file_key.writelines(elements)

def new_index_encr_decr(ind, op, key_op):
    if op == 0: 
        new_ind = ind + key_op
    elif op == 1:
        new_ind = ind - key_op
    return new_ind

def encrypt_message(message, coding, key_coding, abc):
    """Шифруем сообщение с заданным ключом"""
    # global key_encription
    # global alphabet
    result = ''

    for i in message:
        index = abc.find(i)
        new_index = new_index_encr_decr(index, coding, key_coding)

        if i in abc:
            result += abc[new_index]
        else:
            result += i
    return result

def get_text(path):
    """Получаем данные из файла"""
    with open(path, 'r', encoding='utf-8') as file_key:
        text = str(file_key.read())
    return text

def main():
    # определяем набор символов для шифрования
    input_list_element('exmp04_alphabet.txt', 'абвгдежзиклмнопрстуфхцчшщъыьэюяабвгдежзиклмнопрстуфхцчшщъыьэюя')
    alphabet = get_text('exmp04_alphabet.txt')
    
    # Получаем данные для шифрования от пользователя
    original_message = input("Сообщение для шифровки: ")
    key_encription = int(input('Введите ключ шифрования: '))
    en_de = int(input('ШИфруем / ДЕшифруем (0/1): '))

    print(f'\nШифрованное сообщение: ', encrypt_message(original_message, en_de, key_encription, alphabet))
    # Записываем в файл зашифрованное сообщение
    input_list_element('exmp04_coding.txt', encrypt_message(original_message, en_de, key_encription, alphabet))
    
    # Получаем из файла зашифрованное сообщение и дешифруем его
    encryption_message = get_text('exmp04_coding.txt')
    print(f'\nДешифрованное сообщение из файла: ', encrypt_message(encryption_message, 1, key_encription, alphabet))

main()