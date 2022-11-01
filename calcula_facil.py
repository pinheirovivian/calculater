custo_mensal = float(input("Quanto você gasta de matéria prima mensalmente? "))
valor_total = float(input("Qual a média do seu ganho mensal? "))
lucro = valor_total-custo_mensal
if lucro>0:
	print("Seu lucro mensal é de R$%.2f" %lucro)
elif lucro<0:
	print("Seu prejuízo mensal é de R$%2.f" %(abs(lucro)))
else:
	print("Seus lucros foram iguais as suas despesas")
reserva = lucro*0.2
if reserva>0:
	print("Pelas nossas análises recomendamos guardar o valor de R$%.2f do seu lucro para sua reserva de emergência" %reserva)
else:
	print("Pelo seu saldo recomendamos que não tenha reserva")