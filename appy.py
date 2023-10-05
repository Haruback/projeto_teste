# Solicita ao usuário que insira quanto ganha por hora
ganho_por_hora = float(input("Por favor, insira quanto você ganha por hora: "))

# Solicita ao usuário que insira o número de horas trabalhadas no mês
horas_trabalhadas = float(input("Por favor, insira o número de horas trabalhadas no mês: "))

# Calcula o salário total
salario = ganho_por_hora * horas_trabalhadas

# Imprime o salário total
print("O total do seu salário neste mês é: ", salario)