import random
import sympy


# Функция для генерации ключей шифрования.
# Сперва находим два простых числа.
# Далее находим модуль seed (нужен в дальнейшем для шифрования)
# Создаем закрытый ключ, для этого находим функцию Эйлера
# и взаимно простое число с seed.
# Находим открытый ключ, который находится из алгоритма Евклида
# Функция возвращает массив из открытого ключа и закрытого ключа.
# В свою очередь ключ состоит из самого ключа и модуля seed.
def generateKey():
    firstSimpleNumb = generateSimpleNumb(100, 1000)
    secondSimpleNumb = generateSimpleNumb(100, 1000)
    seed = firstSimpleNumb * secondSimpleNumb
    functionEuler = (firstSimpleNumb - 1) * (secondSimpleNumb - 1)
    privateKey = [simplyTwoNum(functionEuler), seed]
    publicKey = [gcd_rem_division(privateKey[0], seed), seed]

    return [publicKey, privateKey]


# Функция для генерации случайных простых чисел.
# Принимает в себя два значения, минимальное и максимальное значения
# которые являются диапазоном для случайного числа.
# Далее цикл проверяет, является ли случайное число, простым
# Если нет, то генерируем заново и снова проверяем
# Если да, то возвращаем нужное число
def generateSimpleNumb(minRange, maxRange):
    randSimpleNumb = random.randint(minRange, maxRange)
    while not sympy.isprime(randSimpleNumb):
        randSimpleNumb = random.randint(minRange, maxRange)
    else:
        return randSimpleNumb


def gcd_rem_division(num1, num2):
    while num1 != 1 and num2 != 1:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


# Функция для нахождения взаимно простых чисел.
# Принимает в себя число для которого ммы находим взаимно простое число.
# Возвращает наибольшее взаимно простое число.
def simplyTwoNum(mainNum):
    numDiv = []
    for num in range(1, mainNum):
        if mainNum % num == 0:
            numDiv.append(num)
    return numDiv[-1]


def encryption(publicKey, seed):
    pass


def decryption(secretKey, seed):
    pass
