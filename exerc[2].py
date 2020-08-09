#Faça um programa que leia um nome de usuário e a sua senha e não
#aceite a senha igual ao nome do usuário, mostrando
#uma mensagem de erro e voltando a pedir as informações.

senha = 0
login = 0

while login == senha:
    login = (input("Informe o login: "))
    senha = (input("Informe a senha: "))

    if login == senha:
        print('inválido, A senha não pode ser o mesmo que o login!')

    else:
	    print("cadastrado efetuado com sucesso")