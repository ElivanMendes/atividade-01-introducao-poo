value = float(input("Informe um Valor: "))

total_payable = value - (value * 0.1)
installment_value = value / 3
commission = total_payable * 0.05

print("Total a Pagar com Desconto: R$ %.2f" % total_payable)
print("Valor das Parcelas em 3x: R$ %.2f" % installment_value)
print("Comissão da Venda a Vista: R$ %.2f" % commission)
