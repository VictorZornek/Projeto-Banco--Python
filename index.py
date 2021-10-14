import os                                                       # Importação da biblioteca os para usar funcionalidades de sistema operacional
from datetime import datetime                                   # Importação da biblioteca datetime para usar as funcionalidade de dia/mês/ano e hora/min

def novaConta():                                                # Criação da função de criar nova conta
    data_hora = datetime.now()                                  # Chamada da biblioteca datetime            

    nome = input("Digite o nome: ")                             # Pede o nome do usuário
    cpf = input("Digite o CPF: ")                               # Pede o CPF do usuário
    
    if os.path.isfile(cpf + ".txt"):                            # Verifica se o CPF digitado já esta cadastrado, se já existir um arquivo com aquele CPF:
        print("Cliente já registrado!")                         # Mostra a mensagem "Cliente já registrado!"
    else:                                                       # Se não estiver cadastrado:
        arquivo = open(cpf+".txt", "w")                         # Abre um novo arquivo com o CPF digitado, com a opção de escrita(write), e armeza dentro da variável arquivo
        arquivo.write("%s\n" % nome)                            # Registra o nome informado no arquivo  
        arquivo.write("%s\n" % cpf)                             # Registra o CPF informado no arquivo

        print("Escolha seu tipo de conta: \n[1] Conta Salário \n[2] Conta Comum \n[3] Conta Plus")          # Menu com as opções de conta para o usuário
        conta = input("Tipo de conta: ")                                                                    # Pede a escolha de conta para o usuário

        if conta == "1":                                        # Se a conta for opção 1:
            arquivo.write("salário\n")                          # Registra "salário" no arquivo como tipo de conta
        if conta == "2":                                        # Se a conta for opção 2:
            arquivo.write("comum\n")                            # Registra "comum" no arqivo como tipo de conta
        if conta == "3":                                        # Se a conta for opção 3:
            arquivo.write("plus\n")                             # Registra "plus" no arquivo como tipo de conta

        senha = input("Crie sua senha: ")                       # Pede a criação de uma senha para o usuário
        arquivo.write("%s\n" % senha)                           # Registra a senha informada no arquivo

        valorInicial = float(input("Valor inicial da conta: R$ "))                                                                                          # Pede um valor inicial da conta para o usuário (saldo inicial)
        arquivo.write("Data: {0} + {1:.2f} Tarifa: 0.00 Saldo: {2:.2f}\n".format(data_hora.strftime("%Y-%m-%d %H:%M"), valorInicial, valorInicial))         # Registra no arquivo as informação do deposito inicial, com ano/mês/dia e hora/min, valor da tarifa, e o valor inicial (informações que serão utilizadas no extrato)
        arquivo.write("%.2f\n" % valorInicial)                                                                                                              # Registra no arquivo o valor inicial (saldo inicial)

        arquivo.close()                                         # Fecha o arquivo

        print()                                                 # Pula uma linha
        print("Sua conta foi criada com sucesso!")              # Mostra a mensagem "Sua conta foi criada com sucesso!"

def apagaConta():                                               # Criação da função de apagar uma conta
    verificaCPF = input("Digite seu CPF: ")                     # Pede o nome do usuário
    verificaSenha = input("Digite sua senha: ")                 # Pede o CPF do usuário    

    if os.path.exists(verificaCPF+".txt"):                      # Verifica se o CPF digitado já esta cadastrado, se já existir um arquivo com aquele CPF:
        arquivo = open(verificaCPF + ".txt", "r")               # Abre um arquivo com o CPF digitado e armazena na variável arquivo,  com a opção de leitura(read)
        info = arquivo.read()                                   # Armazena as infomações do arquivo na variável info
        lista = []                                              # Cria uma lista vazia na variável lista
        lista = info.split()                                    # Armazena as infomações na lista com o metódo split
        arquivo.close()                                         # Fecha o arquivo
        
        if lista[1] == verificaCPF and lista[3] == verificaSenha:       # Verificação se o CPF e senha coincidem, se CPF e senha informados coincidirem com as informações da lista:
            os.remove(verificaCPF+".txt")                               # Utiliza o metódo os.remove para deletar o arquivo solicitado
            print()                                                     # Pula linha
            print("Conta deletada!")                                    # Exibe uma mensagem de "Conta deletada!"
            print()                                                     # Pula linha

        else:                                                   # Se a verificação falhar, se usuário e senha não coincidirem com as informações na lista:
            print()                                             # Pula linha
            print("Usuário ou senha inválidos")                 # Exibe mensagem "Usuário ou senha inválidos"

    else:                                                       # Se o CPF informado, não coincidir com nenhum usuário em nenhum arquivo:
        print()                                                 # Pula linha
        print("Usuário não encontrado")                         # Exibe mensagem "Usuário não encontrado"

