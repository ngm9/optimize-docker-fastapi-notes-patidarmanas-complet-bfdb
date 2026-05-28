from fastapi import APIRouter, HTTPException
from app.models.notes import Note, NoteCreate
from typing import Dict
from uuid import uuid4

router = APIRouter()
notes_store: Dict[str, Note] = {}

@router.get("/notes")
def list_notes():
    return list(notes_store.values())

@router.get("/notes/{note_id}")
def get_note(note_id: str):
    note = notes_store.get(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post("/notes")
def create_note(note: NoteCreate):
    note_id = str(uuid4())
    new_note = Note(id=note_id, content=note.content)
    notes_store[note_id] = new_note
    return new_note

@router.delete("/notes/{note_id}")
def delete_note(note_id: str):
    if note_id not in notes_store:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes_store[note_id]
    return {"status": "deleted"}
