from pydantic import BaseModel, Field
from datetime import datetime

MAX_TITLE_LENGTH = 30 # subject to change but should be limited to a reasonable title length

# Explicit type to define server reponse schema when receiving a note object
class NoteResponse(BaseModel):
    id: int = Field(gt=0)
    content: str
    title: str = Field(max_length = MAX_TITLE_LENGTH)
    created_at: datetime
    updated_at: datetime

# Explicit type to define schema when user creates a note object
class NoteCreate(BaseModel):
    content: str
    title: str = Field(max_length = MAX_TITLE_LENGTH)