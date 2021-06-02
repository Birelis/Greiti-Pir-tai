import sqlite3
from zinutes import pasiekimai_one

def pasiekimai(paskyra, rezultatai):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT pasiekimai FROM paskyros WHERE name = ? ", [paskyra[1]])
    data = c.fetchone()
    data = list(data[0])

    #skubejau delto hard-codinau
    if(paskyra[2] >= 5 and paskyra[2] < 10):
        tikrinimas = True
        for i in data:
            if(i == '1'):
                tikrinimas = False
        if(tikrinimas == True):
            print("1. Pasiekimas: Iveikete 5 lygius")
            data.append('1')
    elif(paskyra[2] >= 10 and paskyra[2] < 15):
        tikrinimas = True
        for i in data:
            if(i == '2'):
                tikrinimas = False
        if(tikrinimas == True):
            print("2. Pasiekimas: Iveikete 10 lygiu")
            data.append('2')
    elif(paskyra[2] >= 15 and paskyra[2] < 20):
        tikrinimas = True
        for i in data:
            if(i == '3'):
                tikrinimas = False
        if(tikrinimas == True):
            print("3. Pasiekimas: Iveikete 15 lygiu")
            data.append('3')
    elif(paskyra[2] >= 20):
        tikrinimas = True
        for i in data:
            if(i == '4'):
                tikrinimas = False
        if(tikrinimas == True):
            print("4. Pasiekimas: Iveikete 20 lygiu")
            data.append('4')

    if(rezultatai[2] >= 50 and rezultatai[2] <75):
        tikrinimas = True
        for i in data:
            if(i == '5'):
                tikrinimas = False
        if(tikrinimas == True):
            print("5. Pasiekimas: Pasiekete 50 WPM")
            data.append('5')
    elif(rezultatai[2] >= 75 and rezultatai[2] <100):
        tikrinimas = True
        for i in data:
            if(i == '6'):
                tikrinimas = False
        if(tikrinimas == True):
            print("6. Pasiekimas: Pasiekete 75 WPM")
            data.append('6')
    elif(rezultatai[2] >= 100 and rezultatai[2] <125):
        tikrinimas = True
        for i in data:
            if(i == '7'):
                tikrinimas = False
        if(tikrinimas == True):
            print("7. Pasiekimas: Pasiekete 100 WPM")
            data.append('7')
    elif(rezultatai[2] >= 125 and rezultatai[2] <150):
        tikrinimas = True
        for i in data:
            if(i == '8'):
                tikrinimas = False
        if(tikrinimas == True):
            print("8. Pasiekimas: Pasiekete 125 WPM")
            data.append('8')
    elif(rezultatai[2] >= 150):
        tikrinimas = True
        for i in data:
            if(i == '9'):
                tikrinimas = False
        if(tikrinimas == True):
            print("9. Pasiekimas: Pasiekete 150 WPM")
            data.append('9')
    str = ""
    data = str.join(data)
    c.execute("UPDATE paskyros SET pasiekimai = ? WHERE name = ?", [data, paskyra[1]])
    conn.commit()
    conn.close()

def pasiekimu_sar(slapyvardis):
    print("Pasiekimu sarasas.")
    print()
    for i in pasiekimai_one:
        print(i)
    
    print()
    print("Paskyros pasiekimai.")
    print()


    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT pasiekimai FROM paskyros WHERE name = ? ", [slapyvardis])
    data = c.fetchone()
    data = list(data[0])

    for i in data:
        i = int(i)
        for y in range(len(pasiekimai_one)):
            if (i == y):
                print(pasiekimai_one[i-1])
    
    conn.commit()
    conn.close()

    val  = input("Iveskite bet ka jeigu norite grizti i pagrindi menu: ")



