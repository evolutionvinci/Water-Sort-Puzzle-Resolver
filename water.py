import colorama
from colorama import init,Fore, Style
init()
numeri = list(map(int, input().split()))
entire=[]
EmptyContainer=2
riga=0
colonna=0
def stampa(lista,ri1,co1,ri2,co2):
    for colonna in range(4):
        for riga in range(len(lista)):
            if lista[riga][colonna]>=10:
                if lista[riga][colonna]==10:
                    if (colonna==co2 and riga==ri2) or (ri1==riga and colonna==co1):
                        print(Fore.BLUE + "a",end=' ')
                    else:
                        print(Fore.WHITE + "a",end=' ')
                if lista[riga][colonna]==11:
                    if (colonna==co2 and riga==ri2) or (ri1==riga and colonna==co1):
                        print(Fore.BLUE + "b",end=' ')
                    else:
                        print(Fore.WHITE +"b",end=' ')
                if lista[riga][colonna]==12:
                    if (colonna==co2 and riga==ri2) or (ri1==riga and colonna==co1):
                        print(Fore.BLUE + "c",end=' ')
                    else:
                        print(Fore.WHITE +"c",end=' ')
            else:
                if (colonna==co2 and riga==ri2) or (ri1==riga and colonna==co1):
                    print(Fore.BLUE + str(lista[riga][colonna]),end=' ')
                else:
                    print(Fore.WHITE +str(lista[riga][colonna]),end=' ')
        print(Fore.WHITE +"")
def check(completo):
    for col in range(len(completo)):
        if completo[col][0]==completo[col][1] and completo[col][0]==completo[col][2] and completo[col][0]==completo[col][3]:
            if col==len(completo)-1:
                return 1
        else:
            return 0
def core(ll,ris,cos,rid,cod,lenght):
    l=[]
    for r1 in range(len(ll)):
        l.append([])
        for c1 in range(4):
            l[r1].append(ll[r1][c1])
    if not(ris==rid and cos==cod):
        while lenght!=0:
            lenght=lenght-1
            l[rid][cod-lenght]=l[ris][cos+lenght]
            l[ris][cos+lenght]=0
        print(Fore.GREEN+"Innesto")
        if check(l)==1:
            print(Fore.RED+"FOUND")
            stampa(l,0,0,0,0,)
            return 1
        else:
            stampa(l,ris,cos,rid,cod)
            print("")
    else:
        if check(l):
            print("La matrice è gia completa")
            return 1
    for r in range(len(l)):
        zerinegativi=0
        for c in range(4):
            if l[r][c]==0:
                zerinegativi=zerinegativi+1
            if l[r][c]!=0:
                lunghezza=0
                while c+lunghezza<4 and l[r][c]==l[r][c+lunghezza]:
                    lunghezza=lunghezza+1
                for ri in range(len(l)):
                    if not(ri==r or l[ri][0]!=0):
                        zeri=0
                        for co in range(4):
                            if l[ri][co]==0:
                                zeri=zeri+1
                            else:
                                if l[ri][co-1]!=0:
                                    break
                            if lunghezza<=zeri and (l[r][c]==l[ri][co] or (co==3 and l[ri][co]==0)):
                                if l[ri][co]==l[r][c]:
                                    co=co-1
                                else:
                                    if lunghezza+zerinegativi==4:
                                        break
                                if 1==core(l,r,c,ri,co,lunghezza):
                                    stampa(l,ris,cos,rid,cod)
                                    print(Fore.RED+"^PASSAGGIO")
                                    return 1
                break
    print(Fore.RED+"No more possible movs")
    stampa(l,ris,cos,rid,cod)
    return 0
for r in range(int(len(numeri)/4)+EmptyContainer): #
    container=[]                                   #Crea una matrice
    for c in range(4):                             #La inizializza con zeri
        container.append(0)                        #Contiene anche le provette vuote
    entire.append(container)                       #
print(Fore.WHITE +"\nMatrice inizializzata con zeri")
stampa(entire,0,0,0,0)
for color in numeri:
    entire[riga][colonna]=int(color)
    if colonna==3:
        riga=riga+1
        colonna=0
        continue
    if riga==(int(len(numeri)/4)+EmptyContainer)+1:
        break
    colonna=colonna+1
print(Fore.WHITE +"\nMatrice di partenza completata:\n")
stampa(entire,0,0,0,0)
print("")
core(entire,0,0,0,0,0)
