import math

def quadrado(x):
    raiz = int(math.sqrt(x))
    return raiz*raiz == x

def fibonacci(num):
    return quadrado(5*num*num + 4) or quadrado(5*num*num - 4)

if __name__=='__main__':
    print("verificando se faz parte da sequencia")
num = int(input('Insira o valor: '))

if(fibonacci(num)):
    print(f"{num} pertence a sequencia")
else:
    print(f"{num} nao pertence a sequencia")

