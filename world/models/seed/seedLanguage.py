import csv
from world.models.models import Language;
from world import db;

f = open('../language.csv')
csv_f = csv.reader(f)


for _ in range(1):
    next(csv_f)

for row in csv_f:
    print(row)
    if row[2] == 'T':
        row[2] = True
    else:
        row[2] = False
    row[3] = float(row[3])
    language = Language(row[0],row[1],row[2],row[3])
    db.session.add(language);
    db.session.commit();

