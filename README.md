# 🛗 ElevApi

API REST para gerenciamento de elevadores e manutenções, desenvolvida com **Django** e **Django REST Framework**.

---

## 📋 Sobre o Projeto

A **ElevApi** é uma API voltada para o setor de elevadores, permitindo o cadastro e controle de fabricantes, elevadores, empresas prestadoras de serviço e registros de manutenção. O projeto utiliza autenticação via JWT e segue boas práticas de desenvolvimento com Django REST Framework.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.12](https://www.python.org/)
- [Django 6.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/) — Autenticação por token JWT
- [dj-rql](https://github.com/cloudblue/django-rql) — Filtros avançados via RQL
- SQLite (banco de dados para desenvolvimento)

---

## 📁 Estrutura do Projeto

```
ElevApi/
├── app/                   # Configurações principais do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── elevator/              # App de elevadores e fabricantes
│   ├── models.py          # Manufacturer, Elevator
│   ├── serializers.py
│   ├── views.py
│   ├── filters.py
│   ├── permissions.py
│   └── urls.py
├── maintenance/           # App de manutenções
│   ├── models.py          # ProviderCompany, Maintenance
│   ├── serializers.py
│   ├── views.py
│   ├── filters.py
│   ├── permissions.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── .flake8
└── .gitignore
```

---

## 🗂️ Modelos Principais

### Fabricante (`Manufacturer`)
Armazena os dados dos fabricantes de elevadores (ex: Atlas Schindler, Otis).

### Elevador (`Elevator`)
Registra os elevadores instalados, vinculados a um fabricante e a um técnico responsável. Controla status operacional, capacidade, localização e datas.

### Empresa Prestadora (`ProviderCompany`)
Cadastro de empresas terceirizadas que realizam manutenções.

### Manutenção (`Maintenance`)
Registra todas as manutenções realizadas em elevadores, com tipo, técnico responsável, datas, custo e peças substituídas.

---

## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/mathRyan889/ElevApi.git
cd ElevApi
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate.bat

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 6. Inicie o servidor

```bash
python manage.py runserver
```

A API estará disponível em: `http://localhost:8000/`

---

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)**. Para acessar os endpoints protegidos, obtenha o token e envie no header de cada requisição.

**Obter token:**
```http
POST /api/v1/token/
Content-Type: application/json

{
    "username": "seu_usuario",
    "password": "sua_senha"
}
```

**Usar o token:**
```http
Authorization: Bearer <access_token>
```

**Renovar token:**
```http
POST /api/v1/token/refresh/

{
    "refresh": "<refresh_token>"
}
```

---

## 🔗 Endpoints

### Fabricantes
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/v1/manufacturer/` | Lista todos os fabricantes |
| `POST` | `/api/v1/manufacturer/` | Cadastra um novo fabricante |
| `GET` | `/api/v1/manufacturer/{id}/` | Detalhes de um fabricante |
| `PUT` | `/api/v1/manufacturer/{id}/` | Atualiza um fabricante |
| `PATCH` | `/api/v1/manufacturer/{id}/` | Atualiza parcialmente |
| `DELETE` | `/api/v1/manufacturer/{id}/` | Remove um fabricante |

### Elevadores
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/v1/elevator/` | Lista todos os elevadores |
| `POST` | `/api/v1/elevator/` | Cadastra um novo elevador |
| `GET` | `/api/v1/elevator/{id}/` | Detalhes de um elevador |
| `PUT` | `/api/v1/elevator/{id}/` | Atualiza um elevador |
| `PATCH` | `/api/v1/elevator/{id}/` | Atualiza parcialmente |
| `DELETE` | `/api/v1/elevator/{id}/` | Remove um elevador |

### Empresas Prestadoras
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/v1/provider-company/` | Lista todas as empresas |
| `POST` | `/api/v1/provider-company/` | Cadastra uma nova empresa |
| `GET` | `/api/v1/provider-company/{id}/` | Detalhes de uma empresa |
| `PUT` | `/api/v1/provider-company/{id}/` | Atualiza uma empresa |
| `PATCH` | `/api/v1/provider-company/{id}/` | Atualiza parcialmente |
| `DELETE` | `/api/v1/provider-company/{id}/` | Remove uma empresa |

### Manutenções
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/v1/maintenance/` | Lista todas as manutenções |
| `POST` | `/api/v1/maintenance/` | Registra uma nova manutenção |
| `GET` | `/api/v1/maintenance/{id}/` | Detalhes de uma manutenção |
| `PUT` | `/api/v1/maintenance/{id}/` | Atualiza uma manutenção |
| `PATCH` | `/api/v1/maintenance/{id}/` | Atualiza parcialmente |
| `DELETE` | `/api/v1/maintenance/{id}/` | Remove uma manutenção |

---

## 📦 Exemplos de Requisição

**Cadastrar Fabricante:**
```json
{
    "name": "Atlas Schindler",
    "cnpj": "00.028.986/0001-08",
    "tel": "(11) 98765-4321"
}
```

**Cadastrar Elevador:**
```json
{
    "serial_number": "SCH-2024-001",
    "manufacturer": 1,
    "model": "Schindler 3300",
    "capacity_kg": 630,
    "num_floors": 10,
    "installation_location": "Av. Goiás, 1200 - Centro - Goiânia/GO",
    "installation_date": "2024-03-10",
    "status": "operacional"
}
```

**Registrar Manutenção:**
```json
{
    "elevator": 1,
    "type": "preventiva",
    "description": "Lubrificação de cabos e verificação de freios",
    "technician": 1,
    "provider_company": 1,
    "start_date": "2024-03-10T08:00:00Z",
    "cost": 450.00,
    "status": "agendada"
}
```

---

## ✅ Qualidade de Código

O projeto utiliza **flake8** para garantir conformidade com o PEP8.

```bash
# Verificar erros
flake8 .

# Corrigir automaticamente
autopep8 --in-place --recursive .
```

---

## 👨‍💻 Autor

Desenvolvido por [Matheus Ryan](https://github.com/mathRyan889)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Matheus_Ryan-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/matheus-ryan-74110521b/)
[![GitHub](https://img.shields.io/badge/GitHub-mathRyan889-black?style=flat&logo=github)](https://github.com/mathRyan889)
[![Stolus](https://img.shields.io/badge/Stolus-Desenvolvimento_de_Software-orange?style=flat)](https://stolus.pythonanywhere.com)

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.