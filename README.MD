# 🌡️ Automação de Pesquisa de Temperatura com Selenium

**Autora:** Beatriz

Projeto em Python que utiliza **Selenium** para abrir o navegador, acessar o Google e pesquisar automaticamente a temperatura do dia.

Os testes são escritos utilizando **BDD** com o framework **Behave**.

---

# 🐍 Versão do Python

Python **3.13.7**

---

# ⚙️ Instalação e Execução do Ambiente Virtual

Crie o ambiente virtual:

```bash
py -m venv .env
```

Ative o ambiente virtual (Windows):

```bash
.env\Scripts\activate
```

---

# 📦 Instalando as dependências

```bash
pip install -r requirements/requirements.txt
```

---

# ▶️ Executando os testes

Para rodar os testes automatizados utilize o comando:

```bash
behave
```

Esse comando irá executar todos os **cenários BDD** definidos na pasta `features`.

---

# 📂 Estrutura do projeto

```
📁 projeto
 ├── features
 │   ├── steps
 │   └── temperatura.feature
 ├── requirements
 │   └── requirements.txt
 └── README.md
```

---

# 🎯 Objetivo do projeto

Este projeto foi criado para praticar:

* Automação web com Selenium
* Testes automatizados com BDD
* Uso do framework Behave em Python
