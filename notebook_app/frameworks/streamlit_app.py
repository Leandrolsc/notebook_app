import streamlit as st
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from interface_adapters.repositories import NoteRepository
from use_cases.add_note import AddNoteUseCase
from use_cases.delete_note import DeleteNoteUseCase
from use_cases.update_note import UpdateNoteUseCase
from use_cases.load_notes import LoadNotesUseCase

# Configuração inicial
if "repo" not in st.session_state:
    st.session_state.repo = NoteRepository()

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