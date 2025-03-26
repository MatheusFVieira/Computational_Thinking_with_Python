# Exercício_4

num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))

op = str(input("Digite o operador da conta (+, -, *, /):\n"))

if op == '+':
    soma = num1 + num2
    print(f'Soma é {soma}')
elif op == '-':
    sub = num1 - num2
    print(f'Subtração é {sub}')
elif op == '*':
    multi = num1 * num2
    print(f'Multiplicação é {multi}')
elif op == '/':
    div = num1 / num2
    print(f'Divisão é {div}')
else:
    print("Digite uma opção válida! (+, -, *, /)")