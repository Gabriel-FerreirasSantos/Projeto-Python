import math

def contademais():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s = (a + b)
    print(s)

def contademenos():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s = (a - b)
    print(s)    

def contadedividir():
    a = float(input('Digite um numero: '))
    b = float(input('Digite outro: '))
    s3 = (a / b)
    print(s3)

def contademutiplicação():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s4 = (a * b)
    print(s4)  

def contaderaiz():
    num = float(input("Digite um numero:\n"))
    raiz = math.pow(num, 1/2)
    print('{:.1f}'.format(raiz))

def contadepotenciação():
    a = float(input('Digite um numero: '))
    b = float(input('Digite outro: '))
    s6 = (a ** b)
    print('{:.1f}'.format(s6))                     