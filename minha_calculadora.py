def soma(a, b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplica(a, b):
    return a * b

def main():
    calculo = input("ad, sub ou multi: ")
    if calculo == "ad":
        x = int(input('x? '))
        y = int(input('y? '))
        s = soma(x, y)
        print(f' Soma = {s}')
    elif calculo == "sub":
        x = int(input('x? '))
        y = int(input('y? '))
        sub = subtracao(x, y)
        print(f' Subtração = {sub}')
    elif calculo == "multi":
        x = int(input("x? "))
        y = int(input('y? '))
        multi = multiplica(x, y)
        print(f' Multiplicação = {multi}')
    else:
        print("Operação inválida.")
main()