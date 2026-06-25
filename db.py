from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

url_to_db = "postgresql://andriididukh:1111@localhost:5432/postgres"
engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)
session = Session()