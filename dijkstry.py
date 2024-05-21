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

if __name__=="__main__":
    d = Droga(["a","b","c","d","e"],[["a","b"],["c","d"],["b","c"],["d","e"]])
    print(d.droga())