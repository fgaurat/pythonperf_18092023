from PersonDAO import PersonDAO

def main():
    
    with PersonDAO("persons.db") as dao:
        p = dao.findAll()

    print("après")


if __name__=='__main__':
    main()
