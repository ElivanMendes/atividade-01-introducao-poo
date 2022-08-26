worked_days = float(input("Informe o Numero de Dias Trabalhados: "))

gross_amount = worked_days * 30.0
net_amount = gross_amount - (gross_amount * 0.08)

print("Quantia Liquida Recebida: R$ %.2f" % net_amount)
