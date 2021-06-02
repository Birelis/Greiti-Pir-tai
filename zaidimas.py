import time
import os
import difflib
import sqlite3
from zinutes import *
from pasiekimai import pasiekimai

def zaidimas_pradzia(tekstas, patikrinimas = '0'):
    skaitliukas = 5
    while (skaitliukas != -1):
        cls()
        print("Informacija gauta(Isijunkite LT kalba). Zaidimas prasides po: "+ str(skaitliukas))
        skaitliukas -=1
        time.sleep(1)

    zaidejo_rez = zaidimas_procesas(tekstas)

    klaidu_kiekis = klaidu_taisymas(tekstas, zaidejo_rez[0])

    wpm = round((len(zaidejo_rez[0])/5)/(zaidejo_rez[1]/60),0)

    print("Zaidimas baigtas, jusu rezultatas.")
    print(f"Teksta atkortoje per {round(zaidejo_rez[1],0)} sekundes.")
    print(f"Klaidu padarete: {klaidu_kiekis}")
    print(f"Jusu WPM(Words per minute): {wpm}")
    print()

    if (patikrinimas == '0'):
        return round(zaidejo_rez[1],0)
    else: 
        return round(zaidejo_rez[1], 0), klaidu_kiekis, wpm

def lygiu_pradzia(paskyra):
    cls()
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute ("SELECT lygis FROM paskyros WHERE name = ?", [paskyra[1]])
    lygis = c.fetchone()
    lygis = lygis[0]+1

    print(f"Bus zaidziamas {lygis} Lygis")
    print()
    print(f"1 - Easy, Lygi reikia iveikti per {lygiu_sunkumas[lygis][0]} sekundziu ir galima padaryti tik {lygiu_sunkumas[lygis][1]} klaidas. ")
    print(f"2 - Medium, Lygi reikia iveikti per {lygiu_sunkumas[lygis][2]} sekundziu ir galima padaryti tik {lygiu_sunkumas[lygis][3]} klaidas.")
    print(f"3 - Hard, Lygi reikia iveikti per {lygiu_sunkumas[lygis][4]} sekundziu ir galima padaryti tik {lygiu_sunkumas[lygis][5]} klaidas.")
    print()
    print("Uz iveikta lygi gaunate patirties tasku.")
    print(f"Easy - {lygiu_patirtis[0]} patirties tasku; Medium - {lygiu_patirtis[1]} patirties tasku; Hard - {lygiu_patirtis[2]} patirties tasku;")
    print()
    valP = True
    while(valP):
        val = input("Pasirinkite sunkuma: ")

        if (val == '1'):
            lygiu_nustatytas_sunkumas = [lygiu_sunkumas[lygis][0], lygiu_sunkumas[lygis][1], lygiu_patirtis[0]]
            valP = False
        elif (val == '2'):
            lygiu_nustatytas_sunkumas = [lygiu_sunkumas[lygis][2], lygiu_sunkumas[lygis][3], lygiu_patirtis[1]]
            valP = False
        elif (val == '3'):
            lygiu_nustatytas_sunkumas = [lygiu_sunkumas[lygis][4], lygiu_sunkumas[lygis][5], lygiu_patirtis[2]]
            valP = False
        else: 
            print("Blogas pasirinkimas bandykite is naujo")
            print()
    # laikas, klaidos, wpm
    rezultatai = zaidimas_pradzia(lygiu_tekstas[lygis-1], '1')

    if(lygiu_nustatytas_sunkumas[0] > rezultatai[0] and lygiu_nustatytas_sunkumas[1] > rezultatai[1]):
        print(f"Sveikinu, iveikiate {lygis} lygi")
        print()

        conn = sqlite3.connect("data.db")
        c = conn.cursor()

        c.execute("SELECT patirtis FROM paskyros WHERE name = ?", [paskyra[1]])
        data = c.fetchone()

        patirtis = lygiu_nustatytas_sunkumas[2] + data[0]

        c.execute("UPDATE paskyros SET lygis = ?, patirtis = ? WHERE name = ?", [lygis, patirtis, paskyra[1]])
        conn.commit()
        conn.close()

        pasiekimai(paskyra, rezultatai)

        val = input("Iveskite bet ka, kad grizti i menu: ")
        cls()
    else:
        print(f"Lygis neiveiktas, bandykite dar karta.")
        val = input("Iveskite bet ka, kad grizti i menu: ")
        cls()


def zaidimas_procesas(tekstas):
    print()
    print("Tekstas kuris reikia atkartoti")
    print()
    print('"'+tekstas+'"')
    print()
    print("Jusu teksto langelis:")
    print()
    start = time.time()
    val = input()
    end = time.time()
    difference = end - start
    cls()
    return val, difference

def klaidu_taisymas(a, b):
    skaitliukas = 0 
    for i,s in enumerate(difflib.ndiff(a, b)):
        if s[0]==' ': continue
        elif s[0]=='-':
            # print(u'Truksta "{}" pozicijoje {}'.format(s[-1],i))
            skaitliukas +=1
        elif s[0]=='+':
            # print(u'Padarėte klaida "{}" pozicijoje {}'.format(s[-1],i))
            skaitliukas +=1  
    return skaitliukas



def cls():
    os.system('cls' if os.name=='nt' else 'clear')



