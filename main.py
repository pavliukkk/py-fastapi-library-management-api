from typing import Generator, Annotated

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
from db.database import SessionLocal

app = FastAPI()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/authors/")
def read_authors(db: Annotated[Session, Depends(get_db)]):
    return crud.get_all_authors(db=db)