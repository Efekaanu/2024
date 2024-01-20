sayi=4.2
sayi2=-5.5
print(type(sayi2))

sayi=-16.8
sayi2=-8.9
print(type(sayi))

dogru_mu=True
yanlis_mi=False
print(type(dogru_mu))

# Type komutu tür demektir

sayi1=45
sayi_float=float(sayi)
print("int to float",sayi_float)

ondalik1=3.14
ondalik2=0.5
sayi=4
sayi_int=int(ondalik1)

print("float to int", sayi_int)
sayi_bool=int(dogru_mu)
print("bool to int", sayi_bool)
# Eğer birşeyi diğer birşeye dönüştürmek istiyorsak (to) komutu kullanılır 

print(type(sayi_bool))

kullanici_adi=input("Lütfen Adınızı Giriniz:")
print("Hoşgeldin",kullanici_adi)

sayi=int(input("1. Sayıyı gir"))
sayi2=int(input("2. Sayıyı gir"))
print(sayi+sayi2)
# input komutu ile program bize cevaba göre cümle sunar
# Eğer toplama çıkarma işlemlerinde değişkenlerin toplamının cevabı birleşik hali çıkarsa örn:60+70=6070 
# Eğer böyle çıkarsa ayırmak için (int) komutu kullanılır örn: 60+70=130
