# 📱 BioWatch - Instagram Bio Monitoring API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0-green?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker&style=flat)](https://www.docker.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Enabled-blue?style=flat&logo=mysql)](https://www.mysql.com/)

🚀 **BioWatch** é uma API poderosa que permite que você monitore perfis do Instagram, rastreando mudanças nas bios e verificando a presença de textos específicos. Ideal para quem precisa de controle total sobre o conteúdo em perfis do Instagram!

## ✨ Recursos

- 🔒 **Autenticação JWT** para proteger suas rotas.
- 📄 **CRUD de Perfis** para monitorar handles do Instagram.
- 📝 **Histórico de Monitoramento** para rastrear alterações nas bios do Instagram.
- 🐳 **Dockerizado** para facilitar o deploy em qualquer ambiente.
- 🛠️ **Integração com MySQL** para armazenamento persistente.

## 🛠️ Instalação e Configuração
---
### 📋 Pré-requisitos

Certifique-se de ter instalado:

- [Python 3.10+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [MySQL](https://www.mysql.com/)

### 🚀 Como Rodar o Projeto

1. Clone o repositório:

    ```bash
    git clone https://github.com/seuusuario/biowatch.git
    cd biowatch
    ```

2. Crie e configure o arquivo `.env` com suas variáveis de ambiente:

    ```env
    DATABASE_URL=mysql+pymysql://user:password@localhost/db_name
    SECRET_KEY=your-super-secret-key
    ```

3. Construa e inicie o Docker container:

    ```bash
    docker build -t biowatch_app .
    docker run -d -p 8000:8000 --env-file .env biowatch_app
    ```

4. Acesse a documentação interativa da API:

    - Abra o navegador e vá para: [http://localhost:8000/docs](http://localhost:8000/docs) 🖥️

## 🔑 Autenticação

Esta API utiliza JWT (JSON Web Token) para autenticação. Para acessar as rotas protegidas, siga os passos:

1. Registre um novo usuário:
    - `POST /register`
2. Faça login para obter um token JWT:
    - `POST /login`
3. Use o token JWT nas suas requisições como Bearer Token.


## 🧪 Testes

Para rodar os testes (ainda a serem criados):
```bash
# Ative o ambiente virtual
source venv/bin/activate

# Rode os testes
pytest
```


## 🛡️ Segurança

	•	Mantenha seu SECRET_KEY seguro! ⚠️
	•	Utilize HTTPS para proteger a transmissão de tokens JWT.

## 🧰 Ferramentas Utilizadas

	•	FastAPI - Framework web moderno e de alta performance.
	•	Pydantic - Validação de dados e parsing.
	•	SQLAlchemy - ORM para interações com o banco de dados.
	•	Docker - Containerização para deploy fácil e consistente.
	•	MySQL - Banco de dados relacional.

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Feito com ❤️ por [Davi Antonaji](https://antonaji.com.br)
