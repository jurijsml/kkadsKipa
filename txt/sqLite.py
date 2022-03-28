import splite3

db = sqlite3.connect('test.db')

#Tabulas Izveide
db.excute("""
          CREATE TABLE IF NOT EXISTS
          (id   INTEGER   PRIMARY KEY   NOT NULL,
          vards   TEXT   NOT NULL,
          alga   REAL,
          piezimes   CHAR(50)
          )
          """)

#Datu pievienošana
db.execute("""INSERT INTO darbinieki
           (id,vards,alga,piezimes)
           VALUES(1,'Anna',900.50,'Ekonomists')
           """)

db.commit()

#Datu iegūšana
dati=db.execute("""SELECT * FROM darbinieki
                WHERE id=1
                """)
rezultats = dati.fetchall()
print(rezultats)


db.execute(
  """
  CREATE TABLE IF NOT EXIST premijas
  (id   INTEGER   PRIMARY KEY AUTOINCREMENT   NOT NULL,
  pceturksnis   REAL,
  oceturksnis   REAL,
  tceturksnis   REAL,
  cceturksnis   REAL
  )
  """
)


p_ceturksnis("Ievadiet pirmā ceturkšņa prēmiju: ")
o_ceturksnis("Ievadiet otrā ceturkšņa prēmiju: ")
t_ceturksnis("Ievadiet trešā ceturkšņa prēmiju: ")
c_ceturksnis("Ievadiet ceturtā ceturkšņa prēmiju: ")

db.execute("""
           INSERT INTO premijas
           (pceturksnis,oceturksnis,tceturksnis,cceturksnis)
           VALUES(:pceturksnis:oceturksnis,:tceturksnis,:cceturksnis)
           """,{'pceturksnis':p_ceturksnis,'oceturksnis',o_ceturksnis,'tceturksnis',t_ceturksnis,'cceturksnis',c_ceturksnis})

db.commit()

dati = db.execute("""SELECT * FROM premijas
                  WHERE id=1
                  """)
rezultats = dati.fetchall()
print(rezultats)