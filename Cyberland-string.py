name = "Efe Kaan"
surname = "Karaman"
age = "16"
karşılama = ('benim adım' ' ' + name + ' ' + surname + ' ' + 'yaşım' ' ' + age + ' ' 'hoşgeldin')
print(karşılama)
uzunluk = len(karşılama)
print(karşılama[-1])

# len ile ifadenin uzunluğu bulunur
# Eğer ifade birleşik ise boşluk için aralarına ' ' konur
# Print'in ardından bir değişkenimizi belirttik diyelim
# Dik parantez []'in arasına hangi sayı veya rakam konulursa, o değişken hangi harfe denk geldiğini söyler
# Eğer dik parantez arasında negatif bir sayı koyarsak, o değişkendeki hangi sayıya denk geldiğini SONDAN başlayarak söyler

print (karşılama[4:10])
# Eğer dik parantez'e 2 sayının arasına 2 nokta konulursa, o sayıların arasında hangi harf var onu söyler
print(karşılama[:21])
# Eğer dik parantez'e başta 2 nokta konulacak şekilde bir sayı konulursa, o sayıya kadar olan ifadeyi bize sunar
print (karşılama[6:])
# Eğer dik parantez'e sonda 2 nokta konulacak şekiklde bir sayı konulursa, o sayıdan başlayan ifadeyi bize sunar
print (karşılama[2:20:5])
# Böyle birşey yazarsak göründüğü gibi karmaşık bir sonuç çıkar
print (karşılama[::-1])
# Böyle birşey yazarsak ifademizi tersten yazar (:+:)
# Eğer negatif yerine pozitif yazarsak :+: 'nın değeri yoktur

karşılama_upper = karşılama.upper()
print(karşılama_upper)
# Eğer Upper komutu ile yazarsak ifademiz İngiliz alfabesine uygun olarak tüm ifadeyi BÜYÜK harfle yazar
karşılama_lower =  karşılama.lower()
print(karşılama_lower)
# Eğer Lower komutu ile yazarsak ifademiz İngiliz alfabesine uygun olarak tüm ifadeyi KÜÇÜK harfle yazılır
karşılama_split = karşılama.split()
print(karşılama_split)
print(karşılama_split[1])
# Eğer Split komutu ile yazarsak ifademizi ayırır

karşılama_strip = karşılama.strip()
print(karşılama_strip)
print(karşılama_strip[1])
# Strip komutu Benim adım Efe Kaan Karaman yaşım 16 hoşgeldin

karşılama_join = "-".join(karşılama)
print(karşılama_join)
# Join komutu ifademizin her harfin arasına (bir sayı-harf belirtirsek) onu koyar
karşılama_find = karşılama.find("Karaman")
print(karşılama_find)
# Find komutu bize belirttiğimiz ifadenin nerde olduğunu söyler

karşılama_startswith = karşılama.startswith("E")
print(karşılama_startswith)

karşılama_endswith = karşılama.endswith("e")
print(karşılama_endswith)

karşılama_replace = karşılama.replace('Efe','Müsavat')
print(karşılama_replace)
# Replace komutu belirttiğimiz nesneyi bir nesne ile değişir
