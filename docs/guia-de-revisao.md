# Guia de Revisao

## Objetivo

Este repositorio apresenta a primeira etapa de automacao de API do ecossistema **Practice Software Testing**.

O foco aqui e mostrar, de forma clara:

- quais endpoints entraram na primeira fase
- como a suite foi organizada
- quais validacoes foram executadas
- qual foi o resultado da primeira rodada

## Ordem de leitura recomendada

1. Ler `RESUMO-DO-PROJETO.txt`.
2. Ler o `README.md`.
3. Ler `docs/escopo-da-api.md`.
4. Ler `execution-reports/2026-04-14-rodada-smoke-api-01.md`.
5. Ler `tests/test_api_smoke.py`.
6. Ler `tests/test_api_negative.py`.
7. Conferir as evidencias em `evidence/`.

## API sob teste

- base URL: https://api.practicesoftwaretesting.com
- frontend relacionado: https://practicesoftwaretesting.com/
- referencia complementar: https://practiceautomatedtesting.com/api

## Como validar os resultados

1. Criar um ambiente virtual Python.
2. Instalar dependencias com `python -m pip install -e .`.
3. Rodar `python -m pytest -m smoke`.
4. Rodar `python -m pytest -m negative`.

## Resultado atual

Na rodada registrada em `2026-04-14`, o projeto terminou com:

- `7` testes smoke aprovados
- `4` testes negativos aprovados
- `11` testes aprovados no total

## Credenciais demo usadas

As validacoes de autenticacao usam, por padrao, a conta demo oficial:

- email: `customer@practicesoftwaretesting.com`
- senha: `welcome01`

As credenciais podem ser substituidas por variaveis de ambiente.
