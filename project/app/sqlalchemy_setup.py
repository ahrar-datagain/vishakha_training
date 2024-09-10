from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from django.conf import settings

# Create the SQLAlchemy engine
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get session
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
