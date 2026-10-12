def cislo_text(cislo):
    x = int(cislo)
    dodvaceti = [
        "nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset", 
        "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"
    ]
    desitky = { 2: "dvacet",
            3: "třicet",
            4: "čtyřicet",
            5: "padesát",
            6: "šedesát",
            7: "sedmdesát",
            8: "osmdesát",
            9: "devadesát"}
    
    if x < 0 or x > 100:
        return "Zadejte pouze čísla od 0 do 100"
    if x == 100:
        return "sto"
    if x < 20:
        return dodvaceti[x]
    else:
        d = x // 10
        j = x % 10
        if j == 0:
            return desitky[d]
        else:
            return f"{desitky[d]} {dodvaceti[j]}"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)