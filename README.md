# Sistema de Gestão de Projetos

Este projeto consiste em um sistema simples de gestão de projetos desenvolvido como parte de uma atividade prática. O objetivo é permitir o controle de projetos em andamento, membros da equipe de desenvolvimento e tarefas atribuídas a cada membro.

## Objetivo

Desenvolver uma aplicação que:
- Controle projetos ativos.
- Gerencie membros da equipe alocados a cada projeto.
- Registre e acompanhe o andamento de tarefas associadas a cada membro e projeto.

## Estrutura do Sistema

O sistema é composto por três principais componentes:

1. **Banco de Dados Relacional** (MySQL ou PostgreSQL):
   - Armazena as informações de projetos, membros e tarefas.
   - Relacionamentos entre tabelas foram modelados de forma a refletir a estrutura da equipe e do trabalho.

2. **Scripts SQL**:
   - Criação das tabelas (`projeto`, `membro`, `tarefa`).
   - Inserção de dados fictícios.
   - Consultas úteis para gerenciamento, como:
     - Listar membros de um projeto.
     - Exibir tarefas de um membro.
     - Verificar tarefas atrasadas.

3. **Interface com Streamlit**:
   - Visualização de projetos, membros e tarefas.
   - Cadastro de novas tarefas com formulário interativo.
   - Seleção de membros e projetos com `st.selectbox()`.
   - Inserção de datas com `st.date_input()` e descrição com `st.text_area()`.