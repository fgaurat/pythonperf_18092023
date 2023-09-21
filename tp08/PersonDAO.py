import sqlite3
from Person import Person

class PersonDAO:


    def __init__(self,db_file) -> None:
        self._con = sqlite3.connect(db_file)
        self.cur = self._con.cursor()

    def findAll(self):
        # all = []
        res = self.cur.execute("SELECT * FROM persons_tbl")

        for data in res.fetchall():
            p = Person(*data)
            yield p
            # all.append(p)
        
        # return all

    def save(self,person):
#         sql = f""" INSERT INTO persons_tbl(first_name,last_name,email,gender,ip_address) 
# VALUES('{person.first_name}','{person.last_name.replace("'"," ")}','{person.email}','{person.gender}','{person.ip_address}')
# """

        sql = " INSERT INTO persons_tbl(first_name,last_name,email,gender,ip_address) VALUES(?,?,?,?,?)"

        # v = person.__dict__.values()
        self.cur.execute(sql,(person.first_name, person.last_name, person.email, person.gender, person.ip_address))
        self._con.commit()

    def __del__(self):
        self._con.close()
        

