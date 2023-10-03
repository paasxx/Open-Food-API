# API Open Food Facts com Docker Compose 🔌🍔

"Uma API REST em Python, usando Django Rest Framework e Docker, que fornece informações nutricionais do banco de dados Open Food Facts para a equipe da Fitness Foods LC."

## Como Começar

Siga os passos abaixo para configurar e executar o projeto usando o Docker Compose.

### Pré-requisitos

1. Docker 🐳
2. Docker Compose

### Tecnologias

1. Docker 🐳
2. Docker Compose
3. Pytest (Testes Unitários)
3. PostgreSQL
4. Swagger (Documentação)
5. Postman (Teste externo Endpoints)

### Instalação

1. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/paasxx/Open-Food-API.git
```

2. Navegue até o diretório do projeto:

```bash
cd djangoproject
```

3. Execute o Docker Compose para construir e iniciar o contâiner:

   Docker: version 24.0.5

```bash
docker-compose up --build
```

A API estará acessível em `http://localhost:8000/api`.

### Endpoints da API

| Método   | Endpoint                    | Descrição                                      |
|----------|-----------------------------|------------------------------------------------|
| GET      | /                           | Detalhes da API                                |
| PUT      | /products/:code             | Atualiza informações do projeto Web            |
| DELETE   | /products/:code             | Altera o status do produto para "excluído"     |
| GET      | /products/:code             | Recupera informações detalhadas de um produto  |
| GET      | /products                   | Lista todos os produtos                        |
| POST     | /products/create            | Adiciona um novo produto ao banco de dados     |


### Parâmetros de entrada para Endpoints da API

Exemplo de parâmetro de entrada para os métodos PUT e POST no formato .json

```json
{
  "code": 20221126,
  "status": "published",
  "imported_t": "2020-02-07T16:00:00Z",
  "url": "https://world.openfoodfacts.org/product/20221126",
  "creator": "securita",
  "created_t": 1415302075,
  "last_modified_t": 1572265837,
  "product_name": "Madalenas quadradas",
  "quantity": "380 g (6 x 2 u.)",
  "brands": "La Cestera",
  "categories": "Lanches comida, Lanches doces, Biscoitos e Bolos, Bolos, Madalenas",
  "labels": "Contem gluten, Contém derivados de ovos, Contém ovos",
  "cities": "",
  "purchase_places": "Braga,Portugal",
  "stores": "Lidl",
  "ingredients_text": "farinha de trigo, açúcar, óleo vegetal de girassol, clara de ovo, ovo, humidificante (sorbitol), levedantes químicos (difosfato dissódico, hidrogenocarbonato de sódio), xarope de glucose-frutose, sal, aroma",
  "traces": "Frutos de casca rija,Leite,Soja,Sementes de sésamo,Produtos à base de sementes de sésamo",
  "serving_size": "madalena 31.7 g",
  "serving_quantity": 31.7,
  "nutriscore_score": 17,
  "nutriscore_grade": "d",
  "main_category": "en:madeleines",
  "image_url": "https://static.openfoodfacts.org/images/products/20221126/front_pt.5.400.jpg"
}
```

### Testes

Para executar testes unitários para a API dentro do contêiner, use o seguinte comando:

Obter o id do container Docker:

```bash
docker ps
```
Rodar o teste:

```bash
docker exec -it container_id python manage.py test
```

### Segurança 

Foi implementada com auxílio do Django Rest Framework a autenticação via token com API Key, que deve ser incorporada no cabeçalho de autorização se estiver testando por exemplo com o Postman.

### Documentação 📚🚀

Documentação completa da API usando o padrão OpenAPI 3.0 acesse:

`http://localhost:8000/api/schema/docs/`
