'''

Задача: на место первого четного элемента целоичсленного массива K (9)
записать произведение остальных элементов этого массива.
Измененный масив вывести.

'''

'''

Обозначение переменных:

K - массив K (9).
ElementJ - индекс первого четного элемента.
Flag = флаг не дающий искать четные эл. после найденного первого четного эл.
stringArrayK  - массив К в виде строки.

'''

'''

Тестовые примеры:

1) K = 1 2 3 4 1 1 1 1 1
Вывод: 1 12 3 4 1 1 1 1 1

2) K = 9 9 9 9 9 9 9 9 9
Вывод: нет четного числа

3) K = -1 0 -2 3
Вывод: -1 6 -2 3

4) K = 0
Вывод: 0

'''

K = []
ElementJ = 1
Flag = True

# Заполнение массива K:

K = []

while len(K) > 9 or len(K) == 0:
    K = list(map(int, input('В одну строку заполните массив \
K (не более 9 элементов): ').split()))
    if len(K) > 9:
        print('\nВы ввели более 9 элементов. \n')

# Поиск первого четного элемента и подсчет произв. остальных:

for i in range (len(K)):
    if K[i] % 2 == 0 and Flag == True:
        j = i
        Flag = False
        K[i] = str(K[i])
    else:
        ElementJ *= K[i]
        K[i] = str(K[i])
    if len(K) == 1:
        ElementJ = K[i]

# Вывод измененного массива:

if Flag == False:
    K[j] = str(ElementJ)
    stringArrayK = ' '.join(K)
    print('\nИзмененный массив K: ', stringArrayK , sep='')
else:
    print('\nМассив не содержит четных элементов.')