def debita():                                                   # Criação da função debita
    data_hora = datetime.now()                                  # Uitliza a biblioteca datetime para utilizar as informações de dia/mês/ano e hora/min, em que a ação vai ser utilizada, armaneza na variável data_hora
    cpf = input("Digite seu CPF: ")                             # Pede um CPF para o usuário
    senha = input("Digite sua senha: ")                         # Pede a senha para o usuário
    
    if os.path.exists(cpf+".txt"):                              # Verifica se o CPF digitado já é um CPF cadastrado, se já existir um arquivo com aquele CPF:
        arquivo = open(cpf+".txt", "r")                         # Abre um arquivo com o CPF digitado e armazena na variável arquivo,  com a opção de leitura(read)
        info = arquivo.read()                                   # Armazena as infomações do arquivo na variável info
        lista = []                                              # Cria uma lista vazia na variável lista
        lista = info.split()                                    # Armazena as infomações na lista com o metódo split
        arquivo.close()                                         # Fecha o arquivo

        if lista[1] == cpf and lista[3] == senha:                                               # Verificação se o CPF e senha coincidem, se CPF e senha informados coincidirem com as informações da lista:
            saldo = float(lista[-1])                                                            # Armazena o valor atual do saldo na variável saldo
            valor = float(input("Digite o valor que deseja debitar da conta: R$ "))             # Pede ao usuário o valor que ele deseja debitar da conta e armazena na variável valor
            
            if lista[2] == "salário":                               # Se a informação na lista referente ao tipo da conta for igual a "salário":
                tarifa = valor * 0.05                               # Realiza o cálculo da tarifa da conta salário (taxa de 5%) por débito, armazena na variável tarifa
                valor_taxa = valor + tarifa                         # Realiza o cálculo do valor + tarifa, que será o valor debitado da conta, armazena na variável valor_taxa

                if saldo >= valor_taxa:                             # Se o saldo for maior ou igual ao valor_taxa:
                    saldo = float(saldo - valor_taxa)               # Realiza a operação do saldo - valor_taxa, transformando o resultado em uma varíavel do tipo float e armazena o resultado na variável saldo

                    novo_saldo = open(cpf+".txt", "a")                                                                                                                          # Abre o arquivo com o CPF digitado, com a opção de append("a"), e armazena na variável novo_saldo                  
                    novo_saldo.write("Data: {0} - {1:.2f} Tarifa: {2:.2f} Saldo: {3:.2f}\n".format(data_hora.strftime("%Y-%m-%d %H:%M"), valor, tarifa, saldo))                 # Registra no arquivo as informação do débito na conta, com ano/mês/dia e hora/min, valor da tarifa, e o valor do saldo atual após o débito (informações que serão utilizadas no extrato)
                    saldo = str(saldo)                                                                                                                                          # Transforma a variável saldo em string
                    novo_saldo.write(saldo+"\n")                                                                                                                                # Registra a variável saldo no arquivo
                    novo_saldo.close()                                                                                                                                          # Fecha o arquivo novo_saldo

                    print()                                         # Pula linha
                    print("Retirada realizada com sucesso!")        # Exibe a mensagem "Retirada realizada com sucesso!"
                
                else:                                               # Se o saldo for menor que o valor_taxa:
                    print()                                         # Pula linha
                    print("Saldo insuficiente")                     # Exibe a mensagem "Saldo insuficiente"

            elif lista[2] == "comum":                               # Se a informação na lista referente ao tipo da conta for igual a "comum":
                tarifa = valor * 0.03                               # Realiza o cálculo da tarifa da conta comum (taxa de 3%) por débito, armazena na variável tarifa
                valor_taxa = valor + tarifa                         # Realiza o cálculo do valor + tarifa, que será o valor debitado da conta, armazena na variável valor_taxa

                if saldo - valor_taxa >= -500:                      # Se o saldo - valor_taxa for maior ou igual a -500 (valor máximo que o usuário pode ficar negativo nesse tipo de conta):
                    saldo = float(saldo - valor_taxa)               # Realiza a operação do saldo - valor_taxa, transformando o resultado em uma varíavel do tipo float e armazena o resultado na variável saldo

                    novo_saldo = open(cpf+".txt", "a")                                                                                                                          # Abre o arquivo com o CPF digitado, com a opção de append("a"), e armazena na variável novo_saldo
                    novo_saldo.write("Data: {0} - {1:.2f} Tarifa: {2:.2f} Saldo: {3:.2f}\n".format(data_hora.strftime("%Y-%m-%d %H:%M"), valor, tarifa, saldo))                 # Registra no arquivo as informação do débito na conta, com ano/mês/dia e hora/min, valor da tarifa, e o valor do saldo atual após o débito (informações que serão utilizadas no extrato)
                    saldo = str(saldo)                                                                                                                                          # Transforma a variável saldo em string
                    novo_saldo.write(saldo+"\n")                                                                                                                                # Registra a variável saldo no arquivo
                    novo_saldo.close()                                                                                                                                          # Fecha o arquivo novo_saldo

                    print()                                         # Pula linha
                    print("Retirada realizada com sucesso!")        # Exibe a mensagem "Retirada realizada com sucesso!"
                
                else:                                               # Se o saldo - valor taxa for menor que o -500:
                    print()                                         # Pula linha
                    print("Saldo insuficiente")                     # Exibe a mensagem "Saldo insuficiente"

            elif lista[2] == "plus":                                # Se a informação na lista referente ao tipo da conta for igual a "plus":
                tarifa = valor * 0.01                               # Realiza o cálculo da tarifa da conta plus (taxa de 1%) por débito, armazena na variável tarifa
                valor_taxa = valor + tarifa                         # Realiza o cálculo do valor + tarifa, que será o valor debitado da conta, armazena na variável valor_taxa

                if saldo - valor_taxa >= -5000:                     # Se o saldo - valor_taxa for maior ou igual a -5000 (valor máximo que o usuário pode ficar negativo nesse tipo de conta):
                    saldo = float(saldo - valor_taxa)               # Realiza a operação do saldo - valor_taxa, transformando o resultado em uma varíavel do tipo float e armazena o resultado na variável saldo

                    novo_saldo = open(cpf+".txt", "a")                                                                                                                          # Abre o arquivo com o CPF digitado, com a opção de append("a"), e armazena na variável novo_saldo
                    novo_saldo.write("Data: {0} - {1:.2f} Tarifa: {2:.2f} Saldo: {3:.2f}\n".format(data_hora.strftime("%Y-%m-%d %H:%M"), valor, tarifa, saldo))                 # Registra no arquivo as informação do débito na conta, com ano/mês/dia e hora/min, valor da tarifa, e o valor do saldo atual após o débito (informações que serão utilizadas no extrato)
                    saldo = str(saldo)                                                                                                                                          # Transforma a variável saldo em string
                    novo_saldo.write(saldo+"\n")                                                                                                                                # Registra a variável saldo no arquivo
                    novo_saldo.close()                                                                                                                                          # Fecha o arquivo novo_saldo

                    print()                                         # Pula linha
                    print("Retirada realizada com sucesso!")        # Exibe a mensagem "Retirada realizada com sucesso!"

                else:                                               # Se o saldo - valor_taxa for menor que -5000
                    print()                                         # Pula linha
                    print("Saldo insuficiente")                     # Exibe a mensagem "Saldo insuficiente"

        else:                                                       # Se a verificação falhar, se usuário e senha não coincidirem com as informações na lista:
            print()                                                 # Pula linha
            print("Usuário ou senha inválidos")                     # Exibe a mensagem "Usuário ou senha inválidos"

    else:                                                           # Se o CPF informado, não coincidir com nenhum usuário em nenhum arquivo:
        print()                                                     # Pula linha
        print("Usuário não encontrado")                             # Exibe a mensagem "Usuário não encontrado"

