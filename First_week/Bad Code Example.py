def ortalama_al(ogr):
    ort=(ogr["ders1"]+ogr["ders2"]+ogr["ders3"])/3
    return ort




sinif= {}
sinif[212121]={}
sinif[212121]["adi"]="Alp Doruk Şengün"
sinif[212121]["ders1"] = 60
sinif[212121]["ders2"] = 70
sinif[212121]["ders3"] = 80

sinif[212122]={}
sinif[212122]["adi"]="Mustafa Emre Kılınç"
sinif[212122]["ders1"] = 50
sinif[212122]["ders2"] = 20
sinif[212122]["ders3"] = 100

for ogr_no in sinif.keys():
    ort=ortalama_al(sinif[ogr_no])
    print(ogr_no,sinif[ogr_no]["adi"],ort)