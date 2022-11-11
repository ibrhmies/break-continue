isim = 'ibrahim SEVEN'

#-> bu haldeyken sadece harf i ise yazılır
for harf in isim:
    if (harf == 'i'):
        print(harf)


#-> continue komutuyla döngüde i harfine geldiğinde o harfi es geçer ve diğer harfi yazdırır 
for harf in isim:
    if (harf == 'i'):
        continue
    print(harf)




#-> break komutuyla S harfine den geldiğinde döngü biter devam etmez.
for harf in isim:
    if (harf == 'S'):
        break
    print(harf)    



#-> while döngüsünde break komutu for döngüsündekiyle aynı
i=0

while i<5:
    if(i == 3):
        break
    i+=1
    print(i)   



#-> while döngüsünde continue komutu kullanıldığında i değerini 1 arttırma eğer continue 
# komutunun altındaysa döngü durur ve devam etmez

i=0

while i<5:
    
    if(i == 3):
        continue
    i+=1
    print(i)   


#-> eğer i değerini 1 arttırmayı continue komutundan önceye alırsak göngü devam eder 


i=0

while i<5:
    i+=1
    if(i == 3):
        continue
    print(i)   