def deposita():                                                     # Criação da função de depositar
    data_hora = datetime.now()                                      # Uitliza a biblioteca datetime para utilizar as informações de dia/mês/ano e hora/min, em que a ação vai ser utilizada, armaneza na variável data_hora
    cpf = input("Digite o CPF da conta: ")                          # Pede um CPF para o usuário

    if os.path.exists(cpf+".txt"):                                  # Verifica se o CPF digitado já é um CPF cadastrado, se já existir um arquivo com aquele CPF:
        arquivo = open(cpf+".txt", "r")                             # Abre um arquivo com o CPF digitado e armazena na variável arquivo,  com a opção de leitura(read)
        info = arquivo.read()                                       # Armazena as infomações do arquivo na variável info
        lista = []                                                  # Cria uma lista vazia na variável lista
        lista = info.split()                                        # Armazena as infomações na lista com o metódo split
        arquivo.close()                                             # Fecha o arquivo

        if lista[1] == cpf:                                                                     # Se o CPF informado for o mesmo presente na lista:
            novo_arquivo = open(cpf+".txt", "a")                                                # Abre o arquivo com o CPF digitado, com a opção de append("a"), e armazena na variável novo_arquivo
            valor = float(input("Digite o valor que deseja depositar na conta: R$ "))           # Pede o valor que o usuário deseja depositar na conta, sendo ele do tipo float, e armeza esse valor na variável valor

            if valor > 0:                                           # Se o valor for maior que 0:
                saldo = float(lista[-1])                            # tranforma o valor do saldo atual presente na lista em float e, armenza na variável saldo
                novo_saldo = float(saldo + valor)                   # Realiza o cálculo do saldo + valor que foi digitado, e armazena na variável novo_saldo

                novo_arquivo.write("Data: {0} + {1:.2f} Tarifa: 0.00 Saldo: {2:.2f}\n".format(data_hora.strftime("%Y-%m-%d %H:%M"), valor, novo_saldo))             # Registra no arquivo as informação do deposito na conta, com ano/mês/dia e hora/min, valor da tarifa (0.00), e o valor do saldo atual após o deposito (informações que serão utilizadas no extrato)
                novo_saldo = str(novo_saldo)                                                                                                                        # Transforma a variável novo_saldo em string
                novo_arquivo.write(novo_saldo+"\n")                                                                                                                 # Registra a variável novo_saldo no arquivo
                novo_arquivo.close()                                                                                                                                # Fecha o arquivo

                print()                                             # Pula linha
                print("Depósito realizado com sucesso!")            # Exibe mensagem "Depósito realizado com sucesso!"

            else:                                                   # Se o valor digitado (guardado na variável valor) for menor do que 0 (valor negativo): 
                print()                                             # Pula linha
                print("Operação inválida")                          # Exibe mensagem "Operação inválida"

        else:                                                       # Se a informação presente na litsa, for diferente do CPF digitado:
            print()                                                 # Pula linha
            print("CPF inválido")                                   # Exibe mensagem "CPF inválido"

    else:                                                           # Se o CPF informado, não coincidir com nenhum usuário em nenhum arquivo:
        print()                                                     # Pula linha
        print("Usuário não encontrado")                             # Exibe a mensagem "Usuário não encontrado"

