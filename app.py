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
            if nome and email:
                sucesso = sendstudenttosql(nome, cpf, sexo, uf, cidade, rua, numero, telefone_fixo, telefone_celular, idade)
                if sucesso:
                    st.success("Aluno gravado com sucesso!")
                else:
                    st.error("Erro ao gravar aluno.")
            else:
                st.warning("Nome e CPF são obrigatórios!")

def showaddproject():
    st.subheader("Adicionar Projeto")
    st.info("Formulário de projeto em construção")

def showaddtask():
    st.subheader("Adicionar Tarefa")
    st.info("Formulário de tarefa em construção")
#


if "tela" not in st.session_state:
    st.session_state["tela"] = "principal"

st.title("🧩 Gestão de Projetos")

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