import datetime
import streamlit as st
import mysql.connector as mysql

def connect_mysql():
    return mysql.connect(
        host="localhost",
        user="root",
        password="aluno",
        database="gestao_projetos"
    )

#funções para enviar pro banco virão aqui
def dbsendmember(nome, email, cargo):
    try:
        conexao = connect_mysql()
        cursor = conexao.cursor()

        comando = """
            INSERT INTO membro (
                nome, email, cargo
            ) VALUES (%s, %s, %s)
        """

        valores = (nome, email, cargo)

        cursor.execute(comando, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        return True

    except Exception as e:
        print(f"[ERRO SQL] Não foi possível gravar o membro: {e}")
        return False
    
def dbsendproject(nome, descricao, data_inicio, data_fim):
    try:
        conexao = connect_mysql()
        cursor = conexao.cursor()

        comando = """
            INSERT INTO projeto (
                nome, descricao, data_inicio, data_fim
            ) VALUES (%s, %s, %s, %s)
        """

        valores = (nome, descricao, data_inicio, data_fim)

        cursor.execute(comando, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        return True

    except Exception as e:
        print(f"[ERRO SQL] Não foi possível gravar o projeto: {e}")
        return False
    
def dbsendtask(descricao, data_inicio, data_fim, status):
    try:
        conexao = connect_mysql()
        cursor = conexao.cursor()

        comando = """
            INSERT INTO tarefa (
                descricao, data_inicio, data_fim, status
            ) VALUES (%s, %s, %s, %s)
        """

        valores = (descricao, data_inicio, data_fim, status)

        cursor.execute(comando, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        return True

    except Exception as e:
        print(f"[ERRO SQL] Não foi possível gravar o projeto: {e}")
        return False
#

#funções para fazer o formulário de cada coisa
def showaddmember():
    st.header("Cadastro de Membro")
    st.markdown("Preencha os dados abaixo:")

    with st.form("form_member", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input("Nome")
            email = st.text_input("Email")
            cargo = st.text_input("Cargo")

        col_btn1, col_btn2 = st.columns([1, 1])

        with col_btn1:
            gravar = st.form_submit_button("Gravar", type="primary")

        if gravar:
            if nome and email and cargo:
                sucesso = dbsendmember(nome, email, cargo)
                if sucesso:
                    st.success("Membro gravado com sucesso!")
                else:
                    st.error("Erro ao gravar o membro.")
            else:
                st.warning("Todos os campos são obrigatórios!")

def showaddproject():
    st.header("Adicionar projeto")
    st.markdown("Preencha os dados abaixo:")

    with st.form("form_project", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input("Nome do projeto")
            descricao = st.text_input("Descrição")
            data_inicio = st.date_input("Data de Início", value=datetime.date.today())
            data_fim = st.date_input("Data de Término")

        col_btn1, col_btn2 = st.columns([1, 1])

        with col_btn1:
            gravar = st.form_submit_button("Gravar", type="primary")

        if gravar:
            if nome and descricao:
                if data_fim >= data_inicio:
                    sucesso = dbsendproject(nome, descricao, data_inicio, data_fim)
                    if sucesso:
                        st.success("Projeto gravado com sucesso!")
                    else:
                        st.error("Erro ao gravar o projeto.")
                else:
                    st.warning("A data de término deve ser maior ou igual à data de início.")
            else:
                st.warning("Todos os campos são obrigatórios!")

def showaddtask():
    st.header("Adicionar tarefa")
    st.markdown("Preencha os dados abaixo:")

    with st.form("form_project", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            descricao = st.text_input("Descrição da tarefa")
            data_inicio = st.date_input("Data de Início", value=datetime.date.today())
            data_fim = st.date_input("Data de Término")
            status = st.selectbox("Status da tarefa",options=["Em andamento", "Concluída", "Atrasada"])

        col_btn1, col_btn2 = st.columns([1, 1])

        with col_btn1:
            gravar = st.form_submit_button("Gravar", type="primary")

        if gravar:
            if descricao:
                if data_fim >= data_inicio:
                    sucesso = dbsendtask(descricao, data_inicio, data_fim, status)
                    if sucesso:
                        st.success("Tarefa gravada com sucesso!")
                    else:
                        st.error("Erro ao gravar a tarefa.")
                else:
                    st.warning("A data de término deve ser maior ou igual à data de início.")
            else:
                st.warning("Descrição é obrigatória!")


if "tela" not in st.session_state:
    st.session_state["tela"] = "principal"

st.title(" Gestão de Projetos")

if st.session_state["tela"] == "principal":
    st.subheader("Escolha uma opção:")

    if st.button("Adicionar Membro", key="btn_add_membro"):
        st.session_state["tela"] = "membro"

    if st.button("Adicionar Projeto", key="btn_add_projeto"):
        st.session_state["tela"] = "projeto"

    if st.button("Adicionar Tarefa", key="btn_add_tarefa"):
        st.session_state["tela"] = "tarefa"

elif st.session_state["tela"] == "membro":
    showaddmember()

elif st.session_state["tela"] == "projeto":
    showaddproject()

elif st.session_state["tela"] == "tarefa":
    showaddtask()