import sqlite3
import time
from zaidimas import cls
from zinutes import pasiekimai_one

def n_paskyra():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS paskyros (
    name DATATYPE text, 
    password DATATYPE text,
    lygis DATATYPE integer,
    pasiekimai DATATYPE text,
    patirtis DATATYPE integer
    )
    """)

    c.execute("SELECT name FROM paskyros")
    data = c.fetchall()

    tikrinimas = True
    while(tikrinimas == True):
        tikrinimas = False
        slapyvardis = input("Iveskite paskyros slapyvardi: ")


        for i in data:
            if(i[0] == slapyvardis):
                cls()
                print("Slapyvardis jau uzimtas, prasome ivesti kitoki slapyvardi")
                tikrinimas = True
                break

    slaptazodis = input("Iveskite paskyros slaptažodi: ")

    c.execute("INSERT INTO paskyros VALUES (?, ?, ?, ?)", (slapyvardis, slaptazodis, 0, '0', 0))
    conn.commit()
    conn.close()
    print("Paskyra sekmingai sukurta. Griztame i pagrindini menu...")
    print()
    time.sleep(2)
    cls()

    return True, slapyvardis, 0

def e_paskyra():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    tikrinimas = True
    while(tikrinimas == True):

        slapyvardis = input("Iveskite paskyros slapyvardi: ")
        slaptazodis = input("Iveskite paskyros slaptažodi: ")


        c.execute("SELECT * FROM paskyros WHERE name = ?", [slapyvardis])
        data = c.fetchone()

        if(data != None):
            if(slaptazodis != data[1]):
                cls()
                print("Paskyra rasta, taciau netinkamas slaptazodis, bandykite is naujo")
                continue
            else:
                tikrinimas = False
        else:
            cls()
            print("Tokio slaptyvardzio nera, bandykite is naujo")
            print()
    conn.commit()
    conn.close()
    print("Prisijungta prie paskyros. Griztame i pagrindini menu...")
    print()
    time.sleep(2)
    cls()
    return True, slapyvardis, data[2]

def paskyros_perziura(slapyvardis):
    cls()
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT * FROM paskyros WHERE name = ?", [slapyvardis])
    data = c.fetchone()

    print(f"{data[0].capitalize()} Paskyra.")
    print(f"Iveikta {data[2]} Lygiai(-iu).")
    print(f"Surinkta {data[4]} patirties tasku.")
    print("Paskyros pasiekimu sarasas.")
    print()
    c.execute("SELECT pasiekimai FROM paskyros WHERE name = ? ", [slapyvardis])
    data = c.fetchone()
    data = list(data[0])

    for i in data:
        i = int(i)
        for y in range(len(pasiekimai_one)):
            if (i == y):
                print(pasiekimai_one[i-1])

    print()
    val = input("Iveskite bet ka kad gristi i menu: ")
    cls()

