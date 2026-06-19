import time
import os

# Iniciei fixando as informações
usuario = {
"nome" : "Feliciana",
"senha" : "1234",
"saldo" : 5000.00,
"historico" : []
}   

# Criei a função para limpar a tela
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear") 

# Início do fluxo de usuário
print("=== Bem-vindo ao serviço de banco ===")

resposta = int(input("Já tem uma conta?\n1- Sim\n2- Não\nSelecione: "))

if resposta == 1:
    nome_utilizador = str(input("Digite o seu nome\n")).strip()
    senha_do_utilizador = str(input("Digite sua senha: "))
    if nome_utilizador == usuario['nome'] and senha_do_utilizador == usuario["senha"]:
        print(f"Autenticação feita com sucesso! Bem-vindo(a) {nome_utilizador}")
        time.sleep(2)
        limpar_tela()
        while True:
            print("-" * 25)
            opcao = int(input("1- Ver saldo\n2- Levantar\n3- Ver histórico\n4- Sair\nSelecione: "))
            if opcao == 1:
                print(f"O seu saldo contabilístico: {usuario["saldo"]:.2f} Kz")
            elif opcao == 2:
                valor = float(input("Digite o valor que deseja levantar: "))
                if valor <= usuario["saldo"]:
                    usuario["saldo"] -= valor
                    usuario["historico"].append(valor)
                    print("Processando..")
                    time.sleep(1)
                    print("Operação realizada com sucesso!")
                    time.sleep(0.5)
                    limpar_tela()
                else:
                    print("Saldo insuficiente!")
            elif opcao == 3:
                if not usuario["historico"]:
                    print("Não foi realizado nenhuma operação!")
                else:
                    print("O seu histórico de levantamentos")
                    for usuario["historico"] in usuario["historico"]:
                        print(f"{usuario["historico"]:.2f} Kz")
            elif opcao == 4:
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