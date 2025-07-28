import streamlit as st
import sys
import os



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from auth.user_auth import UserAuth
from interface_adapters.repositories import NoteRepository
from use_cases.add_note import AddNoteUseCase
from use_cases.delete_note import DeleteNoteUseCase
from use_cases.update_note import UpdateNoteUseCase
from use_cases.load_notes import LoadNotesUseCase
from use_cases.calculate_compound_interest import CalculateCompoundInterestUseCase

st.set_page_config(
    page_title="Bloco de notas Streamlit")



def main_app():
        
    tab1, tab2 = st.tabs(["📝 Notas", "🧮 Calculadora de Juros"])

    with tab1:
    # Configuração inicial
        if "repo" not in st.session_state:
            st.session_state.repo = NoteRepository(st.session_state.username)

        repo = st.session_state.repo
        add_note = AddNoteUseCase(repo)
        delete_note = DeleteNoteUseCase(repo)
        update_note = UpdateNoteUseCase(repo)
        load_notes = LoadNotesUseCase(repo)

        # Interface
        st.title("📝 Bloco de Notas com Streamlit")

        with st.sidebar:
            st.header("Opções")
            new_title = st.text_input("Título da Nova Nota:")
            new_content = st.text_area("Conteúdo:")
            
            if st.button("Adicionar Nota"):
                try:
                    add_note.execute(new_title, new_content)
                    st.success("Nota adicionada!")
                except ValueError as e:
                    st.error(str(e))
            
            selected = st.selectbox("Selecione uma nota:", [""] + list(load_notes.execute().keys()))
            
            if selected and st.button("Excluir Nota"):
                try:
                    delete_note.execute(selected)
                    st.success("Nota excluída!")
                except ValueError as e:
                    st.error(str(e))

        # Edição
        notes = load_notes.execute()
        if selected and selected in notes:
            st.subheader(f"Editando: {selected}")
            edited = st.text_area("Conteúdo:", value=notes[selected].content, height=300)
            if st.button("Salvar Alterações"):
                try:
                    update_note.execute(selected, edited)
                    st.success("Alterações salvas!")
                except ValueError as e:
                    st.error(str(e))

        # Listagem
        st.divider()
        st.subheader("Todas as Notas")
        for title, note in notes.items():
            st.write(f"### {title}")
            st.write(note.content)
            st.divider()




    with tab2:
        st.header("🧮 Calculadora de Juros Compostos")

        st.subheader("Simule o crescimento do seu investimento ao longo do tempo")
        st.write("Avisos:")
        st.write("* A taxa de juros deve ser informada em termos anuais")
        st.write("* O aporte mensal é feito após o segundo Mês")
        
        # Entradas
        principal = st.number_input("Valor Inicial (R$)", min_value=0.0, step=100.0)
        annual_rate = st.number_input("Taxa de Juros Anual (%)", min_value=0.0, step=0.5) / 100
        time_unit = st.radio("Unidade de Tempo", ["Anos", "Meses"], index=0)
        time = st.number_input(f"Tempo ({time_unit.lower()})", min_value=0.0, step=1.0)
        monthly_contribution = st.number_input("Aporte Mensal (R$)", min_value=0.0, step=100.0)
        
        if st.button("Calcular"):
            future_value, monthly_data = CalculateCompoundInterestUseCase().execute(
                principal, annual_rate, time, time_unit.lower(), monthly_contribution
            )
            
            # Valor Futuro
            st.success(f"**Valor Futuro:** R$ {future_value:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            
            # Tabela Detalhada
            st.subheader("Detalhamento Mensal")
            import pandas as pd
            df = pd.DataFrame(monthly_data)
            
            # Formatação Monetária
            for col in df.columns[1:]:
                df[col] = df[col].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            
            st.dataframe(df, hide_index=True, use_container_width=True)


def login_page():
    st.title("🔒 Login")
    auth = UserAuth()
    
    with st.form("login"):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.form_submit_button("Entrar"):
                if auth.authenticate(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Credenciais inválidas!")
        
        with col2:
            if st.form_submit_button("Registrar"):
                try:
                    auth.register_user(username, password)
                    st.success("Registro realizado! Faça login.")
                except Exception as e:
                    st.error(str(e))

if __name__ == "__main__":
    if not st.session_state.get("logged_in"):
        login_page()
    else:
        st.button("Logout", on_click=lambda: st.session_state.clear())
        main_app()