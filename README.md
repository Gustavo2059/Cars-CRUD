# Cars

Sistema web desenvolvido com **Django** para cadastro, gerenciamento e consulta de veículos. O projeto permite registrar carros com marca, modelo, ano, placa, valor, foto e descrição, além de contar com autenticação de usuários e uma funcionalidade opcional de geração automática de biografia do veículo com IA.

## Sobre o projeto

O **Cars** é uma aplicação simples de gerenciamento de veículos, criada com foco em aprendizado e prática de desenvolvimento web com Django. A aplicação possui páginas para listagem, busca, cadastro, edição, visualização detalhada e exclusão de carros.

O sistema também possui controle de acesso: usuários não autenticados conseguem visualizar os carros cadastrados, enquanto ações como cadastrar, editar e excluir exigem login.

## Funcionalidades

- Listagem de carros cadastrados.
- Busca de veículos pelo modelo.
- Visualização detalhada de cada carro.
- Cadastro de novos veículos.
- Edição de veículos existentes.
- Exclusão de veículos.
- Upload de fotos dos carros.
- Cadastro e gerenciamento de marcas pelo painel administrativo.
- Registro e login de usuários.
- Controle de acesso para ações administrativas.
- Validação de campos no formulário de veículos.
- Histórico automático de inventário com quantidade de carros e valor total cadastrado.
- Configuração opcional para gerar uma biografia automática do carro usando IA.

## Tecnologias utilizadas

- Python
- Django 6.0.1
- SQLite
- HTML
- CSS
- Pillow
- OpenAI API

## Estrutura principal do projeto

```text
Cars/
├── accounts/              # Aplicação responsável por registro, login e logout
├── app/                   # Configurações principais do projeto Django
├── cars/                  # Aplicação principal de gerenciamento de carros
│   ├── models.py          # Modelos: Brand, Car, CarInventory e CarConfiguration
│   ├── forms.py           # Formulário de cadastro e edição de carros
│   ├── views.py           # Views baseadas em classes para CRUD de carros
│   ├── signals.py         # Atualização automática do inventário e bio por IA
│   └── templates/         # Templates HTML da aplicação
├── media/                 # Arquivos de mídia enviados pelos usuários
├── openai_api/            # Integração com a API da OpenAI
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## Modelos do sistema

### Brand

Representa a marca do veículo.

Principais campos:

- `brand_name`: nome da marca.

### Car

Representa um carro cadastrado no sistema.

Principais campos:

- `model`: modelo do carro.
- `brand`: marca relacionada ao veículo.
- `factory_year`: ano de fabricação.
- `model_year`: ano do modelo.
- `plate`: placa do veículo.
- `value`: valor do veículo.
- `photo`: imagem do carro.
- `bio`: descrição curta do veículo.

### CarInventory

Armazena registros automáticos do inventário de carros.

Principais campos:

- `cars_count`: quantidade total de carros cadastrados.
- `cars_value`: soma do valor dos carros cadastrados.
- `created_at`: data e hora do registro.

### CarConfiguration

Armazena configurações do sistema, como a opção de habilitar ou desabilitar a geração automática de biografias por IA.

## Requisitos

Antes de iniciar, é necessário ter instalado:

- Python 3.12 ou superior
- pip
- Git

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual

No Linux ou macOS:

```bash
python -m venv venv
source venv/bin/activate
```

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Observação: o projeto importa `dotenv` no arquivo `openai_api/client.py`. Caso ocorra erro relacionado a esse pacote, instale também:

```bash
pip install python-dotenv
```

Também é recomendado adicionar essa dependência ao `requirements.txt`:

```text
python-dotenv
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, caso deseje utilizar a integração com IA:

```env
API_KEY=sua_chave_da_api_aqui
```

A chave da API não deve ser enviada para o GitHub. Mantenha o arquivo `.env` no `.gitignore`.

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Depois, acesse no navegador:

```text
http://127.0.0.1:8000/cars/
```

## Rotas principais

| Rota | Descrição |
|---|---|
| `/cars/` | Lista os carros cadastrados |
| `/car/<id>/` | Exibe os detalhes de um carro |
| `/new_car/` | Cadastra um novo carro |
| `/car/<id>/update/` | Edita um carro existente |
| `/car/<id>/delete/` | Exclui um carro |
| `/register/` | Cria uma nova conta de usuário |
| `/login/` | Realiza login |
| `/logout/` | Realiza logout |
| `/admin/` | Acessa o painel administrativo do Django |

## Validações implementadas

O formulário de veículos possui validações para evitar cadastros inconsistentes:

- O valor do carro não pode ser menor que R$ 10.000,00.
- O ano de fabricação não pode ser anterior a 1975.

## Inventário automático

O sistema possui sinais do Django que atualizam automaticamente o inventário sempre que um carro é salvo ou excluído.

A cada alteração, é criado um novo registro em `CarInventory` contendo:

- quantidade total de carros cadastrados;
- valor total somado dos veículos;
- data e hora do registro.

## Geração automática de biografia com IA

O projeto possui uma integração opcional com a API da OpenAI para gerar uma pequena biografia do veículo.

Quando a configuração `enable_car_ai_bio` estiver habilitada no painel administrativo, o sistema tenta gerar automaticamente uma descrição para o carro com base em:

- modelo;
- marca;
- ano do modelo.

Caso a integração não esteja configurada ou a geração não esteja habilitada, o sistema mantém uma mensagem padrão ou permite o preenchimento manual da biografia.

## Recomendações antes de publicar no GitHub

Antes de subir o projeto para um repositório público, verifique se os seguintes itens não estão sendo enviados:

```text
venv/
db.sqlite3
.env
media/
__pycache__/
*.pyc
```

O arquivo `.gitignore` já possui algumas dessas regras, mas vale reforçar a exclusão de arquivos gerados automaticamente e informações sensíveis.

## Possíveis melhorias futuras

- Melhorar o layout das telas de login, cadastro e formulário de veículos.
- Adicionar paginação na listagem de carros.
- Criar filtros por marca, ano e faixa de preço.
- Melhorar o tratamento de erros na integração com IA.
- Adicionar testes automatizados.
- Criar uma API REST para consulta dos veículos.
- Substituir o SQLite por PostgreSQL em ambiente de produção.
- Configurar variáveis sensíveis, como `SECRET_KEY`, via `.env`.

## Autor

Projeto desenvolvido por **Gustavo** como prática de desenvolvimento web com Django.
