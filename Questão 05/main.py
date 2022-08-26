salary = float(input("Informe seu Salario: "))

gratification = salary * 0.05
tax = salary * 0.07

salary += gratification
salary -= tax

print("Salario a Receber: R$ %.2f" % salary)
