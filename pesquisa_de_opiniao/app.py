
TOTAL_ENTREVISTADOS = 50

qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

for entrevistado in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {entrevistado} de {TOTAL_ENTREVISTADOS} ---")

    nome = input("Nome: ")

    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Idade inválida! Digite um número inteiro.")

    while True:
        try:
            opiniao = int(input(
                "Avalie o atendimento (1-EXCELENTE, 2-BOM, 3-RUIM): "
            ))
            if opiniao in (1, 2, 3):
                break
            else:
                print("Opção inválida! Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite um número (1, 2 ou 3).")

    if opiniao == 1:
        qtd_excelente += 1
        opiniao_texto = "EXCELENTE"
    elif opiniao == 2:
        qtd_bom += 1
        opiniao_texto = "BOM"
    else:
        qtd_ruim += 1
        opiniao_texto = "RUIM"

    print(f"Registrado: {nome}, {idade} anos, avaliou como {opiniao_texto}.")

print("\n===== RESULTADO DA PESQUISA =====")
print(f"Total de entrevistados: {TOTAL_ENTREVISTADOS}")
print(f"Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"Quantidade de respostas RUIM: {qtd_ruim}")
print(f"Quantidade de respostas BOM: {qtd_bom}")