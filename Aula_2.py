# Ex.1

# Estrutura de entrada

variavel_A = 20
variavel_B = 10

# Estrutura de saída

print(f'Valor da variável A é {variavel_A}')
print(f'Valor da variável B é {variavel_B}')

# Estrutura de condição

if variavel_A > variavel_B:
    print("A é maior que B")
elif variavel_A == variavel_B:
    print("A e B são iguais!")
else:
    print("B é maior que A")
    
    

# Ex.2 - Estrutura com input para o usuário

var_A = float(input("Insira o valor de A:\n"))
var_B = float(input("Insira o valor de B:\n"))

# Estrutura de condição

if var_A > var_B:
    print("A é maior que B")
elif var_A == var_B:
    print("A e B são iguais!")
else:
    print("B é maior que A")
    
    
    
# Ex.3 - Variáveis mão numéricas

usuario = str(input("Digite um caractere ou palavra:\n"))
senha = str(input("Digite sua senha:\n"))

print(usuario)
print(senha)


# Ex.4 - Cálculos com variáveis constantes e variáveis com input do usuário

x = 10.5
resultado = (2*x) + 10
print(resultado)


# Ex.5

x1 = float(input("Digite um valor:\n"))
resultado_1 = (2*x1) + 10
print(resultado_1)




# Ex.6 - Crie um algoritmo para calcular o resultado das sequintes equações:
    
# 1) 10x^2 + 2x - 2
# 2) 5x^2 + 3y + 5
# 3) 10x^2 + 4x^2 - 2z^2

# Exercício 1:
    
x = float(input("Digite o valor de X:\n"))
y = float(input("Digite o valor de Y:\n"))
z = float(input("Digite o valor de Z:\n"))

resultado = 10*(x**2) + (2*x) -2

print(resultado)
          

# Exercício 2:

resultado_2 = 5*(x**2) + (3*y) + 5

print(resultado_2)


# Exercício 3:

resultado_3 = 10*(x**2) + 4*(y**2) - 2*(z**2)

print(resultado_3)