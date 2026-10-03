# Шифр Цезаря 0.5 (только для маленьких английских букв)
# n = int(input())
# shifr = input()
# res = ''
# for i in range(len(shifr)):
#     pos = ord(shifr[i]) - ord('a') 
#     shifrator = (pos - n) % 26
#     new = chr(shifrator + ord('a'))
#     res += new

# print(res)


# Шифр Цезаря 1.0 (адаптация под английский и русский язык)
print('Привет, ты попал на программу шифр Цезаря!')

first_gran = ord('a')
last_gran = ord('z')
buk_int_mal = ord('a')
buk_int_big = ord('A')
all_buk = 26

n = int(input('Шаг сдвига каждой буквы(только целое число):\n'))

while not n.isdigit():
    n = input('Ты ввёл неправильно, попробуй ещё раз(целое число без знака):\n')
n = int(n)
direction = input('Ты хочешь зашифровать или дешифровать сообщение?(принимаются только ответы: шифрование или дешифрование)\n ')

while True:
    if direction.lower() == 'дешифрование':
        n = n * -1
        break
    elif direction.lower() == 'шифрование':
        break
    else:
        direction = input('Ты ввёл неправильно, попробуй ещё раз(шифрование или дешифрование)\n')


language = input('Выбери язык на котором ты будешь писать(принимаются только ответы: русский или английский)?\n')

while True:
    if language.lower() == 'русский':
        first_gran = ord('а')
        last_gran = ord('я')
        buk_int_mal = ord('а')
        buk_int_big = ord('А')
        all_buk = 32
        break
    elif language.lower() == 'английский':
        break
    else:
        language = input('Ты ввёл язык неправильно, попробуй ещё раз(русский или английский)\n')


shifr = input('Твоё сообщение:\n')
res = ''



for i in range(len(shifr)):
    if shifr[i].isalpha() and first_gran <= ord(shifr[i].lower()) <= last_gran:
        if shifr[i].islower():
            pos = ord(shifr[i]) - buk_int_mal 
            shifrator = (pos + n) % all_buk
            new = chr(shifrator + buk_int_mal)
            res += new
        else:
            pos = ord(shifr[i]) - buk_int_big 
            shifrator = (pos + n) % all_buk
            new = chr(shifrator + buk_int_big)
            res += new
    else:
        res += shifr[i]


print(res)
