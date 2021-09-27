class Animal:
    def __init__(self, habitat, jenis_makanan, aktivitas ):
        self.habitat = habitat
        self.jenis_makanan = jenis_makanan
        self.aktivitas = aktivitas

    def printname(self):
        print(self.habitat)
        print(self.jenis_makanan)
        print(self.aktivitas)

class aves(Animal):
    def __init__(self, habitat, jenis_makanan, aktivitas):
       super().__init__(habitat,jenis_makanan,aktivitas)

    def tampilanaves(self):
        print("Habitat       : ", self.habitat)
        print("Jenis Makanan : ", self.jenis_makanan)
        print("aktivitas     : ", self.aktivitas)
    

class mamalia(Animal):
    def __init__(self, habitat, jenis_makanan, aktivitas):
       super().__init__(habitat,jenis_makanan,aktivitas)

    def tampilanmamalia(self):
        print("Habitat       : ", self.habitat)
        print("Jenis Makanan : ", self.jenis_makanan)
        print("aktivitas     : ", self.aktivitas)

x = aves("terestial","herbivora","diurnal/nokturnal")
y = mamalia("terestial","herbivora/karnivora","diurnal/nokturnal")

print("Kelas Burung (Aves)")
x.tampilanaves()
print("=============================================")
print("Kelas Mamalia (Mamals)")
y.tampilanmamalia()
print("=============================================")
print("Keterangan:")
print("Terestial : Hewan yang habitatnya di darat")
print("Herbivora : Hewan pemakan tumbuhan")
print("Karnivora : Hewan pemakan daging")
print("Diurnal   : Hewan yang aktif mencari makan di siang hari")
print("Nokturnal : Hewan yang aktif mencari makan di malam hari")


