import csv
import argparse
from Person import Person
from PersonDAO import PersonDAO
def main(csv_file):
    
    dao = PersonDAO('persons.db')
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            del row["id"]
            p = Person(**row)
            dao.save(p)


    


if __name__=='__main__':
    p = argparse.ArgumentParser()
    p.add_argument('csv_file',help="csv_file")
    args =p.parse_args()
    
    main(args.csv_file)

