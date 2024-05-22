class Droga:

    def __init__(self, wierzcholki, krawedzie):
        self.wierzcholki = wierzcholki
        self.krawedzie = sorted(krawedzie)
        for krawedz in krawedzie:
            if (not krawedz[0] in wierzcholki) or (not krawedz[1] in wierzcholki):
                raise Exception("Krawędź nie nalezy do wierzchołków")



    def droga(self):
        wierzcholkiA = []
        wierzcholkiB = []
        for krawedz in self.krawedzie:
            if (krawedz[0] in wierzcholkiA) or (krawedz[1] in wierzcholkiB):
                return False
            wierzcholkiA.append(krawedz[0])
            wierzcholkiB.append(krawedz[1])
        if (len((set(wierzcholkiA) | set(wierzcholkiB)) - (set(wierzcholkiA) & set(wierzcholkiB))) > 2):
            return False
        return True

    def Dijkstry(self, wagi, wierzchołek_startowy):
        self.wagi = dict(sorted(wagi.items()))
        drogi = {}
        wierzcholki = sorted(self.wierzcholki)
        print(self.wagi)
        print(self.krawedzie)
        drogi[0] = [wierzcholki[0], 0, 0]
        for wierzcholek in range(len(self.wierzcholki)-1):
            drogi[wierzcholek+1] = [self.wierzcholki[wierzcholek+1], 999999999, 0]
        for krawedz in self.krawedzie:
            print("wierzcholek: " + str(drogi[wierzcholki.index(krawedz[1])][2]))
            if drogi[wierzcholki.index(krawedz[1])][2] in wierzcholki:
                pass
            else:
                drogi[wierzcholki.index(krawedz[1])][2] = krawedz[0]
            droga_do_poprzedniego = drogi[wierzcholki.index(krawedz[0])][1]
            print("obecny: " + str(drogi[wierzcholki.index(krawedz[1])]))
            print("droga do poprzedniego: " +  str(drogi[wierzcholki.index(krawedz[0])][1]))
            print("waga teraz: " +str(self.wagi[tuple(krawedz)]))
            
            if drogi[wierzcholki.index(krawedz[1])][1] > droga_do_poprzedniego + self.wagi[tuple(krawedz)]:
                drogi[wierzcholki.index(krawedz[1])][1] = droga_do_poprzedniego + self.wagi[tuple(krawedz)]
                drogi[wierzcholki.index(krawedz[1])][2] = krawedz[0]
            print(drogi[wierzcholki.index(krawedz[1])])
        return drogi


if __name__=="__main__":
    d = Droga(["a","b","c","d","e","f"],[["a","b"],['a','c'],['a','f'],["c","f"],["c","d"],['c','e'],['b','d'],["b","e"],["d","f"],["d","c"],['f','c'],['f','e'],["f","d"]])
    #print(d.droga())
    print(d.Dijkstry({('a','b'):3 ,('a','c'):10 , ('a','f'):15 , ('c','f'):2 , ('c','d'):7 , ('c','e'):9 , ('b','d'):4, ('b','e'):25 , ('d','f'):5 , ('d','c'):2 , ('f','c'):5 , ('f','e'):6 , ('f','d'):3},['a']))