# Exercício_8

usuarios = {}

while True:
    op = input("Digite 1 para criar um usuário, 2 para acessar sua conta ou 3 para sair do sistema\n")

    if op == "3":
        break
    elif op == "1":
        user = input("Digite o usuário que deseja criar:\n")
        if user in usuarios:
            print("Usuário já existe! Escolha outro nome.\n")
        else:
            senha = input("Crie a senha para esse usuário:\n")
            usuarios[user] = senha
            print("Usuário criado\n")
    elif op == "2":
        userT = input("Digite o seu Usuário:\n")
        if userT in usuarios:
            senhaT = input("Digite a sua senha:\n")
            if senhaT == usuarios[userT]:
                print("Bem-vindo ao sistema!\n")
            else:
                print("Senha incorreta!\n")
        else:
            print("Usuário não encontrado!\n")
    else:
        print("Digite uma opção válida!\n")
