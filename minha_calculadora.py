def soma(a, b):
    return a + b

def subtracao(a,b):
    return a - b

def main():
    calculo = input("ad ou sub: ")
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
    else:
        print("Operação inválida.")
main()