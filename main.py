lista = [i for i in open("uzenetek.txt", "r").readlines()]

#region A
feladatA = "".join(lista).count("?") + "".join(lista).count("-")
print(feladatA)
#endregion

#region B
adatok = {}

for i in range(1, 101):
    adatok[f'C{i}'] = {}
    for j in range(0, 10):
        adatok[f'C{i}'][f'N{j}'] = 0

for i in lista:
    for j in range(0, 100):
        if i[j] == "?" or i[j] == "-":
            continue
        else:
            adatok[f'C{j+1}'][f'N{i[j]}'] += 1

megoldas = ""
for i in range(1, 101):
    nagy = 0
    ertek = 0
    for j in range(0, 10):
        if adatok[f'C{i}'][f'N{j}'] > nagy:
            nagy = adatok[f'C{i}'][f'N{j}']
            ertek = j
    megoldas += str(ertek)
print(megoldas)
#print(megoldas == "7610922751913275142233435073915524642160008422684973049146293643594970710907471138712178244571230807")
#endregion

#region C1
stat = {}
tevedesek = 0

for i in range(0, 10):
    stat[f'N{i}'] = 0

for sor in lista:
    for i in range(0, 100):
        helyeskarakter = megoldas[i]

        if sor[i] == "?" or sor[i] == "-":
            tevedesek += 1
        else:
            if sor[i] != helyeskarakter:
                tevedesek += 1
                stat[f'N{sor[i]}'] += 1
print(stat.items())
print(tevedesek)
#endregion
                
#region C2
szamstatok = [0 for i in range(100)]
temp = 0

for i in lista:
    for j in range(0, 100):
        helyes = megoldas[j]
        karakter = i[j]

        if karakter != "?" or karakter != "-" or karakter != helyes:
            temp += 1

        szamstatok[j] += temp
        temp = 0
#print(szamstatok)
#endregion

#region C3
szamstatok = []

for i in range(100):
    szamstatok.append([])

print(szamstatok)
#endregion

#region D
legtobbhiba = 0
megoldassor = 0
megoldaskezdo = 0

temphiba = 0    
kezdo = 0
for index in range(0, 500):
    for karindex in range(0, 100):
        karakter = lista[index][karindex]
        helyes = megoldas[karindex]

        if karakter == "-" or karakter == "?" or karakter != helyes:
            temphiba += 1

            if temphiba > legtobbhiba:
                legtobbhiba = temphiba
                megoldassor = index + 1
                megoldaskezdo = karindex + 1
        else:
            temphiba = 0
    temphiba = 0    
    kezdo = 0

print(legtobbhiba, megoldassor, megoldaskezdo)
#endregion
