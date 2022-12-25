# 4-Создайте два списка — один с названиями языков программирования, 
# другой — с их нумерацией. ['python', 'c#'] и  [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей,
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — 
# которая отфильтрует этот список следующим образом:
# если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, 
# его номер заменяется на сумму очков.
# [сумма очков C# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. 
# Суммой очков называется сложение порядковых номеров букв в слове. 
# Cложите получившиеся числа и верните из функции в качестве ответа 
# вместе с преобразованным списком

задача не решена

def upp_char(languages):
    """Переводим буквы из строчных в заглавные"""
    upp_languages = list(map(str.upper, languages))
    return upp_languages
 

def list_num_lang(list1, list2):
    """Создаем кореж из двух списков"""
    data = list(zip(list1, list2))
    return data

def sum_word(list_char):
    """Находим сумму очков слова"""
    code = 0
    for i in range(0, len(list_char)-1):
        sum_code = 0
        word = list(tuple(list_char[i]))
        for k in range(len(word)):
            symbol = word[k]
            code = ord(symbol)
            sum_code += code
    return sum_code
    
def factors_calculation(number):
    """Создает список простых множителей заданного числа"""
    factor = 2
    factors_array = []
    while factor * factor <= number:
        if number % factor == 0:
            factors_array.append(factor)
            number //= factor
        else:
            factor += 1
    if number > 1:
        factors_array.append(number)

    return factors_array

def search_elements(n_list):
    """Определяем есть ли среди делителей номер языка"""
    result = False
    for number in n_list:
        if number in n_list:
            return not result
   

# начало
program_lang = ['python', 'c#']
numbers = [1, 2]
languages = upp_char(program_lang) # получаем заглавные буквы
mixture = list_num_lang(numbers, languages) # создаем кортеж номер+язык

sum_lang = sum_word(languages)
x = factors_calculation(sum_lang)
valid = search_elements(x)
for i in range(len(numbers)):
    if valid == True:
        numbers[i] = x
