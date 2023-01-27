from app.src.db.database import Base, engine
from app.src.models.Transaction import *
print("Creating database ....")

Base.metadata.create_all(engine)