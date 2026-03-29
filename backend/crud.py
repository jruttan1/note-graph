from sqlmodel import select, Session
from db import Note
from datetime import datetime
from schemas import NoteCreate, NoteResponse

def get_all_notes(session: Session):
    statement = select(Note)
    notes = session.exec(statement)
    return notes.all() # .all() unpacks reponse object

def get_note_from_id(id: int, session: Session): 
    statement = select(Note).where(Note.id == id)
    note = session.exec(statement) # this is not the same as python exec builtin, this just runs the query in the postgres session
    return note.first() # unpack container to return one object

def write_note(note: NoteCreate, session: Session):
    note = Note(title = note.title, content = note.content) # Id default field auto assigns on object creation in db
    session.add(note)
    session.commit()
    session.refresh(note) #refreshes local object to have id and datetime from postgres (basically pull from db after pushing) to give id to return statement below
    return note

def delete_note(id: int, session: Session):
    statement = select(Note).where(Note.id == id)
    note = session.exec(statement).one_or_none()
    if note:
        session.delete(note)
        session.commit()
        print(f'deleted note: {id}')
        return note
    else:
        print('note not found')

def update_note(id: int, new_note: NoteCreate, session: Session):
    statement = select(Note).where(Note.id == id)
    note = session.exec(statement).first()

    if note:
        print(f'updating note {note.content} to {new_note.content}')
        note.content = new_note.content
        note.title = new_note.title
        note.updated_at = datetime.now()
        session.add(note)
        session.commit()
        session.refresh(note)
        print('successful update')
        return note

    else:
        print(f'note not found with id: {id}')
    