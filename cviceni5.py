import sys

def inkrementuj_cisla(data):
    nova_data = []
    for radek in data:
        rozdeleny = radek.split(",")
        novy_radek = []
        for prvek in rozdeleny:
            try:
                prvek = str(int(prvek) + 1)
            except ValueError:
                pass
            novy_radek.append(prvek)
        nova_data.append(",".join(novy_radek))
            
    return nova_data

def nacti_radky(file_name):
    radky = []
    with open(file_name, "r") as file:
        for line in file:
            radky.append(line.strip())
    return radky

def zapis_radky(file_name, data):
    with open(file_name, "w") as file:
        for line in data:
            file.write(line + "\n")

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print(f'Pouziti: python {sys.argv[0]} jmeno_souboru')
        sys.exit()

    file_name = sys.argv[1]  # data.txt

    try:
        data = nacti_radky(file_name)
    except FileNotFoundError:
        print(f'Soubor {file_name} neexistuje')

    print(data)
    
    data = inkrementuj_cisla(data)

    print(data)

    name = file_name.split('.')  #  name = ['data', 'csv']

    file_name2 = name[0] + '2.' + name[1]  #  'data2.txt'
    zapis_radky(file_name2, data)