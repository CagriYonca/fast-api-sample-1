import csv
import datetime

from models import *
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("/Users/cagimer/Projects/fetch-spacex/sars_2003_data.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_record = models.Record(
            date=datetime.datetime.strptime(row["date"], "%Y-%m-%d"),
            country=row["country"],
            cases=row["cases"],
            deaths=row["deaths"],
            recoveries=row["recoveries"],
        )
        db.add(db_record)

    db.commit()

db.close()