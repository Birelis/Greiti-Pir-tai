import difflib

def klaidu_taisymas(cases):
    skaitliukas = 0
    for a,b in cases:     
        print('Pateiktas tekstas: {}\nJusu tekstas: {}'.format(a,b))  
        print()
        for i,s in enumerate(difflib.ndiff(a, b)):
            if s[0]==' ': continue
            elif s[0]=='-':
                print(u'Truksta "{}" pozicijoje {}'.format(s[-1],i))
                skaitliukas +=1
            elif s[0]=='+':
                print(u'Padarėte klaida "{}" pozicijoje {}'.format(s[-1],i))  
                skaitliukas +=1  
        print() 
    print("Jus padarete " + str(skaitliukas) + " klaidas.")


    # text = "As myliu medzius"

# print("Pakartokite teksta")
# print(text)

# mas = inputas()
# val = mas[0]

# cases = [(text, val)]

# klaidu_taisymas(cases)
