# 🛒 Sistema de Desconto Progressivo

Este projeto foi desenvolvido em **Python** com o objetivo de criar um sistema simples de **desconto progressivo** para uma loja online.

O programa solicita o valor total da compra e calcula automaticamente o desconto correspondente, mostrando também o valor final que o cliente deverá pagar.

## 📌 Regras de desconto

| Valor da compra            | Desconto |
| -------------------------- | -------: |
| Menor que R$ 200,00        |       5% |
| De R$ 200,00 até R$ 299,99 |      10% |
| R$ 300,00 ou mais          |      15% |

## 💻 Tecnologias utilizadas

* 🐍 Python
* `if`, `elif` e `else`
* Entrada de dados com `input()`
* Conversão de valores com `float()`
* Exibição de resultados com `print()`
* Formatação de valores com `f-string`

## ⚙️ Como funciona

O usuário informa o valor total da compra. O programa verifica em qual faixa de preço o valor está e define a porcentagem de desconto.

Depois, são calculados:

1. O valor do desconto;
2. O valor final da compra após o desconto.

### Exemplo

Se o usuário informar:

```text
Digite o valor total da compra: R$ 250
```

O programa identificará que a compra está na faixa de **10% de desconto** e exibirá:

```text
Valor da compra: R$ 250.00
Desconto aplicado: R$ 25.00
Valor a pagar: R$ 225.00
```

## ▶️ Como executar

1. Tenha o **Python** instalado no computador.
2. Baixe ou clone este repositório.
3. Abra o arquivo `.py` em um editor de código.
4. Execute o programa.
5. Digite o valor da compra quando solicitado.

## 🎯 Objetivo do projeto

Este projeto foi criado para praticar conceitos básicos de programação em Python, principalmente **estruturas condicionais, entrada de dados e operações matemáticas**.

---

📚 **Projeto desenvolvido para fins de estudo.**
