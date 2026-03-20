print("Calcule seu consumo de energia eletrica")
equipamento = input("digite o nome do equipamento usado:")
potencia = float(input("digite a potencia do equipamento em watts:"))
tempo = float(input("qual uso do equipamento em horas por dia:"))
consumoMensal = (potencia * tempo * 30) / 1000
print(" o consumo mensal do equipamento, " + equipamento + " é de " + str(consumoMensal) + " kwh")