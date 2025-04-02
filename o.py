cisla = [1,5,10,15,20,25,30]

cislo = int(input("zadejte prvni cislo"))
cislo2 = int(input("zadejte druhe cislo"))
znamenko = (input("zadejte znamenko"))

if znamenko == "+":
    vysledek = cislo+cislo2
    print("vysledek")
elif znamenko == "-":
    vysledek = cislo-cislo2
    print("vysledek")
elif znamenko == "*":
    vysledek = cislo*cislo2
    print("vysledek")
elif znamenko == "/":
    vysledek = cislo/cislo2
    print("vysledek")
else:
    input("zadejte spravne znamenko")

cisla.append(vysledek)
print(cisla)





