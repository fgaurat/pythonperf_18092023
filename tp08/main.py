from Person import Person
from PersonDAO import PersonDAO


def filter_male(all_persons:Person):
    for person in all_persons:
        if person.gender == "Male":
            yield person


def main():
    dao = PersonDAO('persons.db')
    l = filter_male()

    for p in l:
        print(p)

if __name__=='__main__':
    main()
