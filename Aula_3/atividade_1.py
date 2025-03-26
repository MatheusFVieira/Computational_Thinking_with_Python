# Exercício_1

velocidade = int(input("Digite a sua velocidade em (KM/h):\n"))

if velocidade > 80:
    multa = (velocidade - 80) * 50
    print(f'Você está acima da velocidade perimitida!\nO valor da sua multa é de R${multa},00')
else:
    print("Você está dentro da velocidade permitida e não receberá multa!")