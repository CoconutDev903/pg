
    
    #vek = input("Zadej svuj vek: ")
    #vek = 1
    #vek = int(vek)

    #vek += 1

    #print(f"Za rok ti bude {vek}")

#if vek >= 21:
#  print("Muzes pit v USA")
#else:
 #   print("Dej si colu")

#seznam = [1, 2, 3, "ctyri", 5]
#print(seznam)
#seznam.append("ahoj")
#print(seznam)

#print(f"Seznam ma {len(seznam)} prvku")

#print(seznam[2])

def vynasob_xty_prvek(seznam, x, nasobek):
    #funkce vezme x-ty prvek ze seznamu (zadano jako 1 pro první prvek), 
    #vynasobí ho pomoci * nasobek a ulozi zpet do seznamu na puvodni pozici
    #pozor, seznam muze mit mene prvku nez x
    if len(seznam) < x:
        print("V seznamu neni dostatek prvku")
        return seznam

    x -= 1
    if x < 0:
        print("Index mensi nez 0")
        return seznam

    seznam[x] *= nasobek
    return seznam
if __name__ == "__main__":

    seznam = vynasob_xty_prvek([1, 2, 3, 4, 5], 3, 1)
    print(seznam)

def spocitej_prumer(seznam):
    
    suma = sum(seznam)
    pocet = len(seznam)
    if pocet <= 0:
        print("Prazdny seznam")
        return None
    return suma / pocet

prumer = spocitej_prumer(seznam)
#prumer = print(sum(seznam)/len(seznam))
print(prumer)

def formatuj_text(student):
    znamky = student ["znamky"]
    prumer = spocitej_prumer(znamky)   
    prumer = round(prumer, 1)
    return f"Student {student["jmeno"]} {student["prijmeni"]}, Vek: {student["Vek"]}, Prumer: {prumer}"
    
student = {
    "jmeno": "Jan",
    "prijmeni": "Novak",
    "Vek": 21,
    "znamky": [1, 2, 1, 1, 3, 2]
    }
print (formatuj_text(student))
