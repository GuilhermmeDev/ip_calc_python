# 🧮 Calculadora de Sub-rede em Python

Este é um projeto simples em Python que calcula e exibe informações essenciais sobre uma rede IP a partir de um endereço com máscara CIDR. Ele foi criado com o objetivo de facilitar o estudo e a análise de redes de computadores.

## 🚀 Funcionalidades

* Cálculo do endereço da rede
* Exibição da máscara de sub-rede
* Determinação do endereço de broadcast
* Identificação da faixa de endereços IP válidos para hosts
* Cálculo da quantidade de IPs disponíveis na sub-rede

## 🎯 Objetivo

A ferramenta foi desenvolvida para auxiliar estudantes, técnicos e profissionais da área de redes a compreender e analisar sub-redes de forma rápida e prática, sem depender de ferramentas externas.

## 🛠️ Tecnologias Utilizadas

* **Python 3** – Linguagem de programação principal do projeto
* **Biblioteca `ipaddress`** – Nativa do Python, utilizada para manipulação de IPs e sub-redes

## 🧑‍💻 Como usar (modo terminal)

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Execute o script:

   ```bash
   python calculadora_rede.py
   ```

3. Edite o endereço IP no final do arquivo para calcular informações de diferentes redes.

### 📌 Exemplo de entrada no código

```python
calcular_informacoes_rede("192.168.0.0/24")
```

### 🖥️ Saída esperada

```
Endereço da rede: 192.168.0.0
Máscara de rede: 255.255.255.0
Endereço de broadcast: 192.168.0.255
Faixa de endereços válidos: 192.168.0.1 - 192.168.0.254
Total de endereços disponíveis: 254
```

## 🧾 Interface gráfica (branch `GUI`)

O projeto também conta com uma interface gráfica desenvolvida com **Streamlit**, disponível na branch `GUI`.

### Como usar a versão com interface:

1. Troque para a branch:

   ```bash
   git checkout GUI
   ```

2. Instale o Streamlit (caso ainda não tenha):

   ```bash
   pip install streamlit
   ```

3. Execute a aplicação:

   ```bash
   streamlit run app.py
   ```

---
