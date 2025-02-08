import json
import os
from entities.note import Note

class NoteRepository:
    def __init__(self, file_path="notes.json"):
        self.file_path = file_path
        self.notes = {}
        self.load()
    
    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.notes = {k: Note(k, v) for k, v in data.items()}
    
    def save(self):
        with open(self.file_path, "w") as f:
            data = {k: v.content for k, v in self.notes.items()}
            json.dump(data, f)
    
    def add_note(self, note):
        self.notes[note.title] = note
        self.save()
    
    def delete_note(self, title):
        del self.notes[title]
        self.save()
    
    def update_note(self, note):
        self.notes[note.title] = note
        self.save()
    
    def get_all_notes(self):
        return self.notes.copy()