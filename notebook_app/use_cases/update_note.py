from entities.note import Note

class UpdateNoteUseCase:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, title, new_content):
        if title not in self.repository.get_all_notes():
            raise ValueError("Nota não encontrada!")
        self.repository.update_note(Note(title, new_content))