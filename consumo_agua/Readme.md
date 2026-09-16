# ⚡ Calculadora de Consumo Elétrico

Uma calculadora simples desenvolvida em **Python** para estimar o consumo mensal de energia elétrica de um aparelho.

## 🎯 Objetivo

O projeto tem como objetivo calcular quanto um aparelho pode consumir de energia por mês, utilizando sua potência e o tempo médio de utilização diária.

## 🧮 Como funciona

O programa utiliza a seguinte fórmula:

**Consumo mensal = (Potência × Horas por dia × 30) ÷ 1000**

O resultado é apresentado em **kWh/mês**.

Além disso, o programa calcula uma estimativa do custo mensal utilizando uma tarifa de **R$ 0,75 por kWh**.

## 💻 Tecnologias utilizadas

* 🐍 Python
* 💻 Git
* 🐙 GitHub

## 🚀 Como executar

1. Instale o Python no computador.
2. Clone este repositório.
3. Entre na pasta do projeto.
4. Execute o arquivo `app.py`.

```bash
python app.py
```

## 📌 Exemplo

```text
=== Calculadora de Consumo Elétrico ===

Digite o nome do aparelho: Geladeira
Digite a potência do aparelho em watts (W): 500
Digite o tempo médio de uso diário (em horas): 3

=== Resultado ===
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75/mês
```

## 📚 Aprendizados

Com este projeto, foram praticados conceitos básicos de programação em Python, como:

* Entrada de dados com `input()`
* Conversão de valores com `float()`
* Operações matemáticas
* Variáveis
* Formatação de resultados com `f-string`

## 👨‍💻 Autor

Projeto desenvolvido como atividade de iniciação em tecnologia.
