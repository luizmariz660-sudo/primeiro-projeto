nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horasDia = float(input("Digite o tempo médio de uso diário em horas: "))

consumoMensal = (potencia * horasDia * 30) / 1000

print(f"\nAparelho: {nome}")
print(f"Consumo mensal: {consumoMensal:.2f} kWh")
