import time #zaman modülü
import sys #system işlemleri modülü


print("""
            aaaa     a    a  aaaa   aaaaa  a   a    a 
           aaaaaa     a  a   aaaa   a   a  a    a  a
          a      a   a    a  a  a   aaaaa  a   a    a
          """) 

def sonuc(girdi): #tek tek sonuc yazmamak için
    print("sonuc",girdi)

print("orta düzey hesap makineme hoş geldiniz.")
time.sleep(2)#programın beklemesi
print("-"*30)
islemler = ["topla :x","çıkar :y","çarp: c","böl :d","çıkmak için[q]"]
print(islemler)
while True:# basit etkileşimli kabuk için sürekli girdi alma
    istek = input(">>> ")
    istek1 = istek.split()#girdiyi boşluklardan parçalara bölme

    if istek == "q":
        break
        sys.exit[0]
    
    if len(istek1) != 3: #yanlış girişi engellemek için
        print("hatalı giriş :: '12 x 13' şeklinde giriniz")
        break

    
    ilk_sayı = int(istek1[0])#girdinin birinci parçası ilk sayıdır
    ikinci_sayı = int(istek1[2])#girdinin üçüncü parçası ikinci sayıdır
    islem = istek1[1].lower()# girdinin 2 parçası işlmedir lower ile her zaman küçük harfdir
    islemler_listesi = ["x","y","d","c"]
    
    

    if islem == "x":
        sonuc(ilk_sayı+ikinci_sayı)#sonuc fonksiyonum
        sys.stdout.flush()#tahsis edilen hafızayı geri veriyoruz

    elif islem == "y":
        sonuc(ilk_sayı-ikinci_sayı)
        sys.stdout.flush()

    elif islem == "c":
        sonuc(ilk_sayı*ikinci_sayı)
        sys.stdout.flush()
        
    elif islem == "d":
        try:#hata ayıklamak için
            sonuc(ilk_sayı/ikinci_sayı)
            sys.stdout.flush()
        except ZeroDivisionError: #ilgili hata 
            print("0 a bölünme tanımsızdır.") 
    else:
        print("yanlıs giriş lütfen yönlendirmelere uyunuz")
        print(islemler)

    
