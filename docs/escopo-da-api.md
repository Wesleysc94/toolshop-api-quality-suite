# Escopo da API

## Visao geral

Esta primeira etapa foi definida para validar os endpoints mais importantes e mais simples de reproduzir em uma rodada inicial de automacao.

## Endpoints em escopo

### Catalogo

- `GET /products`
- `GET /products/{id}`
- `GET /brands`
- `GET /categories/tree`

### Autenticacao

- `POST /users/login`
- `GET /users/me`

### Carrinho

- `POST /carts`
- `GET /carts/{id}`

### Cenarios negativos

- login invalido
- acesso sem autenticacao
- item inexistente
- carrinho inexistente

## Fora de escopo nesta fase

- inclusao de item no carrinho
- fluxos completos de checkout
- validacao detalhada de schema
- cobertura por Postman/Newman
- pipeline de CI

## Resultado esperado

Com esse recorte, a primeira fase entrega uma base automatizada real, facil de entender e pronta para evoluir nas proximas rodadas.
