salario_mensal = input("Salário? ")
horas_trabalhadas = input("Horas trabalhadas? ")

valor_hora = float(salario_mensal) / float(horas_trabalhadas)

print("O valor da sua hora de trabalho é: R$ ", round(valor_hora,2))