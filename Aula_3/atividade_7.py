# Exercício_7

d_mes = int(input("Digite o dia do mês (1 a 30):\n"))
d_semana = input("Digite o dia da semana (segunda a domingo):\n")

if d_mes >= 5 and d_mes <= 10:
    if d_semana != "domingo" and d_semana != "sabado":
        print("Hoje é o dia do pagamento!\n")
    else:
        print("O pagamento será feito em um dia útil!\n")
elif d_mes > 10:
    print("O dia do pagamento já passou!\n")
else:
    print("O dia do pagamento ainda não chegou!\n")