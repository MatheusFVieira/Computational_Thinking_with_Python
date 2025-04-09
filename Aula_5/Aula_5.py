# REVISÃO

# Ex.1 Estruturas de entrada e saída

var_1 = int(input("Digite um número inteiro: "))
var_2 = float(input("Digite um número não inteiro: "))
var_3 = str(input("Digite uma palavra: "))

print(f"O número inteiro é {var_1}")
print(f"O número não inteiro é {var_2:.02f}")
print(f"A palavra é {var_3}")


# Ex.2

nome = str(input("Digite seu nome: "))

if nome == 'fiap':
    rm = int(input("Digite seu RM: "))
    if rm == 123456:
        print("Acesso permitido!")
    else:
        print("RM está incorreto!")
        rm = int(input("Digite seu RM: "))
        if rm == 123456:
            print("Acesso permitido!")
        else:
            print("RM incorreto, acesso bloqueado!")


# Ex.3

nome = str(input("Digite seu nome: "))
rgm = int(input("Digite seu RGM: "))

if nome == 'fiap' or rgm == 1234:
    print("Acesso permitido!")



# Ex.4

forma = str(input("Digite qual forma geométrica você quer calcular a área e o perímetro:  "))

if forma == 'quadrado' or forma == 'retangulo':
    lado1 = float(input("Digite o primeiro lado: "))
    lado2 = float(input("Digite o segundo lado: "))
    area = lado1 * lado2
    perimetro = (lado1*2) + (lado2*2)
    print(f"A área é: {area:.02f}")
    print(f"O perímetro é: {perimetro:.02f}")
elif forma == 'circulo':
    raio = float(input("Digite o raio do seu circulo: "))
    area = 3.14 * (raio**2)
    perimetro = (2 * 3.14) * raio
    print(f"A área do seu circulo é {area:.02f}")
    print(f"O perímetro do seu circulo é: {perimetro:.02f}")
elif forma == 'triangulo':
    base = float(input("Digite o valor da base do triangulo: "))
    altura = float(input("Digite o valor da altura do triangulo: "))
    hipo = float(input("Digite o valor da hipotenusa do triangulo: "))
    area = (base * altura) / 2
    perimetro = base + altura + hipo
    print(f"A área do seu triangulo é {area:.02f}")
    print(f"O perímetro do seu triangulo é: {perimetro:.02f}")
else:
    print("Escolha uma opção entre (quadrado, retangulo, circulo, triangulo")