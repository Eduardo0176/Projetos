# 📊 Pesquisa de Satisfação — TudoWeb

Programa em **Python** desenvolvido para a empresa de marketing **TudoWeb**, com o objetivo de coletar e analisar o grau de satisfação dos clientes em relação ao atendimento prestado.

## 📝 Descrição

O sistema simula uma pesquisa de opinião aplicada a um grupo de entrevistados. Para cada pessoa, o programa coleta **nome**, **idade** e **opinião sobre o atendimento**, classificando a resposta em uma das três categorias abaixo:

| Código | Avaliação   |
|:------:|-------------|
| 1      | EXCELENTE   |
| 2      | BOM         |
| 3      | RUIM        |

Ao final da coleta, o programa exibe um resumo com a quantidade de respostas em cada categoria.

## ⚙️ Funcionalidades

- ✅ Coleta de dados de **50 entrevistados** através de estrutura de repetição (`for`)
- ✅ Validação de entrada para idade e opinião (evita erros de digitação)
- ✅ Classificação da opinião usando estruturas de decisão (`if` / `elif` / `else`)
- ✅ Exibição do total de respostas **EXCELENTE**, **BOM** e **RUIM** ao final da execução

## 🚀 Como executar

### Pré-requisitos

- [Python 3](https://www.python.org/downloads/) instalado na máquina

### Passo a passo

```bash
# Clone ou baixe o arquivo do projeto
# Acesse a pasta onde o arquivo está salvo
cd caminho/para/o/arquivo

# Execute o programa
python3 pesquisa_satisfacao.py
```

Durante a execução, o programa solicitará, para cada entrevistado:

```
Nome: 
Idade: 
Avalie o atendimento (1-EXCELENTE, 2-BOM, 3-RUIM): 
```

## 🧪 Testando com menos entrevistados

Por padrão, a pesquisa é realizada com **50 entrevistados**. Para realizar testes rápidos (por exemplo, com 10 pessoas), basta alterar a constante no início do arquivo:

```python
TOTAL_ENTREVISTADOS = 50   # altere para 10 durante os testes
```

## 📤 Exemplo de saída

```
--- Entrevistado 1 de 10 ---
Nome: Ana
Idade: 25
Avalie o atendimento (1-EXCELENTE, 2-BOM, 3-RUIM): 1
Registrado: Ana, 25 anos, avaliou como EXCELENTE.

...

===== RESULTADO DA PESQUISA =====
Total de entrevistados: 10
Quantidade de respostas EXCELENTE: 4
Quantidade de respostas RUIM: 3
Quantidade de respostas BOM: 3
```

## 🗂️ Estrutura do projeto

```
.
├── pesquisa_satisfacao.py   # Programa principal da pesquisa
└── README.md                # Este arquivo
```

## 🛠️ Tecnologias utilizadas

- **Python 3** — estruturas de repetição (`for`), estruturas de decisão (`if/elif/else`) e tratamento de exceções (`try/except`)

## 👤 Autor

Projeto desenvolvido para fins acadêmicos/demonstrativos da empresa fictícia **TudoWeb**.