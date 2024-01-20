liste = [1,2,3,4,5]
print(liste)
print(liste[4])
# Cevabı 5 alırız çünkü sistem sayı saymaya 0'dan başlar 
# Bu olay program dillerine göre değişir
liste[4] = 50
print (liste)
# ! Atamalar sağdan sola yapılır
alt_liste = liste[2:4]
print(alt_liste)
# Sonucumuz [3,4] çıktı

# Tuple
tuple = (10,20,30)
print(tuple)
print(tuple[1])
# 1'i bulmaya çalıştık 20 çıktı
# UNUTMA: Program saymaya 0'dan başlar

# Kümeler
küme={100,200,300,400,500,100}
print(küme)
# Birden fazla aynı sayı yazılırsa sistem tek olarak cevap verir
küme.add(700)
print(küme)
# Add komutu adı üzerinde ifademize nesne ekler
küme.update([400,900])
print(küme)
# Update komutu ifadeyi bulup günceller

# dict dictionary sözlük
dict={'anahtar1':'değer1','anahtar2':'değer2'}
print(dict)
değer=dict['anahtar1']
print(değer)

küme_list=list(küme)
print(küme_list)
print(type(küme_list))

list_keys=list(dict.keys())
print(type(list_keys))
print(list_keys)

sayılar=[10,8,5,3,15]
en_büyük=max(sayılar)
en_küçük=min(sayılar)
print(en_büyük)
print(en_küçük)
sayılar.append(20)
sayılar.append(1)

yeni_en_büyük=max(sayılar)
yeni_en_küçük=min(sayılar)
print(yeni_en_büyük)
print(yeni_en_küçük)
print(sayılar)
# Max en fazla demektir
# Min en az demektir


sayılar.pop()
print(sayılar)

sayılar.sort()
print(sayılar)

sayılar.reverse()
print(sayılar)

print(sayılar.count(10))
# Count saymak demektir

aralık=range(1,50)
print(list(aralık))
# Range komutu türkçede aralık anlamına gelir list ile birleşince bir nesne ile bir nesnenin arasındaki sayıları harfleri listeler

import random
rastgele_sayı=random.randint(1,100)
print("tutulan sayı",rastgele_sayı)
# Random komutu kullanırsak ifadenin içerisinde rastgele birşey seçer
