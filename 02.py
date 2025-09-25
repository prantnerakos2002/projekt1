# adattípusok 2. óra
'''hosszabb megjegyzés
 ez egy több soros'''

szoveg = 'autorendszám'
szam = 15
logikai = True

print(szoveg)
print(szam)

szam +=1
print(szam)
print(logikai)
print(not logikai)
print (szam > 20)

print(szoveg[0])
print(szoveg[0:3])
print(szoveg[4:])
print(szoveg[4:8])
print(szoveg[-4:])

lista = ["habos", "kakaó"]
print (lista[0])
print (lista[1])
print (lista[0] + lista[1])
lista +=["tejszínes"]
print (lista)
print (lista[2],lista[0] + lista[1])

halmaz = {5, 4, 8, 5, 6, "alma"}
print(halmaz)
szotar = {"név": "Béla", "kor":43}
print(szotar)

eletkor = int(input("Kérem adja meg az életkorát: "))
eletkor += 5
print(eletkor)

print(szotar["név"],"kora:", eletkor)
print(szotar["név"],"kora:", eletkor, sep="-")
print(szotar["név"],"kora:\n", eletkor, sep="-", end="\n")

print("valameilyen szöveg".rjust(50,"_"))
print("valameilyen szöveg".ljust(50,"_"))
print("valameilyen szöveg".center(50,"_"))

# adattípsok
''' Ez egy több
soros megjegyzés'''

szoveg = "autórendszám"
szam = 15
logikai = True

print(szoveg)
print(szam)

szam *= 2
print(szam)
print(not logikai)
print(szam > 20)

print(szoveg[0])
print(szoveg[0:4])
print(szoveg[4:])
print(szoveg[4:8])
print(szoveg[-4:])

lista = ["habos", "kakaó"]
print(lista[0] + lista[1])
lista += ["tejszínes"]
print(lista)
print(lista[2], lista[0] + lista[1])

halmaz = {5 , 4 , 8 , 5, "alma"}
print(halmaz)

szotar = {"név": "Béla", "kor": 43}
print(szotar)

eletkor = int(input("Kérem adja meg az életkorát: "))
eletkor += 5
print(eletkor)
print(szotar["név"], "kora:\n", eletkor, sep="-", end="\n")

print("valami".rjust(50,"_"))
print("valami".ljust(50,"_"))
print("valami".center(50,"_"))