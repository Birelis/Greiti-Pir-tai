from aprasymas import aprasymas
from zinutes import *
from zaidimas import lygiu_pradzia
from pasiekimai import pasiekimu_sar
from paskyra import paskyros_perziura
from zaidimas import cls
from topai import topai

def lygiai(paskyra):
    while(True):
        print(f"""Zaidimas: Greiti pirštai\nBusena: Prisijunges\nPaskyra: {paskyra[1].capitalize()}\nDabartinis lygis: {paskyra[2]}\n\n1 - Testi lygius.\n2 - Perziureti lygiu sarasa\n3 - Pasiekimu sarasas(bei paskyros pasiekimai)\n4 - Paskyros perziura\n5 - Zaideju TOP 10\n6 - Aprasymas\n7 - Grizti atgal
            """)

        pasirinkimas = input("Iveskite savo pasirinkimą(1-4): ")

        if pasirinkimas == "1":
            lygiu_pradzia(paskyra)
        elif pasirinkimas == "2":
            lygiu_perziura()
        elif pasirinkimas == "3":
            pasiekimu_sar(paskyra[1])
        elif pasirinkimas == "4":
            paskyros_perziura(paskyra[1])
        elif pasirinkimas == "5":
            topai()
        elif pasirinkimas == "6":
            aprasymas()
        elif pasirinkimas == "7":
            cls()
            return 0 


def lygiu_perziura():
    cls()
    skaitliukas = 1
    for i in lygiu_tekstas:
        print(f"Lygis: {skaitliukas}")
        print(f"Tekstas: {i}")
        print()
        skaitliukas+=1
    
    val  = input("Iveskite bet ka jeigu norite grizti i pagrindi menu: ")
    cls()
