valor_compra = float(input("Digite o valor da compra: "))
if valor_compra >= 100:
  desconto = valor_compra * 0.1
  valor_final = valor_compra - desconto
  print("Parabens! Voce ganhou um desconto de 10%")
  print("O valor final é R$", valor_final)
else:
  print ("Voce nao ganhou desconto")
  print("O valor final é R$", valor_compra)