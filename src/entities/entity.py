
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = '30507'
db_name = 'THEDB'
db_user = 'A2unb5rapVvKSixj'
db_password = 'tX5[pI4:fN3*jI4&'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')

usl = 'postgresql://30507:tX5[pI4:fN3*jI4&@30507/THEDB'

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    updated = Column(DateTime)
    last_updated = Column(String)

    def __init__(self, created_by) -> None:
        self.created = datetime.now()
        self.updated = datetime.now()
        self.last_updated = created_by