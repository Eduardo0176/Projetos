print("=== Calculadora de Consumo Elétrico ===")
aparelho=input("Digite o nome do aparelho: ")
potencia=float(input("Digite a potência do aparelho em watts (W): "))
horas_dia=float(input("Digite o tempo médio de uso (Em horas): "))
consumo_mensal=(potencia*horas_dia*30)/1000
tarifa=0.75
custo_mensal=tarifa*consumo_mensal
print("\n===resultado===")
print(f"aparelho: {aparelho}")
print(f"consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"custo estimado: R$ {custo_mensal:.2f}/mês")