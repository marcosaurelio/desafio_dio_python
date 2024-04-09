menu = """
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == "d":
    valor_deposito = float(input("Valor do depósito: "))
    if valor_deposito > 0:
      saldo += valor_deposito
      extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
      print("Valor inválido. Depósito não realizado!!!")
    
  elif opcao == "s":
    valor_saque = float(input("Valor do saque: "))
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Saldo insuficiente!!!")
    elif excedeu_limite:
      print("Valor do saque excede limite.")
    elif excedeu_saques:
      print("Quantidade diária de saque excedida.")
    elif valor_saque > 0:
      saldo -= valor_saque
      extrato += f"Saque:    R$ {valor_saque*-1:.2f}\n"
      numero_saques += 1
    else:
      print("Valor é inválido. Saque não realizado!!!")

  elif opcao == "e":
    print("======================= EXTRATO =======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================================================")
  elif opcao == "q":
    break
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")