# Iniciei fixando as informações
usuario = {
"nome" : "Feliciana",
"senha" : "1234",
"saldo" : 5000.00
}

# Início do fluxo de usuário
print("===Bem-vindo ao serviço de banco===")

resposta = int(input("Já tem uma conta?\n1- Sim\n2- Não\nSelecione: "))

if resposta == 1:
    nome_utilizador = str(input("Digite o seu nome\n")).strip()
    senha_do_utilizador = str(input("Digite sua senha: "))
    if nome_utilizador == usuario["nome"] and senha_do_utilizador == usuario["senha"]:
        print(f"Autenticação feita com sucesso! Bem-vindo(a) {nome_utilizador}")
        while True:
            print("-" * 65)
            opcao = int(input("1- Ver saldo\n2- Levantar\n3- Sair\nSelecione: "))
            if opcao == 1:
                print(f"O seu saldo contabilístico: {usuario["saldo"]:.2f} Kz")
            elif opcao == 2:
                valor = float(input("Digite o valor que deseja levantar: "))
                if valor <= usuario["saldo"]:
                    usuario["saldo"] = usuario["saldo"] - valor
                    print("Operação realizada com sucesso!")
                else:
                    print("Saldo insuficiente!")
            elif opcao == 3:
                print("Saindo..")
                break
            else:
                print("Opção inválida!")
    else:
        print("Nome ou senha incorretos! Tente mais tarde")
elif resposta == 2:
    print("Dirija-se a um banco mais próximo!")
else:
     print("Opção inválida!")