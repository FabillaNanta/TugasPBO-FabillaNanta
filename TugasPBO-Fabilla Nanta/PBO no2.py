class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luasSegitiga(self):
        print((self.alas*self.tinggi)/2)

class balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def volumeBalok(self):
        print(self.panjang*self.lebar*self.tinggi)

segitiga = segitiga(
    alas = 20,
    tinggi = 10
)

balok = balok(
    panjang = 15,
    lebar=5,
    tinggi=7
)

segitiga.luasSegitiga()
balok.volumeBalok()