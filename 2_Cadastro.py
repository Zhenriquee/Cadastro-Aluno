import streamlit as st
import controllers.controller as controller

st.title("Cadastro de Alunos para Natação")
    
with st.form(key='student_form'):
        full_name = st.text_input("Nome Completo")
        cpf = st.text_input("CPF")
        email = st.text_input("Email")
        contact_number = st.text_input("Número para Contato")
        days_of_week = st.multiselect("Dias da Semana", [
            "Segunda-feira", "Terça-feira", "Quarta-feira", 
            "Quinta-feira", "Sexta-feira", "Sábado","Domingo"
        ])
        schedule = st.selectbox("Horário", [
            "08:00 - 09:00", "09:00 - 10:00", "10:00 - 11:00", 
            "11:00 - 12:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00"
        ] ) 
          
        submit_button = st.form_submit_button(label='Cadastrar')

if submit_button:
        cpf = cpf.replace(".", "").replace("-", "")  # Remove a formatação para validação
        if not controller.validate_cpf(cpf):
            st.error("Erro: CPF inválido. Por favor, insira um CPF válido.")
        elif controller.is_cpf_registered(controller.format_cpf(cpf)):  # Verifica o CPF formatado
            st.error("Erro: CPF já cadastrado no sistema. Por favor, use um CPF diferente.")
        elif not days_of_week:
            st.error("Erro: Por favor, selecione ao menos um dia da semana para as aulas.")
        else:
            formatted_cpf = controller.format_cpf(cpf)  # Formata o CPF antes de salvar
            controller.save_student_data(full_name, formatted_cpf, email, contact_number, schedule, days_of_week)
            st.success("Aluno cadastrado com sucesso!")
