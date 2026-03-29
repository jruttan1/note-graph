from celery import Celery
from dotenv import load_dotenv
import os
from embedding import create_embedding
from schemas import NoteCreate, NoteResponse
from sqlmodel import Session
from db import engine
from crud import get_note_from_id

load_dotenv()
redis_url = os.getenv('REDIS_URL')

app = Celery("queue", broker=redis_url, backend=redis_url)

@app.task
def embed_note(id: int) -> NoteResponse:
    with Session(engine) as session: # start db session for this task

        note = get_note_from_id(id, session) # pull the note you wanna update
        embedding = create_embedding(note) # call create embedding, returns a list of vectors
        note.embedding = embedding # add it to the note object
        
        session.add(note)
        session.commit()
        session.refresh(note)
    
        return note