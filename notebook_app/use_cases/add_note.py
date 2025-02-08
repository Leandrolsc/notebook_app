from entities.note import Note

class AddNoteUseCase:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, title, content):
        if title in self.repository.get_all_notes():
            raise ValueError("Uma nota com este título já existe!")
        self.repository.add_note(Note(title, content))