import csv
from world.models.models import Country;
from world import db;

f = open('../country.csv')
csv_f = csv.reader(f)


for _ in range(1):
    next(csv_f)

for row in csv_f:
    print(row)
    row[4] = None if row[4] == 'NULL' or row[4] == '' else int(row[4])
    row[5] = None if row[5] == 'NULL' or row[5] == '' else int(row[5])
    row[6] = None if row[6] == 'NULL' or row[6] == '' else int(row[6])
    row[7] = None if row[7] == 'NULL' or row[7] == '' else float(row[7])
    row[8] = None if row[8] == 'NULL' or row[8] == '' else float(row[8])
    row[9] = None if row[9] == 'NULL' or row[9] == '' else int(row[9])
    country = Country(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
    db.session.add(country);
    db.session.commit();

