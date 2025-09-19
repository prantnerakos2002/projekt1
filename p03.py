# 3. alkalom
def szam_bekerese(legnagyobb_szam):

 szam = input("Kérek egy számot:")

 if szam.isdigit():
    szam = int(szam)
    if szam==0:
        print("nem ismremem a nullát")
    elif szam > legnagyobb_szam:
        print("Túl nagy számot adtál meg")
    else:
        print("Jó")
 else:
    print("Nem számot adtál meg")
 return szam

#program inditása
muvelet = input("Milyen műveletet akar végrehajtani? {+,-, *,/}")
egyik_szam = szam_bekerese(10)
print(egyik_szam)
masik_szam = szam_bekerese(100)
if muvelet == "+":
    eredmeny = egyik_szam + masik_szam
elif muvelet == "-":
    eredmeny = egyik_szam - masik_szam
    eredmeny = egyik_szam + masik_szam
print(f"az eredmeny: {egyik_szam} {muvelet} {masik_szam} = {egyik_szam} = {eredmeny}")
print(masik_szam)



def veletlenszam(max):
    import random
    szam = random.randint(0, max)
    return szam






def egeszszam_bekerese():
    while True:
        szam = input("Kérek egy egész számot:")
        szam = int(szam)
        break
    print("Nem egész számot adott meg")
    return szam







#  a program inditása = input("Kérek egy  másik számot:")
