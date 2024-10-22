
Funcionalidades
    Página Inicial
    Listagem de postagens do blog, exibindo título, resumo e data de publicação.

Página de Postagem
    Exibição completa da postagem com título, conteúdo, autor e data. **Feito
    Formulário para adicionar comentários diretamente na página.

Página de Criação/edição de Postagem

    Formulário para criar ou editar postagens (acessível apenas para administradores ou autores).

Sistema de Registro e Login
    Formulários de registro e login.
    Autenticação de usuários para permitir que apenas usuários registrados comentem e criem postagens.

Implementação do Backend
Modelo de Dados

    Usuário: Armazenar informações sobre os usuários.
    Postagem: Armazenar detalhes das postagens, como título e conteúdo.
    Comentário: Armazenar comentários vinculados a postagens específicas.

Manipulação de Dados

    Usar o ORM (Object Relational Mapping) do framework (como SQLAlchemy para Flask ou o ORM do Django) para interagir diretamente com o banco de dados.
    As operações de CRUD (Create, Read, Update, Delete) para postagens e comentários são feitas diretamente nas rotas do servidor.

Anotoções

    Admin feita