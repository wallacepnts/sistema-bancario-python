print(
    '''
+--------------------------------+
|             Pybank             |
+--------------------------------+
| 1. Depósito                    |
| 2. Saque                       |
| 3. Extrato                     |
| 4. Sair                        |
+--------------------------------+
'''
)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        valor = float(input('Digite o valor do depósito: R$ '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 2:
        valor = float(input('Digite o valor do saque: R$ '))

        if valor > saldo:
            print('Não será possível sacar o dinheiro por falta de saldo.')

        elif valor > limite:
            print(f'O limite de saque é de R$ {limite:.2f}')

        elif numero_saques >= LIMITE_SAQUES:
            print(f'Você atingiu o limite diário de {LIMITE_SAQUES} saques.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')

    elif opcao == 3:
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == 4:
        print('Obrigado por usar nossos serviços.')
        break

    else:
        print('Opção invalida')
