from openai import OpenAI
client = OpenAI()
from schemas import NoteCreate
from sqlmodel import select
from db import Note

def create_embedding(note: NoteCreate):
    text = {'title': note.title,
            'content': note.content}
    response = client.embeddings.create(
        input = str(text),
        model = "text-embedding-3-small"
    )
    embedding = response.data[0].embedding # unpack response object
    return embedding

def get_k_nearest_neighbors(note: NoteCreate, session, k): # make sure to handle session when calling
    search_embedding = create_embedding(note)

    knn = Note.embedding.cosine_distance(search_embedding)
    statement = select(Note).order_by(knn).limit(k)
    notes = session.exec(statement)

    return notes.all() 

