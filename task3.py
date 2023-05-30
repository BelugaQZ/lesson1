from random import randint
""""
list = []
def InputList(n):
    for i in range(n):
        #list[i] = randint(1, 100)
        list.append(randint(1, 100))
    print(*list)

def SearchList(x, list):
    count = 0
    for i in range(len(list)):
        if list[i] == x: count += 1
    print(f'Элемент "{x}" встречается {count} раз')

def Element(b, list):
    max = 0
    for i in range(len(list)):
        if list[i] > max and list[i] < b:
            max = list[i]
    print(f'Самый близкий элемент {max}')

n = int(input('Количество элементов: '))
InputList(n)
x = int(input('Найти цифру: '))
SearchList(x, list)
#b = int(input(''))
Element(x, list)

"""

#Задача 20
word = input('Введите слово: ').upper()
alphabet = {
1: 'A, E, I, O, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т',
2: 'D, G, Д, К, Л, М, П, У',
3: 'B, C, M, P, Б, Г, Ё, Ь, Я',
4: 'F, H, V, W, Y, Й, Ы',
5: 'K, Ж, З, Х, Ц, Ч',
8: 'J, X, Ш, Э, Ю',
10: 'Q, Z, Ф, Щ, Ъ'
}

count = 0
for i in range(len(word)):
    for j in alphabet:
        mylist = list(alphabet[j])
        for k in range(len(mylist)):
            if word[i] == mylist[k]:
                count += j
print(f'{word} = {count}')