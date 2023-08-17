# Documentação da Aplicação

A documentação a seguir descreve as funcionalidades dos endpoints da aplicação, divididos nos aplicativos 'vibra' e 'minalba'.

## Aplicativo Vibra

### URL Endpoints

#### 1. GET /clientes/

Recupera uma lista de todos os clientes, permitindo a filtragem por nome e operação inbound/outbound.

**Resposta**
- Código de Status: 200 (OK)

#### 2. GET /clientes/<codigo>

Permite a edição de um cliente específico, baseado no seu código.

**Resposta**
- Código de Status: 200 (OK)

#### 3. GET /produtos/

Recupera uma lista de produtos, permitindo a filtragem por nome.

**Resposta**
- Código de Status: 200 (OK)

#### 4. GET /produtos/<codigo>

Permite a edição de um produto específico, baseado no seu código.

**Resposta**
- Código de Status: 200 (OK)

#### 5. GET /transportadoras/

Recupera uma lista de transportadoras, permitindo a filtragem por código, grupo e nome.

**Resposta**
- Código de Status: 200 (OK)

#### 6. GET /transportadoras/<codigo>

Permite a edição de uma transportadora específica, baseada no seu código.

**Resposta**
- Código de Status: 200 (OK)

## Aplicativo Minalba

### URL Endpoints

#### 1. GET /placas/

Recupera uma lista de placas, permitindo a filtragem por placa.

**Resposta**
- Código de Status: 200 (OK)

#### 2. GET /placas/<id>

Permite a edição de uma placa específica, baseada no seu ID.

**Resposta**
- Código de Status: 200 (OK)

## Aplicativo API

### URL Endpoints

#### 1. GET /transportadora_cnpj/

É necessário o envio de 2 parâmetros no header: AuthenticationKey e cnpj. A API fará uma busca da transportadora pelo cnpj enviado.

**Respota**
- Código de Status: 200 (OK)

## Tecnologias utilizadas
- Django
- Outras bibliotecas e módulos conforme necessário

## Notas
- Certifique-se de enviar as informações corretas nos parâmetros GET e POST conforme a necessidade de cada endpoint.

## Autor
Gustavo Henrique Faneco

`https://github.com/fanecovsf`
