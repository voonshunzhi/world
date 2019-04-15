import csv
from world.models.models import City;
from world import db;

f = open('../city.csv')
csv_f = csv.reader(f)


for _ in range(1):
    next(csv_f)

for row in csv_f:
    print(row)
    city = City(row[1],row[2],row[3],row[4])
    db.session.add(city);
    db.session.commit();

