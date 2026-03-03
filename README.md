# 🏋️ Workout API - Desafio DIO

Esta é uma API de gerenciamento de competições de Crossfit, desenvolvida com **FastAPI**, **SQLAlchemy** e **Pydantic**. O projeto utiliza **Alembic** para migrações e **PostgreSQL** rodando via **Docker**.

## 🚀 Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web de alta performance.
- [SQLAlchemy 2.0](https://www.sqlalchemy.org/) - ORM para interação com banco de dados.
- [Alembic](https://alembic.sqlalchemy.org/) - Ferramenta de migrações.
- [Docker](https://www.docker.com/) - Para containerização do banco de dados.
- [fastapi-pagination](https://uriyyo-fastapi-pagination.netlify.app/) - Suporte a paginação customizada.

---

## ⚙️ Pré-requisitos

Antes de começar, você precisará ter instalado:
1. **Python 3.12 ou superior**.
2. **Docker e Docker Compose**.
3. **Make** (Utilitário de automação).
    - *Usuários Windows:* Instale via [Winget](https://github.com/ezwinports/make) (`winget install ezwinports.make`) e certifique-se de que está no seu PATH.

---

## 🛠️ Passo a Passo para Instalação

### 1. Clonar o repositório e criar o Ambiente Virtual
```bash
git clone <url-do-repositorio>
cd Workout_API
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 2. Subir o Banco de Dados (Docker)
**IMPORTANTE:** O banco deve estar rodando para que as migrações e a API funcionem.
```bash
docker-compose up -d
```
*O banco será exposto localmente na porta **5433** para evitar conflitos com instalações locais do Postgres na porta 5432.*

### 3. Rodar as Migrações do Banco
O banco de dados precisa ser estruturado antes de iniciar a API.
```bash
# Cria a revisão inicial (se ainda não existir)
make create-migrations d="init-db"

# Aplica as migrações ao banco
make run-migrations
```

### 4. Iniciar a API
```bash
make run
```
Acesse a documentação interativa em: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 📌 Funcionalidades Implementadas (Desafio)

### 🔍 Filtros Customizados
- No endpoint `GET /atletas`, é possível filtrar por `nome` (busca parcial) e `cpf`.

### 📄 Paginação (Limit/Offset)
- Implementada utilizando `fastapi-pagination`. Os resultados retornam com metadados de total de registros e links de navegação.

### 🛡️ Tratamento de Exceções
- **Status 303 (See Other):** Caso tente cadastrar um atleta com um CPF já existente, a API retornará:
  `"Já existe um atleta cadastrado com o cpf: x"`.

### 📦 Resposta Simplificada
- O endpoint de listagem de atletas foi customizado para retornar apenas `nome`, `centro_treinamento` e `categoria`.

---

## ⚠️ Possíveis Problemas e Soluções (FAQ)

### 1. Comando `make` não encontrado
Certifique-se de que o executável do `make` está na variável de ambiente PATH do seu sistema. No Windows, após a instalação, reinicie o terminal.

### 2. Conexão Recusada com o Banco
Verifique se o Docker está rodando (`docker ps`). Lembre-se que a aplicação se conecta na porta **5433** (configurada no `.env` e `docker-compose.yml`).

### 3. Erro de Importação Cíclica (Circular Import)
Os modelos de `Atleta`, `Categoria` e `CentroTreinamento` possuem relacionamentos entre si. Para evitar erros, as classes são referenciadas como strings nos relacionamentos (ex: `relationship("CategoriaModel", ...)`).

### 4. Erro no Delete (Status 204)
O status HTTP 204 indica "No Content". Portanto, o endpoint de exclusão **não possui** `response_model` e não deve retornar nenhum corpo na resposta.

### 5. Swagger vazio ou 404
Certifique-se de acessar a rota correta: `/docs`. Além disso, verifique se o `api_router` foi incluído corretamente no `main.py` antes da função `add_pagination(app)`.

---

## 📂 Estrutura do Projeto
```text
workout_api/
├── atleta/            # Módulo de atletas (Model, Schema, Controller)
├── categorias/        # Módulo de categorias
├── centro_treinamento/# Módulo de CTs
├── configs/           # Configurações de DB e Variáveis de Ambiente
├── contrib/           # Classes e dependências genéricas
├── main.py            # Ponto de entrada da aplicação
└── routers.py         # Centralização das rotas
```

---
*Desenvolvido como parte do desafio técnico de APIs Assíncronas com FastAPI.*
