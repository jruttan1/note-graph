from fastapi import FastAPI, HTTPException, Depends
import crud
import db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('starting server & db')
    db.create_db_and_tables()
    yield
    print('shutting down server, ending db connection')


app = FastAPI(lifespan=lifespan)


@app.get('/notes')
async def get_all_notes(session = Depends(db.get_session)): # Depends keyword from fastapi automatically opens and closes the postgres session
    notes = crud.get_all_notes(session) # uses crud functions from crud.py
    return notes
    
@app.get('/notes/{id}')
async def get_note_from_id(id: int, session = Depends(db.get_session)):
    note = crud.get_note_from_id(id, session)
    if note is not None:
        return note
    else:
        raise HTTPException(status_code=404, detail="Note not found in DB")


@app.post('/note')
async def update_content(content: str, title: str, session = Depends(db.get_session)):
    note = crud.write_note(content, title, session)
    return note
