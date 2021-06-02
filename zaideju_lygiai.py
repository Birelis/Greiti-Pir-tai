import sqlite3
import time
from zaidimas import zaidimas_pradzia, cls

def naujas_lygis(kurejas):

    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS zaideju_lygiai (
    kurejas DATATYPE text, 
    pavadinimas DATATYPE text, 
    tekstas DATATYPE text,
    laikas DATATYPE integer
    )
    """)
    cls()
    print("Naujo lygio kurimo procesas")
    print()

    pavadinimas = input("Iveskite lygio pavadinima: ")
    tekstas = input("Iveskite lygio teksta: ")
    laikas =  input("Iveskite laika per kuri norite jog lygis butu iveikas(sekundemis): ")

    c.execute("INSERT INTO zaideju_lygiai values (?, ?, ?, ?)", [kurejas, pavadinimas, tekstas, laikas])
    conn.commit()
    conn.close()

    print()
    print("Lygis sekmingai sukurtas, zaisti ji galesite pasirinkti per menu. Griztame i menu...")
    time.sleep(3)
    cls()

    return 0

def lygiu_saras(tikrinimas = 0):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()


    c.execute("SELECT kurejas, pavadinimas FROM zaideju_lygiai")
    data  = c.fetchall()

    cls()
    print("Zaideju sukurtu lygiu sarasas.")
    print()

    skaitliukas = 1
    for i in data:
        print(f"{skaitliukas} lygis. Kurejas: {i[0].capitalize()}. Pavadinimas: {i[1]}")
        skaitliukas +=1

    conn.commit()
    conn.close()

    if  tikrinimas == 0:
        niekas = input("Jei norite grizti i pagrindi menu iveskite bet koki simboli: ")
        cls()
        return 0
    elif tikrinimas == 1:
        return 0

def zaisti_zaidejo_lygi():
    cls()
    lygiu_saras(1)
    print()

    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    tikrinimas = True
    while (tikrinimas == True):
        pasirinkimas = input("Iveskite lygio pavadinima kuri norite zaisti: ")
        print()

        c.execute("SELECT * FROM zaideju_lygiai WHERE pavadinimas = ?", [pasirinkimas])
        data  = c.fetchone()

        if (data !=None):
            tikrinimas = False
        else:
            print("Tokio lygio nera, bandykite is naujo...")
            time.sleep(1)
            continue
    laikas = zaidimas_pradzia(data[2], '0') 

    if (laikas > data[3]):
        print("Lygio neiveikete per atitinkama laika.")
    else:
        print("Lygi iveikete per atitinkama laika.")



    conn.commit()
    conn.close()  
    val = input("Iveskite bet ka jei norite grizti i pagrindi menu: ")


    




    


