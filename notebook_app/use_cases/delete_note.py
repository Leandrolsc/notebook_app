class DeleteNoteUseCase:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, title):
        if title not in self.repository.get_all_notes():
            raise ValueError("Nota não encontrada!")
        self.repository.delete_note(title)