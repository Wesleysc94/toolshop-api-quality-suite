# Estrategia de Testes

## Objetivo

Organizar uma primeira rodada automatizada de API com foco em endpoints reais e respostas verificaveis.

## Tipos de teste desta fase

- smoke
- negativo
- autenticacao
- leitura de dados

## Abordagem

### Smoke

Usado para validar rapidamente se a API principal responde bem nos fluxos mais importantes da rodada.

### Negativo

Usado para confirmar se a API responde com status e mensagens coerentes quando recebe credenciais ou identificadores invalidos.

## Criterios da primeira rodada

- validar status code
- validar campos principais da resposta
- validar autenticacao com conta demo oficial
- validar comportamento basico do carrinho

## Evolucao prevista

As proximas rodadas podem ampliar a cobertura para:

- mutacoes adicionais de carrinho
- checkout
- validacao de schema
- execucao em CI
- relatorios mais completos
