from fastapi import APIRouter, Depends
from ..db import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/trade")
def execute_trade(request: schemas.TradeJournalCreate, db: Session = Depends(database.get_db)):
    new_trade = models.TradeJournal(**request.dict())
    db.add(new_trade)
    db.commit()
    db.refresh(new_trade)
    return new_trade
