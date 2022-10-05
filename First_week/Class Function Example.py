class ders:
    adi:str=""
    notu:int=0

class ogrenci:
    ogr_no:int = 0
    ogr_adi:str = ""
    notlar:ders = None
    ortalama:float = 0
    sinif:str = ""

def __init__(self,numara,adi,sinif,notlari):
    self.ogr_adi=adi
    self.ogr_no=numara
    self.sinif=sinif
    self.notlar_ekle = [notlari]

def notlar_ekle(self,notlari):
    self.notlar=[]
    for n in notlari:
        self.not_ekle("",n)
    


def not_ekle(self,ders_adi:str,ders_notu:int):
    yeni_ders= ders()
    yeni_ders.adi = ders_adi
    yeni_ders.notu = ders_notu
    self.notlar.append(yeni_ders)
    

def print(self):
    print(self.ogr_no,self.ogr_adi,self.sinif,self.ortalama)
    sablon="{}.sınıf öğrencisi{} numaralı {} isimli öğrencinin ortalaması: {}"
    self.ortalama_hesapla()
    

def ortalama_hesapla(self):
    ort = 0
    for d in self.notlar:
        ort= ort + d.notu    
    ort=ort/len(self.notlar)
    self.ortalama=ort
    


sinif=[]
sinif.append(ogrenci(212121,"Alp Doruk Şengün","2",60,70,80))
sinif.append(212122,"Mustafa Emre Kılınç","3",60,100,80)

for ogr in sinif:
    ogr.print()