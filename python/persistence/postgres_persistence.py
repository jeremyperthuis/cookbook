from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

try :
    db = create_engine('postgresql://postgres:password@localhost:5432/satellite')
    conn = db.connect()
except OperationalError as e:
    print(e)
db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")

db.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

result_set = db.execute("SELECT * FROM films")
for r in result_set:
    print(r)