def saldo():                                                        # Cria a função saldo, para exibir o saldo atual
    cpf = str(input("Digite seu CPF: "))                            # Pede o CPF do usuário
    senha = str(input("Digite sua senha: "))                        # Pede a senha do usuário

    if os.path.exists(cpf+".txt"):                                  # Verifica se o CPF digitado já é um CPF cadastrado, se já existir um arquivo com aquele CPF:
        arquivo = open(cpf+".txt", "r")                             # Abre um arquivo com o CPF digitado e armazena na variável arquivo,  com a opção de leitura(read)
        info = arquivo.read()                                       # Armazena as infomações do arquivo na variável info
        lista = []                                                  # Cria uma lista vazia na variável lista
        lista = info.split()                                        # Armazena as infomações na lista com o metódo split
        arquivo.close()                                             # Fecha o arquivo

        if lista[1] == cpf and lista[3] == senha:                   # Se a informação do CPF e da senha digitados coincidirem com as informações presentes na lista:
            saldo = lista[-1]                                       # O valor do saldo presente na lista é armazenado na variável saldo
            print()                                                 # Pula linha
            print("Saldo atual: R$", saldo)                         # Exibe a mensagem "Saldo atual: R$" e o valor do saldo atual

        else:                                                       # Se a informação do CPF e da senha digitados não coincidirem com as informações presentes na lista:
            print()                                                 # Pula linha
            print("Usuário ou senha inválidos")                     # Exibe a mensagem "Usuário ou senha inválidos"

    else:                                                           # Se o CPF informado, não coincidir com nenhum usuário em nenhum arquivo:
        print()                                                     # Pula linha
        print("Usuário não encontrado")                             # Exibe a mensagem "Usuário não encontrado"

