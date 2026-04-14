# Relatorio de Execucao - Rodada Smoke API 01

## Visao geral

Primeira rodada automatizada executada contra a API real do ecossistema **Practice Software Testing**.

## Data

- `2026-04-14`

## Ambiente

- Base URL: `https://api.practicesoftwaretesting.com`
- Ferramentas: `pytest` + `httpx`
- Linguagem: `Python 3.12.3`

## Suite executada

- `python -m pytest -m smoke`
- `python -m pytest -m negative`

## Resultado

- Smoke: `7` aprovados em `11.47s`
- Negativos: `4` aprovados em `5.25s`
- Total: `11` aprovados

## Cobertura validada nesta rodada

- lista de produtos
- detalhe de produto
- marcas
- arvore de categorias
- login
- usuario autenticado
- criacao de carrinho
- leitura de carrinho
- usuario autenticado sem login
- login com senha invalida
- produto inexistente
- carrinho inexistente

## Evidencias

- `evidence/2026-04-14-rodada-smoke-api/pytest-smoke.txt`
- `evidence/2026-04-14-rodada-smoke-api/pytest-smoke.xml`
- `evidence/2026-04-14-rodada-smoke-api/pytest-negative.txt`
- `evidence/2026-04-14-rodada-smoke-api/pytest-negative.xml`

## Conclusao

A primeira etapa da suite de API foi concluida com sucesso na rodada registrada.

O projeto ficou com uma base automatizada simples, legivel e reproduzivel, pronta para ser expandida nas proximas fases com cenarios mais profundos de carrinho, checkout e integracao em pipeline.
