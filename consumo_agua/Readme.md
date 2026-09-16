# 💧 Análise de Consumo de Água por Imóvel

Script em Python para coletar dados de consumo de água de um imóvel e classificar o consumo de acordo com o tipo de imóvel (comercial, apartamento ou casa), alertando sobre consumo excessivo.

## 📋 Descrição

Este programa simples via terminal solicita ao usuário:
- Nome
- Tipo de imóvel (`comercial`, `apartamento` ou `casa`)
- Consumo de água em m³

E retorna uma classificação com base em regras de negócio simples, indicando se o consumo está dentro do esperado ou se está excessivo.

## ⚙️ Como funciona

O script avalia o consumo seguindo esta lógica:

| Tipo de imóvel | Condição de consumo | Resultado |
|---|---|---|
| Comercial | — | Tarifa comercial aplicada, consulte o plano corporativo |
| Apartamento | consumo < 10 m³ | Consumo econômico — excelente controle de água |
| Apartamento ou Casa | consumo < 25 m³ | Consumo moderado — dentro do padrão residencial |
| Qualquer outro caso | consumo ≥ 25 m³ | Consumo excessivo — adote medidas de economia e verifique vazamentos |

## 🚀 Como executar

### Pré-requisitos

- [Python 3.6+](https://www.python.org/downloads/) instalado

### Passos

1. Clone este repositório ou baixe o arquivo `.py`:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Execute o script:
   ```bash
   python consumo_agua.py
   ```

3. Responda às perguntas no terminal:
   ```
   Olá, estamos fazendo uma pesquisa de consumo de água por imóvel, primeiro, nos informe seu nome: Maria
   Digite o tipo do imóvel entre as opções: comercial, apartamento e casa: apartamento
   Digite o consumo de água em m3: 8
   ```

4. Veja o resultado:
   ```
   Consumo econômico–excelente controle de água!
   ```

## 🧪 Exemplos de uso

**Exemplo 1 — Apartamento com consumo baixo**
```
Tipo de imóvel: apartamento
Consumo: 8 m³
Resultado: Consumo econômico–excelente controle de água!
```

**Exemplo 2 — Casa com consumo moderado**
```
Tipo de imóvel: casa
Consumo: 20 m³
Resultado: Consumo moderado – dentro do padrão residencial.
```

**Exemplo 3 — Consumo excessivo**
```
Tipo de imóvel: casa
Consumo: 40 m³
Resultado: Consumo excessivo – adote medidas de economia e verifique vazamentos
```

## 🛠️ Possíveis melhorias futuras

- [ ] Validar se o tipo de imóvel digitado é uma das opções válidas
- [ ] Normalizar entrada do usuário (remover espaços, ignorar maiúsculas/minúsculas)
- [ ] Adicionar cálculo de tarifa em R$ com base no consumo
- [ ] Registrar histórico de consumo em arquivo (CSV/JSON) para comparação mensal
- [ ] Criar interface gráfica ou web para facilitar o uso

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

## ✍️ Autor

Desenvolvido como parte de um estudo/pesquisa sobre consumo de água por imóvel.
