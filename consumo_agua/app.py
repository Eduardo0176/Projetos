print(input("Olá, estamos fazendo fazendo uma pesquisa de consumo de água por imóvel, primeiro, nos informe seu nome:"))
imóvel=input("Digite o tipo do imóvel entre as opções:comercial, apartamento e casa: ")
consumo=float(input("Digite o consumo de água em m3: "))
if imóvel =="comercial":
    print("Tarifa comercial aplicada-consulte o plano corporativo.")
elif imóvel =="apartamento" and consumo <10:
    print("Consumo econômico–excelente controle de água!")
elif imóvel in ("apartamento", "casa") and consumo <25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos")