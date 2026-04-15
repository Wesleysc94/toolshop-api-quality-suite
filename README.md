# 🔌 toolshop-api-quality-suite

> Suite de automação de API com Python, pytest e httpx aplicada ao ecossistema Practice Software Testing.

[![Python](https://img.shields.io/badge/Python-pytest-3776AB?logo=python&logoColor=white)]()
[![Testes](https://img.shields.io/badge/Testes-11%20aprovados-brightgreen)]()
[![Produto](https://img.shields.io/badge/Produto-Practice%20Software%20Testing-blue)](https://practicesoftwaretesting.com/)

📦 **Parte do portfolio:** [toolshop-quality-portfolio](https://github.com/Wesleysc94/toolshop-quality-portfolio)

---

## Objetivo

Validar a camada de serviço da aplicação Practice Software Testing através de testes automatizados de API. Enquanto a suite E2E verifica o comportamento do usuário no navegador, esta suite verifica se os dados e regras de negócio estão corretos na API que alimenta a aplicação.

---

## API sob teste

| Recurso | URL |
|---|---|
| API principal | https://api.practicesoftwaretesting.com |
| Referência complementar | https://practiceautomatedtesting.com/api |

---

## Cobertura de testes

| Área | Cenários | Status |
|---|---|---|
| **Catálogo** | Listagem de produtos, detalhes de produto | ✅ |
| **Autenticação** | Login com credenciais válidas, token de acesso | ✅ |
| **Usuário autenticado** | Acesso a dados do usuário logado | ✅ |
| **Carrinho** | Criação, adição de itens, consulta | ✅ |
| **Cenários negativos** | Respostas de erro esperadas (401, 404, 422) | ✅ |

### Resultado da rodada

```
  11 testes executados
  11 aprovados
   0 falhas
  ────────────────
  Taxa de aprovação: 100%
```

---

## Stack utilizada

| Ferramenta | Uso |
|---|---|
| **Python** | Linguagem dos testes |
| **pytest** | Framework de teste (fixtures, markers, assertions) |
| **httpx** | Cliente HTTP moderno (async-ready, tipado) |

**Por que httpx em vez de requests?** httpx é mais moderno, suporta async nativamente e tem API compatível com requests. Mostra familiaridade com ferramentas atuais do ecossistema Python.

---

## Como executar

**Pré-requisitos:** Python 3.10+ instalado.

```bash
# 1. Clone o repositório
git clone https://github.com/Wesleysc94/toolshop-api-quality-suite.git
cd toolshop-api-quality-suite

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute os testes
pytest                          # Roda tudo
pytest -v                       # Modo detalhado
pytest --tb=short               # Traceback resumido em caso de falha
```

---

## Estrutura do repositório

```
toolshop-api-quality-suite/
├── README.md                    ← Você está aqui
├── RESUMO-DO-PROJETO.txt        ← Leitura rápida
├── 00-LEIA-PRIMEIRO.txt         ← Orientação inicial
├── requirements.txt             ← Dependências Python
├── tests/                       ← Suite de testes de API
├── docs/
│   ├── escopo.md                ← Endpoints cobertos e decisões
│   ├── estrategia.md            ← Abordagem de automação
│   └── guia-de-revisao.md       ← Trilha pra avaliadores
├── execution-reports/           ← Relatório da rodada executada
└── evidence/                    ← Saídas e logs da execução
```

---

## Escopo atual vs. próximas fases

| Coberto agora | Planejado para próximas fases |
|---|---|
| ✅ Catálogo (listagem e detalhe) | ⏳ Paginação e filtros avançados |
| ✅ Autenticação (login e token) | ⏳ Refresh token e expiração |
| ✅ Usuário autenticado | ⏳ Atualização de perfil |
| ✅ Carrinho (CRUD básico) | ⏳ Cupons e descontos |
| ✅ Cenários negativos básicos | ⏳ Rate limiting e validação de schema |
| | ⏳ CI/CD com GitHub Actions |

---

## Como revisar

1. **[RESUMO-DO-PROJETO.txt](RESUMO-DO-PROJETO.txt)** — Visão geral rápida
2. **[docs/guia-de-revisao.md](docs/guia-de-revisao.md)** — Trilha de leitura
3. **[tests/](tests/)** — Código dos testes
4. **[execution-reports/](execution-reports/)** — Relatório da rodada
5. **[evidence/](evidence/)** — Logs e saídas

---

## O que este projeto demonstra

- **Testes na camada de serviço** — validação direta da API, independente da interface
- **Python + pytest** — stack padrão do mercado para automação de API
- **httpx** — cliente HTTP moderno, mostrando conhecimento de ferramentas atuais
- **Cenários negativos** — validação de que a API responde corretamente a entradas inválidas
- **Execução reproduzível** — qualquer pessoa pode clonar, instalar e rodar
