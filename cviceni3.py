def my_range_while(start, stop, step=1):
    vysledek = []
    x = start

    while (x > stop if step < 0 else x < stop):
        vysledek.append(x)
        x += step
    return vysledek


#def my_enumerate_for(iterable, start=0):
    vysledek = []
    for x in range(0, len(iterable)):
        vysledek.append((x+start, iterable[x]))
    return vysledek

#def my_enumerate_for2(iterable, start=0):
    vysledek = []
    for value in iterable:
        vysledek.append((start, value))
        start += 1
    return vysledek

def my_enumerate_while(iterable, start=0):
    vysledek = []
    i = 0
    while i < len(iterable):
        vysledek.append((i + start, iterable[i]))
        i+=1
    return vysledek


def my_zip(*iterables):
    iterables = [
        ["Alice", "Bob", "Karel", "Eva", "Martin"],
        [30, 20, 24, 18, 27],
        [50, 80, 90, 55, 67]
    ]


    
    vysledek = []
    lenght = min(len(iterable) for iterable in iterables)
    i = 0
    while i < lenght:
        value = []
        for iterable in iterables:
            value.append(iterable[i])
        vysledek.append(value)
        i += 1
    return vysledek

if __name__=="__main__":
    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"],
    vek = [30, 20, 24, 18, 27],
    vaha = [50, 80, 90, 55, 67]



    vysledek = my_zip(jmena, vek, vaha)

    #print(list(range(1,10,2)))
    #print(my_range_while(1, 10,))
    
    #print(list(enumerate(["aaa", "bbb", "ccc"])))
    #print(my_enumerate_for(["aaa", "bbb", "ccc"], 100))
    #print(my_enumerate_while(["aaa", "bbb", "ccc"], 100))

    #print(list(zip(
    #    ["Alice", "Bob", "Eva"],
    #    [24, 25, 20],
    #    ["Praha", "Cesko Budejovice", "Pisek"]
    #)))
