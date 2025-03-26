# Ex.1

num1 = int(input("Insira um número:\n"))
num2 = int(input("Insira um número:\n"))
dia = str(input("Digite o dia da semana:\n"))

if num1 > num2 and dia == 'quarta':
    print("Número 1 é maior e hoje é quarta-feira!\n")
elif num1 > num2:
    print("O número 1 é maior e hoje não é quarta-feira!\n")
elif num1 == num2:
    print("Os números são iguais!\n")
else:
    print("Número 2 é maior!\n")        