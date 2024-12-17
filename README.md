# ambrosia-serve

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FPostechSOAT2024Grupo40%2Fambrosia-serve%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/PostechSOAT2024Grupo40/ambrosia-serve)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr/PostechSOAT2024Grupo40/ambrosia-serve)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=PostechSOAT2024Grupo40_ambrosia-serve&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=PostechSOAT2024Grupo40_ambrosia-serve)

# Ambrosia Serve by **_Grupo 40_**

Ambrosia Serve é uma solução desenvolvida como parte do tech challenge do curso de Software
Architecture da Fiap. O
projeto coloca em prática os conhecimentos adquiridos ao longo do curso.

O objetivo do desenvolvimento é apoiar lanchonetes em rápida expansão, oferecendo uma solução para
gerir pedidos e
aumentar a satisfação dos clientes.

**Índice**

- [Propósito](#proposito)
- [Princípios](#principios)
- [Documentações](#documentacoes)
- [Linguagem Ubíqua](#Linguagem_Ubiqua)
- [Requisitos](#requisitos)
- [Estrutura](#estrutura)
- [Executando](#executando)
- [Campos Enums](#campos-enums)

## Propósito

Para garantir a satisfação dos clientes num negócio em constante crescimento, foi modelada uma
solução que auxilia na
gestão de pedidos. A arquitetura foi projetada para que as regras de negócio sejam independentes de
recursos
externos, como banco de dados, interface do usuário (website, mobile, etc.) e meios de autenticação.
Assim, é possível
garantir que o que é importante não dependa de recursos ou ferramentas que não estão sob o nosso
controle.

Dessa forma, podemos garantir que cada parte das regras de negócio possa ser testada de maneira
isolada.

## Principios

Os principais princípios seguidos no desenvolvimento desta aplicação incluem:

- **Independência**: As regras de negócio são independentes de infraestrutura externa, o que garante
  maior flexibilidade
  e testabilidade.
- **Modularidade**: A aplicação é dividida em módulos, facilitando a manutenção e evolução do
  sistema.
- **Escalabilidade**: A arquitetura foi desenhada para suportar o crescimento rápido do negócio.
- **Segurança**: Implementação de práticas de segurança em todas as camadas da aplicação.

## Documentações

https://miro.com/app/board/uXjVKzFU2VA=/

1. **Sessão de Brainstorming**

![Brainstorming](docs/Brainstorming.jpg)
Nesta sessão, foram discutidos todos os eventos que ocorrem no negócio.

2. **Ajuste dos Eventos em Ordem Cronológica**
   ![Fluxo Temporal](docs/Fluxo_temporal.jpg)
   Nesta etapa, os eventos mapeados no _brainstorming_ foram refinados e ajustados em ordem
   cronológica, exibindo todos
   os eventos do começo ao fim.

3. **Agrupamento dos Eventos, Políticas, Comandos, Usuários e Sistemas Externos**
   ![Relacionamentos](docs/Relacionamentos.jpg)
   Nesta etapa, foram inseridos outros recursos do DDD, como mapeamento de atores, sistemas externos
   e comandos. Também
   foram agrupados os serviços relacionados.

4. **Contextos Delimitados**
   ![Contextos Delimitados](docs/Contextos_Delimitados.jpg)
   Nesta etapa, foram identificados os contextos delimitados e as suas fronteiras, além de mapear
   onde um contexto se
   comunica com outro.

## Linguagem Ubíqua

### AG Cliente

#### Eventos de Negócio

- **Cliente acessou com usuário cadastrado**: Evento que ocorre quando o usuário inicia um pedido
  logado.
- **Cliente Acessou o Sistema**: Evento que ocorre quando um cliente, seja cadastrado ou anônimo,
  acessa a tela inicial
  do sistema.
- **Cliente Anônimo**: Evento que ocorre quando um usuário não identificado inicia um pedido.

#### Comandos

- **Buscar Ofertas**: Ação realizada pelo cliente para visualizar as ofertas disponíveis.
- **Acessar com Usuário Cadastrado**: Ação de acessar o sistema utilizando as credenciais de um
  usuário previamente
  registrado.
- **Acessar o Sistema**: Ação geral de acessar a tela inicial do sistema.
- **Acessar com Usuário Anônimo**: Ação de um pedido sem fornecer credenciais de usuário registrado.

#### Agregados e Entidades

- **Cliente**: Agregado que representa o login no sistema, que pode ser de usuário cadastrado ou
  anônimo.
  - **Usuário**: Entidade que representa um cliente cadastrado no sistema.

#### Sistemas Externos

- **Ofertas e Promoções**: Sistema externo que fornece informações sobre ofertas e promoções
  disponíveis para os
  clientes.

#### Políticas

- **Cliente Acessou com Usuário Cadastrado**: Política que define que, quando um cliente acessa o
  sistema com usuário
  cadastrado, ele pode participar de campanhas promocionais.

#### Atores

- **Usuário**: Ator que interage com o sistema, podendo ser um usuário cadastrado ou anônimo.

#### Modelos de Leitura

- **Tela inicial**: Home page do sistema.

### AG Produtos

#### Eventos de Negócio

- **Cliente iniciou o pedido**: Evento que ocorre quando o usuário inicia um pedido, criando um
  carrinho.
- **Cliente adicionou itens no pedido**: Evento que ocorre quando um cliente seleciona um item e
  monta o combo.
- **Aplicou desconto ao pedido**: Evento que ocorre quando um usuário autenticado recebe descontos
  no pedido.

#### Comandos

- **Iniciar pedido**: Ação de iniciar um novo pedido.
- **Adicionar item**: Ação de adicionar itens no combo.
- **Aplicar desconto**: Ação de selecionar um desconto ou itens promocionais disponíveis para
  usuário autenticado.

#### Agregados e Entidades

- **Produtos**: Agregado que representa a montagem do combo.
- **Produtos**: Entidade que representa os itens disponíveis para compor o combo.

#### Políticas

- **Os itens podem ser adicionados na ordem: Lanche, Acompanhamento, Bebida e sobremesa**: Política
  que define que os
  itens do pedido podem ser inseridos na sequência: Lanche, Acompanhamento, Bebida e sobremesa,
  sendo que todos são
  opcionais. Em cada sequência, são exibidos o nome, descrição e o preço.

#### Atores

- **Usuário**: Ator que seleciona os itens do pedido, montando o combo.

#### Modelos de Leitura

- **Lista de ofertas e promoções**: Lista de ofertas, promoções e campanhas promocionais disponíveis
  para usuários
  autenticados selecionarem.
- **Lista de produtos**: Lista de itens disponíveis exibidos sequencialmente na ordem: Lanche,
  Acompanhamento, Bebida e
  sobremesa.

### AG Carrinho

#### Eventos de Negócio

- **Cliente Abriu o carrinho**: Evento que ocorre quando o cliente, após adicionar os produtos no
  combo, abre o carrinho
  para verificar todas as informações dos itens e o valor total.
- **Cliente desejou adicionar mais itens no pedido**: Evento que ocorre quando o cliente, dentro da
  tela de carrinho,
  deseja adicionar mais algum item.
- **Cliente confirmou o pedido**: Evento que ocorre quando o cliente confirma os itens do pedido e
  deseja realizar o
  pagamento.
- **Cliente realizou o pagamento**: Evento que ocorre quando o cliente realiza o pagamento do
  pedido.
- **Pedido cancelado**: Evento que ocorre quando o cliente cancela o pedido, quando o pedido atinge
  o tempo máximo em
  status aberto e não pago, ou quando o cliente desiste e deseja cancelar.

#### Comandos

- **Abrir carrinho**: Ação de abrir o carrinho e visualizar os itens que compõem o pedido.
- **Adicionar mais itens**: Ação de adicionar mais itens no pedido.
- **Confirmar pedido**: Ação de confirmação do pedido e avançar para o pagamento.
- **Realizar pagamento**: Ação de realizar o pagamento do pedido.
- **Cancelar pedido**: Ação de cancelar o pedido aberto, por ação automatizada ou por usuário.
- **Enviar pedido**: Ação de enviar o pedido para a cozinha para ser preparado.

#### Agregados e Entidades

- **Carrinho**: Agregado que representa o carrinho do pedido.
- **Produto**: Entidade que representa os itens do combo escolhidos pelo usuário.

#### Sistemas Externos

- **Mercado Pago**: API de pagamento do Mercado Pago.
- **Fila de processamento de pedidos**: Sistema de mensageria que armazena os pedidos na fila FIFO.

#### Políticas

- **Pedido aberto e status não atualizado após 30 minutos é cancelado por meio de um job**: Política
  que define que um
  pedido é cancelado automaticamente quando o seu status não é atualizado de aberto para pago em 30
  minutos.
- **Pedido que não possuir itens não pode ser confirmado**: Política que define que um pedido não
  pode ser avançado sem
  conter produtos inseridos.
- **Pagamento recusado**: Política que define que pagamentos recusados pela API do Mercado Pago não
  podem ser avançados,
  retornando ao cliente para alterar os dados de pagamento.
- **Cliente é notificado sobre o status de pagamento**: Política que define que o cliente recebe uma
  notificação com o
  status do processo de pagamento.

#### Atores

- **Usuário**: Ator que confirma os itens do pedido e realiza o pagamento.

### AG Preparo

#### Eventos de Negócio

- **Pedido foi enviado para a cozinha**: Evento que ocorre quando um pedido válido/pago é enviado
  para preparo.
- **Foi iniciado o preparo do pedido**: Evento que ocorre quando é iniciado o preparo dos produtos.
- **Pedido foi preparado**: Evento que ocorre quando todos os itens de um pedido foram preparados e
  estão disponíveis
  para retirada.

#### Comandos

- **Pegar pedido**: Ação de pegar um pedido da fila de pedidos para ser preparado.
- **Iniciar preparo**: Ação de iniciar o preparo dos itens de um pedido.
- **Finalizar preparo**: Ação de concluir todos os itens de um pedido.

#### Agregados e Entidades

- **Preparo**: Agregado que representa a cozinha onde os pedidos são preparados.
- **Pedido**: Entidade que representa os combos de produtos que precisam ser preparados.

#### Políticas

- **Cliente é notificado sobre o preparo**: Política que define que o cliente será notificado quando
  o preparo do pedido
  é iniciado.
- **Cliente é notificado sobre o fim do preparo**: Política que define que o cliente será notificado
  quando o pedido foi
  finalizado e está disponível para retirada.

#### Atores

- **Cozinha**: Ator que prepara os pedidos.

#### Modelos de Leitura

- **Tela de pedidos**: Lista de pedidos que precisam ser preparados, ordenada pela ordem de
  inserção.

## Requisitos

Para rodar este projeto localmente, você precisará ter as seguintes ferramentas instaladas:

- **[Python3](https://www.python.org/downloads/)**
- **[pip3](https://pip.pypa.io/en/stable/installation/)**
- **[uv documentation](https://docs.astral.sh/uv/)**
- **[docker](https://docs.docker.com/engine/install/)**

Esse projeto utiliza a biblioteca `uv` para gerir as dependências do projeto, os seguintes comandos
são mais utilizados:

1. Instalar o Python versão 3.11, caso seja necessário

```shell
uv python install 3.11
```

2. Criar um ambiente virtual

```shell
uv venv
```

3. Para travar as dependências declaradas no pyproject.toml:

```shell
uv pip compile pyproject.toml -o requirements.txt
```

4. Para sincronizar o ambiente com o arquivo requirements.txt

```shell
uv pip sync requirements.txt
```

## Estrutura

**Diagrama da implementação do servidor**

<p align="center">
  <img src="docs/architecture-diagram.png" />
</p>

**Diagrama da infra**
<p align="center">
  <img src="docs/k8s.png" />
</p>

## Executando

Para executar a API localmente, siga as seguintes etapas:

1. Clone o repositório:

```shell
git clone git@github.com:PostechSOAT2024Grupo40/ambrosia-serve.git && cd ambrosia-serve
```

2. Crie um arquivo .env com os valores:

```
POSTGRES_DB=<Nome do banco de dados>
POSTGRES_USER=<Nome de usuário>
POSTGRES_HOST=<URL de acesso>
POSTGRES_PORT=<Porta do banco de dados>
POSTGRES_PASSWORD=<Senha de usuário>
```

3. Siga as etapas de [Requisitos](#requisitos)

4. Inicie a aplicação:

```shell
fastapi run --workers 4 src/api/presentation/http/http.py
```

5. Acesse o endpoint de documentação `swagger` no navegador `http://<HOST>:8000/docs`

Os seguintes Status de Pedidos estão disponíveis:

| Status        | Descricão                                        |
|---------------|--------------------------------------------------|
| `RECEBIDO`    | O Pedido foi recebido                            |
| `PENDENTE`    | O Pedido esta aguardando pagamento               |
| `PROCESSANDO` | O Pedido foi pago e foi encaminhado para cozinha |
| `CONCLUIDO`   | O Pedido foi concluído                           |
| `CANCELADO`   | O Pedido foi cancelado                           |


Para executar o projeto localmente utilizando Docker, siga as seguintes etapas:

1. Crie a infraestrutura kubernetes utilizando
   o [minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download),
   instale
   caso necessario:

```shell
minikube start
```

```shell
kubectl apply -f infra/namespace.yml && kubectl apply -f infra/
```

2. Conecte-se ao serviço `ambrosia-server`:

```shell
minikube service ambrosia-server
```


## Para executar no EKS

```shell
aws eks update-kubeconfig --region us-east-1 --name ambrosia-serve-cluster
```

```shell
kubectl get svc
```

