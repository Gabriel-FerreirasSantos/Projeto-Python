import math

def contademais():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s1 = (a + b)
    print('{} + {} = {}'.format(a, b, s1))

def contademenos():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s2 = (a - b)
    print('{} - {} = {}'.format(a, b, s2))    

def contadedividir():
    a = float(input('Digite um numero: '))
    b = float(input('Digite outro: '))
    s3 = (a / b)
    print('{:.1f} ÷ {:.1f} = {:.1f}'.format(a, b, s3))

def contademutiplicação():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro: '))
    s4 = (a * b)
    print('{:.1f} x {:.1f} = {:.1f}'.format(a, b, s4)) 

def contaderaiz():
    num = float(input("Digite um numero:\n"))
    raiz = math.pow(num, 1/2)
    print('{:.1f} √ = {:.1f}'.format(num, raiz)) 
    

def contadepotenciação():
    a = float(input('Digite um numero: '))
    b = float(input('Digite outro: '))
    s6 = (a ** b)  
    print('{:.1f}ª  {:.1f}ª = {:.1f}ª'.format(a, b, s6)) 
                      