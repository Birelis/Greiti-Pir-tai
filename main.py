from aprasymas import aprasymas
from paskyra import e_paskyra, n_paskyra, paskyros_perziura
from  zaideju_lygiai  import naujas_lygis, lygiu_saras, zaisti_zaidejo_lygi
from lygiai import lygiai
from zaidimas import cls
from topai import topai

cls()
# MENU
while(True):
    paskyra = [False, ""]
    while(paskyra[0] == False):
        # Menu - Neprisijunges
        print("""Zaidimas: Greiti pirštai\nBusena: Neprisijunges\n\n1 - Susikurti naują paskyrą\n2 - Prisijungti prie egzistuojančios paskyros\n3 - Aprašymas
        """)
        pasirinkimas = input("Iveskite savo pasirinkimą(1-3): ")

        if pasirinkimas == "1":
            paskyra = n_paskyra()
        elif pasirinkimas == "2":
            paskyra = e_paskyra()
        elif pasirinkimas == "3":
            aprasymas()
    
    while(paskyra[0] == True):
        print(f"""Zaidimas: Greiti pirštai\nBusena: Prisijunges\nPaskyra: {paskyra[1].capitalize()}\n\n1 - Pradėti/Testi žaisti "Greiti Pirštai" lygius\n2 - Sukurti savo lygi\n3 - Perziureti sukuru lygiu sarasa\n4 - Zaisti zaidejo sukurta lygi\n5 - Paskyros perziura\n6 - Zaideju TOP 10\n7 - Aprasymas
        """)
        pasirinkimas = input("Iveskite savo pasirinkimą(1-5): ")
        cls()

        if pasirinkimas == "1":
            lygiai(paskyra)
        elif pasirinkimas == "2":
            naujas_lygis(paskyra[1])
        elif pasirinkimas == "3":
            lygiu_saras()
        elif  pasirinkimas == "4":
            zaisti_zaidejo_lygi()
        elif pasirinkimas == "5":
            paskyros_perziura(paskyra[1])
        elif pasirinkimas == "6":
            topai()
        elif pasirinkimas == "7":
            aprasymas()



