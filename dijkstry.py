class Droga:

    def __init__(self, wierzcholki, krawedzie):
        self.wierzcholki = wierzcholki
        self.krawedzie = krawedzie
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

    def Dijkstry(self, wagi):

if __name__=="__main__":
    d = Droga(["a","b","c","d","e","f"],[["a","b"],["c","d"],["b","c"],["d","e"],["f","e"]])
    print(d.droga({('a','b'):1 ,('b','c'):2 , ('c','d'):5 , ('a','c'):1 , ('a','d'):1 , ('b','d'):5 , ('c','d'):2}))
    print(d.Dijkstry([]))