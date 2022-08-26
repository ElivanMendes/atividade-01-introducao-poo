hour_value = float(input("Informe o Valor da Hora de Trabalho: "))
worked_hours = float(input("Informe as Horas Trabalhadas: "))

amount_paid = hour_value * worked_hours
amount_paid += amount_paid * 0.1

print("Valor a ser Pago: R$ %.2f" % amount_paid)
