# 🔌 toolshop-api-quality-suite

> Suite de automação de API com Python, pytest e httpx aplicada ao ecossistema Practice Software Testing.

[![Python](https://img.shields.io/badge/Python-pytest-3776AB?logo=python&logoColor=white)]()
[![Testes](https://img.shields.io/badge/Testes-11%20aprovados-brightgreen)]()
[![Produto](https://img.shields.io/badge/Produto-Practice%20Software%20Testing-blue)](https://practicesoftwaretesting.com/)

🔎 **Portfolio principal:** [Wesleysc94](https://github.com/Wesleysc94/Wesleysc94)
📦 **Case Study 1:** [toolshop-quality-portfolio](https://github.com/Wesleysc94/toolshop-quality-portfolio)

---

## Objetivo

Validar a camada de serviço da aplicação Practice Software Testing por meio de testes automatizados de API.

Enquanto a automação web verifica o fluxo do usuário no navegador, esta suíte valida se os endpoints respondem corretamente, se as regras básicas de negócio estão coerentes e se os principais erros retornam os status esperados.

---

## API sob teste

| Recurso | URL |
|---|---|
| API principal | https://api.practicesoftwaretesting.com |
| Frontend relacionado | https://practicesoftwaretesting.com/ |
| Referência complementar | https://practiceautomatedtesting.com/api |

---

## Escopo

| Área | O que foi validado |
|---|---|
| **Catálogo** | listagem de produtos e detalhe de produto |
| **Autenticação** | login com credenciais válidas e token de acesso |
| **Usuário autenticado** | consulta de dados do usuário logado |
| **Carrinho** | criação, adição de itens e leitura |
| **Cenários negativos** | respostas esperadas para 401, 404 e 422 |

---

## Resultado da rodada

```
  11 testes executados
  11 aprovados
  0 falhas
  ----------------
  Taxa de aprovação: 100%
```

Rodada registrada em 2026-04-14.

---

## Stack utilizada

| Ferramenta | Uso |
|---|---|
| **Python** | linguagem dos testes |
| **pytest** | execução, fixtures, markers e assertions |
| **httpx** | cliente HTTP usado para chamadas à API |

---

## Como executar

**Pré-requisitos:** Python 3.10+ instalado.

```bash
git clone https://github.com/Wesleysc94/toolshop-api-quality-suite.git
cd toolshop-api-quality-suite

python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

pip install -r requirements.txt

pytest
pytest -v
pytest --tb=short
```

---

## Como revisar

1. Leia o [RESUMO-DO-PROJETO.txt](RESUMO-DO-PROJETO.txt)
2. Consulte o [docs/guia-de-revisao.md](docs/guia-de-revisao.md)
3. Abra o escopo em [docs/escopo-da-api.md](docs/escopo-da-api.md)
4. Revise os testes em [tests/](tests/)
5. Confira o relatório da rodada em [execution-reports/](execution-reports/)

---

## O que este projeto entrega

- **Validação na camada de serviço** — sem depender da interface web
- **Automação em Python com pytest** — stack comum no mercado para API
- **Cenários positivos e negativos** — não apenas fluxo feliz
- **Instalação e execução simples** — clone, instale e rode em poucos passos
