class segitiga:
    def __init__ (self, T,i ):
        self.T=T
        self.i=i

    def terbalik(self):
        for self.i in range(1, self.T+1):
            print((self.T-self.i)*"*")

    def jajargenjang(self):
        for self.i in range(1, self.T+1):
            print((self.T-self.i)*" "+(self.T)*"*")

Segitiga_terbalik = segitiga(
    T=6,
    i=0
)
Segitiga_terbalik.terbalik()
print("================")
print("")
Segitiga_terbalik.jajargenjang()