def extrato():                                                      # Criação da função para exibir o extrato
    cpf = input("Digite seu CPF: ")                                 # Pede o CPF do usuário
    senha = input("Digite sua senha: ")                             # Pede a senha do usuário

    if os.path.exists(cpf+".txt"):                                  # Verifica se o CPF digitado já é um CPF cadastrado, se já existir um arquivo com aquele CPF: 
        arquivo = open(cpf+".txt", "r")                             # Abre um arquivo com o CPF digitado e armazena na variável arquivo,  com a opção de leitura(read)
        info = arquivo.readlines()                                  # Armazena as infomações do arquivo na variável info, utilizando o readlines
        arquivo.close()                                             # Fecha o arquivo
        lista = []                                                  # Cria uma lista vazia na variável lista

        for x in info:                                              # Para x na variável info:
            retira_n = x.strip()                                    # Criação da variavél retira_n com o metódo strip para retirar o \n das informações do arquivo
            lista.append(retira_n)                                  # Faz um append na lista de cada informação

        if lista[1] == cpf and lista[3] == senha:                   # Se a informação do CPF e da senha digitados coincidirem com as informações presentes na lista:
            print()                                                 # Pula linha
            print("Nome: %s" % lista[0])                            # Exibe a mensagem "Nome: " e o nome registrado na lista
            print("CPF: %s" % lista[1])                             # Exibe a mensagem "CPF: " e o CPF registrado na lista
            print("Conta: %s" % lista[2])                           # Exibe a mensagem "Conta: " e o tipo de conta registrado na lista

            for x in range(4, len(lista), 2):                       # Para x no range(começa no índice 5, com tamanho do tamanho da lista, e passo 2):
                print(lista[x])                                     # Mostra as informações de extrato (depositos e débitos) presentes na lista
        
        else:                                                       # Se a informação do CPF e da senha digitados não coincidirem com as informações presentes na lista:
            print()                                                 # Pula linha
            print("Usuário ou senha inválidos")                     # Exibe a mensagem "Usuário ou senha inválidos"

    else:                                                           # Se o CPF infomado, não coincidir com nenhum usuário em nenhum arquivo:
        print()                                                     # Pula linha
        print("Usuário não encontrado")                             # Exibe a mensagem "Usuário não encontrado"

def main():                                                         # Criação da função principal (main), onde terá todas as funções dentro dela
    while True:                                                     # Laço para ficar exibindo o menu e suas funções enquanto True:
        print()                                                     # Pula linha
        print("----- Menu QuemPoupaTem -----")                      # Exibe mensagem "----- Menu QuemPoupaTem -----"
        print()                                                     # Pula linha
        print("1 - Criar nova conta")                               # Exibe mensagem "1 - Criar nova conta", primeira opção do menu
        print("2 - Apagar conta")                                   # Exibe mensagem "2 - Apagar conta", segunda opção do menu
        print("3 - Debita")                                         # Exibe mensagem "3 - Debita", terceira opção do menu
        print("4 - Deposita")                                       # Exibe mensagem "4 - Deposita", quarta opção do menu
        print("5 - Saldo")                                          # Exibe mensagem "5 - Saldo", quinta opção do menu
        print("6 - Extrato")                                        # Exibe mensagem "6 - Extrato", sexta opção do menu
        print()                                                     # Pula linha
        print("0 - Sair")                                           # Exibe mensagem "0 - Sair", sétima opção do menu
        print()                                                     # Pula linha

        opcao = input("Escolha uma das opções: ")                   # Pede para o usuário escolher uma das opções e armazena na variável opcao

        if opcao == "1":                                                    # Se a opção for igual a "1":
            novaConta()                                                     # Chama e realiza a função novaConta()
        elif opcao == "2":                                                  # Se a opção for igual a "2":
            apagaConta()                                                    # Chama e realiza a função apagaConta()
        elif opcao == "3":                                                  # Se a opção for igual a "3":
            debita()                                                        # Chama e realiza a função debita()
        elif opcao == "4":                                                  # Se a opção for igual a "4":
            deposita()                                                      # Chama e realiza a função deposita()
        elif opcao == "5":                                                  # Se a opção for igual a "5":
            saldo()                                                         # Chama e realiza a função saldo()
        elif opcao == "6":                                                  # Se a opção for igual a "6":
            extrato()                                                       # Chama e realiza a função extrato()
        elif opcao == "0":                                                  # Se a opção for igual a "0":
            print("Obrigado por usar QuemPoupaTem! Volte sempre!")          # Exibe a mensagem "Obrigado por usar QuemPoupaTem! Volte sempre!"
            break                                                           # Quebra do laço com o break e encerra o programa
        else:                                                               # Se a opção for diferente de alguns dos números citados acima:
            print("Não é uma opção válida")                                 # Exibe a mensagem "Não é uma opção válida"
        
main()                                                                      # Chama a função main() para realizar o programa