import random
import sympy

message = "Hello World!!!".encode('utf8')


def generateSimpleNumb(minRange, maxRange):
    randNumb = random.randint(minRange, maxRange)
    while not sympy.isprime(randNumb):
        randNumb = random.randint(minRange, maxRange)
    else:
        return randNumb


def generateKey():
    p = generateSimpleNumb(100, 1000)
    q = generateSimpleNumb(100, 1000)
    n = p * q
    functionEuler = (p - 1) * (q - 1)
    d = simplyTwoNum(functionEuler)
    e = int(((n ** 2) + 1) / d)

    print("Открытый ключ:", e, n)
    print("Закрытый ключ:", d, n)


def simplyTwoNum(main_num):
    lmain_div = []
    for num in range(1, main_num):
        if main_num % num == 0:
            lmain_div.append(num)
    print(lmain_div[-1])
    return lmain_div[-1]


generateKey()
