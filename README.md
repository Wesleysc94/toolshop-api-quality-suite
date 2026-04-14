# toolshop-api-quality-suite

Projeto de automacao de API construido sobre a API publica usada pelo ecossistema **Practice Software Testing**.

Este repositorio apresenta a primeira suite automatizada de API do portfolio, com foco em catalogo, autenticacao, usuario autenticado, carrinho e cenarios negativos basicos.

## Visao Geral

A proposta desta etapa foi mostrar:

- quais endpoints entraram na primeira fase
- como a suite foi organizada
- o que foi validado na rodada inicial
- como a execucao pode ser reproduzida

## API Sob Teste

- Base URL: https://api.practicesoftwaretesting.com
- Frontend relacionado: https://practicesoftwaretesting.com/
- Referencia complementar: https://practiceautomatedtesting.com/api

## Escopo Da Etapa

A cobertura inicial desta suite inclui:

- lista de produtos
- detalhe de produto
- marcas
- arvore de categorias
- login
- consulta de usuario autenticado
- criacao de carrinho
- leitura de carrinho
- cenarios negativos basicos

Ficaram fora desta fase:

- checkout mais profundo
- schema fuzzing
- Postman ou Newman
- CI
- relatorios Allure

## Stack Utilizada

- `Python`
- `pytest`
- `httpx`

## Resultado Da Rodada

Na execucao registrada em `2026-04-14`:

- `7` testes smoke foram aprovados
- `4` testes negativos foram aprovados
- `11` testes foram aprovados no total
- a autenticacao foi validada com a conta demo oficial
- o carrinho foi validado em criacao e leitura

## Estrutura Do Repositorio

- [RESUMO-DO-PROJETO.txt](./RESUMO-DO-PROJETO.txt): leitura curta da etapa
- [docs/](./docs/): escopo, estrategia e guia de revisao
- [tests/](./tests/): suite automatizada em `pytest + httpx`
- [execution-reports/](./execution-reports/): relatorio da rodada executada
- [evidence/](./evidence/): saidas e artefatos da execucao

## Como Executar

1. Crie um ambiente virtual Python.
2. Instale as dependencias com `python -m pip install -e .`.
3. Rode `python -m pytest -m smoke`.
4. Rode `python -m pytest -m negative`.

As credenciais demo podem ser sobrescritas por variaveis de ambiente:

- `PST_API_BASE_URL`
- `PST_API_EMAIL`
- `PST_API_PASSWORD`

## Como Revisar

1. Comece por [RESUMO-DO-PROJETO.txt](./RESUMO-DO-PROJETO.txt).
2. Leia [docs/guia-de-revisao.md](./docs/guia-de-revisao.md).
3. Veja a suite em [tests/](./tests/).
4. Consulte o relatorio em [execution-reports/2026-04-14-rodada-smoke-api-01.md](./execution-reports/2026-04-14-rodada-smoke-api-01.md).
5. Confira as evidencias em [evidence/](./evidence/).
