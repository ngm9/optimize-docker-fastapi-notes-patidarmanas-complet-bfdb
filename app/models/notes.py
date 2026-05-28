from pydantic import BaseModel

class Note(BaseModel):
    id: str
    content: str

class NoteCreate(BaseModel):
    content: str
