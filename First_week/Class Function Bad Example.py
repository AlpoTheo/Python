class ders:
    adi:str=""
    notu:int=0

class ogrenci:
    ogr_no:int = 0
    ogr_adi:str = ""
    notlar:ders = None


def __init__(self):
    self.notlar = []

def not_ekle(self,ders_adi:str,ders_notu:int):
    yeni_ders= ders()
    yeni_ders.adi = ders_adi
    yeni_ders.notu = ders_notu
    self.notlar.append(yeni_ders)
    

def print(self):
    print(self.ogr_no,self.ogr_adi,self.ortalama)
    self.ortalama_hesapla()
    

def ortalama_hesapla(self):
    ort = 0
    for d in self.notlar:
        ort= ort + d.notu    
    ort=ort/len(self.notlar)
    self.ortalama=ort
    


sinif=[]
ogr1= ogrenci()
ogr1.ogr_no=212121
ogr1.ogr_adi="Alp Doruk Şengün"
ogr1.not_ekle("OOP",60)
ogr1.not_ekle("Algoritma",70)
ogr1.not_ekle("Elektrik",80)
sinif.append(ogr1)

ogr2= ogrenci()
ogr2.ogr_no=212122
ogr2.ogr_adi="Mustafa Emre Kılınç"
ogr2.not_ekle("OOP",60)
ogr2.not_ekle("Algoritma",70)
ogr2.not_ekle("Elektrik",80)
sinif.append(ogr2)

for ogr in sinif:
    ogr.print()