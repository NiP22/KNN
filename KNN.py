import random
import math
import numpy as np
import copy
from itertools import groupby


'''

alphabet = {'б': 1, 'Б': 1, 'в': 2, 'В': 2, 'г': 3, 'Г': 3, 'д': 4, 'Д': 4, 'ж': 5, 'Ж': 5, 'з': 6, 'З': 6,
            'й': 7, 'Й': 7, 'к': 8, 'К': 8, 'л': 9, 'Л': 9, 'м': 10, 'М': 10, 'н': 11, 'Н': 11,  'п': 12, 'П': 12,
            'р': 13, 'Р': 13, 'с': 14, 'С': 14, 'т': 15, 'Т': 15, 'ў': 16, 'Ў': 16, 'Ф': 17, 'ф': 17, 'х': 18, 'Х': 18,
            'ц': 19, 'Ц': 19, 'ч': 20, 'Ч': 20, 'ш': 21, 'Ш': 21, 'ь': 22, 'Ь': 22, 'э': 30, 'Э': 30, 'ю': 31, 'Ю': 31,
            'я': 32, 'Я': 32, 'а': 33, 'А': 33, 'е': 34, 'Е': 34, 'ё': 35, 'Ё': 35, 'i': 36, 'І': 36, 'о': 37, 'О': 37,
            'у': 38, 'У': 38, 'ы': 39, 'Ы': 39}

'''


alphabet = {'б': 10, 'Б': 10, 'в': 5, 'В': 5, 'г': 10, 'Г': 10, 'д': 10, 'Д': 10, 'ж': 10, 'Ж': 10, 'з': 10, 'З': 10,
            'й': 10, 'Й': 10, 'к': 5, 'К': 5, 'л': 10, 'Л': 10, 'м': 10, 'М': 10, 'н': 10, 'Н': 10,  'п': 5, 'П': 5,
            'р': 10, 'Р': 10, 'с': 5, 'С': 5, 'т': 5, 'Т': 5, 'ў': 5, 'Ў': 5, 'Ф': 5, 'ф': 5, 'х': 5, 'Х': 5,
            'ц': 10, 'Ц': 10, 'ч': 5, 'Ч': 5, 'ш': 5, 'Ш': 5, 'ь': 5, 'Ь': 5, 'э': 20, 'Э': 20, 'ю': 20, 'Ю': 20,
            'я': 20, 'Я': 20, 'а': 20, 'А': 20, 'е': 20, 'Е': 20, 'ё': 20, 'Ё': 20, 'i': 20, 'І': 20, 'о': 20, 'О': 20,
            'у': 20, 'У': 20, 'ы': 20, 'Ы': 20}




def wordToVekt(word):
    mas = list(word)
    ans = []
    count = 0
    for i in mas:
        if i in alphabet:
            count += 1
            ans.append(alphabet[i])
        else:
            break
        if count > 9:
            break
    while count <= 9:
        count += 1
        ans.append(0)
    return ans


def listToStr(lis):
    ans = ""
    for i in lis:
        ans += (str(i) + ' ')
    return ans


def getSet():#читает из файла векторы
    outX = open("X.txt", "r")
    keys = outX.read()
    mas = keys.split(sep=':')
    #a = np.zeros(shape=(2*len(mas), 15))
    X = np.array(list(map(lambda x: x.split(), mas)))
    outX.close()
    return X


koef = [5, 10, 20]

def createSet():# создает файл с векторами
    outX = open("X.txt", "w")
    f = open('train-bel.txt', 'r', encoding='utf-8')
    line = f.read()
    count = 0
    for i in line.split():
        if wordToVekt(i)[0] == 0:
            #print(str(wordToVekt(i)))
            continue
        count += 2
        print(count)
        outX.write(listToStr(wordToVekt(i)) + ':')
        outX.write(listToStr([koef[random.randint(0, 2)] for i in range(10)]) + ':')
        outX.write(listToStr([koef[random.randint(0, 2)] for i in range(10)]) + ':')

        #outX.write(listToStr([random.randint(1, 32) for i in range(8)]) + ':')
        print(str(wordToVekt(i)))
    f.close()

#createSet()
X = getSet()
count = len(X)
Y = np.zeros(count)
for i in range(0, count - 1, 3):
    #print(i, Y[i])
    Y[i] = 1
    #print(i, Y[i])


#print(Y)

print(Y[0:100])
def Nmin(mas, k):
    for i in range(0, k - 2):
        print(mas, k)
        mas.remove(min(mas))
    return min(mas)


def classifyKNN (X, Y, test, k, count):
    def dist(a, b):
        #print(b)
        ans = 0
        for i in range(0, len(a)):
            if (i + 1 == len(a)) or (a[i] == 0 and a[i + 1]):
                continue
            ans += (a[i] - int(b[i]))**2
        return math.sqrt(ans)
    distances = []
    for i in range(0, count - 1):
        distances.append([dist(test, X[i]), Y[i]])
    #outY.write(str(sorted(distances)))
    countYes = 0
    countNo = 0
    distances.sort()
    new_dist = [el for el, _ in groupby(distances)]
    #print(new_dist)
    for i in range(0, k + 1):
        if new_dist[i][1] == 1:
            countYes += 1
        else:
            countNo += 1
    #print(countNo, countYes)
    return countYes >= countNo


if classifyKNN(X, Y, wordToVekt("Алесь"), 7, count):
    print("это слово")
else:
    print("это не слово")

ans = ""
flag = 0
length = 6
allin = open("test-bel.txt", "r", encoding='utf-8')

bel = allin.read()
i = 0
stop = len(bel)
allin.close()
print(bel)
otv = open("ans.txt", "w")
kek = ""
print(bel[1:7])
while i < stop:
    print(i/stop)
    for j in range(length, 11):
        #print(str[i: i + j])
        for k in range(i, i + j):
            if bel[k] not in alphabet:
                #print(bel[k])
                ans = bel[i: k + 1] + " "
                otv.write(ans)
                print(ans)
                kek += ans
                i = (k + 1)
                length = 5
                #print("otveeet tochka:")
                #print(ans)
                flag = 1
                break
        if flag:
            break
        if classifyKNN(X, Y, wordToVekt(bel[i: i + j]), 7, count):
            flag = 1
            length = 5
            #print(bel[i: i + j])
            ans = bel[i: i + j] + " "
            otv.write(ans)
            print(ans)
            kek += ans
            i += j
            #print("otveeet:")
            #print(ans)
            break
    if flag:
        flag = 0
        continue
    else:
        length -= 1
outX = open("X.txt", "w")
print(kek)
outX.write(kek)
