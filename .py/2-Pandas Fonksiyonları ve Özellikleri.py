#1.Pandas'ın Kurulumu

#Bir sistemde Python ve PIP kuruluysa NumPy’nin kurulumu çok kolaydır. Bu komutu kullanarak kurulumu yapabilirsiniz:
#pip install pandas
#Bu komut başarısız olursa, Anaconda, Spyder vb. gibi zaten NumPy’nin kurulu olduğu bir python dağıtımı kullanın.

#1.1.Pandas'ı Projeye Dahil Etmek
#import pandas as pd

#1.2.Pandas Sürümünü Kontrol Etme

print(pd.__version__)

#Kaggle vb. sitelerden indirdiğimiz datasetlerini incelemek için df = pd.read_csv("Dosya Yolu")

import numpy as np
import pandas as pd 

#CSV Dosyasını Çekme 

df = pd.read_csv("employees.csv")
df

print("--------------------------------------------------")

print("Pandas'taki Veri Yapıları\n1.Pandas Series\n2.DataFrame Veri Çerçevesi\n3.Indexes - Indeksler")

ps = pd.Series([1, 2, 4, 5, 7, 9]) #Seriler tek boyutlu dizilerdir. 
ps

ps.index #Index sayısını verir.

ps.values #NumPy array olarak verir. 

ps_1 = pd.Series([2, 4, 6, 8], index = ['a', 'b', 'c', 'd'])
ps_1

#Veri Çerçevesi
veri_c = pd.DataFrame(np.random.rand(3, 2), columns = ['Sütün 1', 'Sütün 2'], 
                      index = ['a', 'b', 'c']) 
veri_c
#3 satır, 2 sütündan oluşan, satırların ve sütünların isimleri olan random sayılardan oluşan DF oluşturma.

plakalar = {'İstanbul':'34', 'Bursa':'16', 'Ankara':'06'}

nufus = {'İstanbul' : 15000000, 'Bursa' : 8000000, 'Ankara' : 10000000}

veri_c1 = pd.DataFrame({'Plaka Kodları' : plakalar, 'Nüfus' : nufus })

veri_c1

print("--------------------------------------------------")

print("Verilere Ulaşma\n1.loc (location) - Etiketlerle ulaşmak\n2.iloc - Sayılarla ulaşmak")

veri_c1.iloc[1, 0] #2. şehrin plaka numarasını getir.

veri_c1.iloc[:, 0] #Tüm şehirleri getirir.

df.iloc[[0, 3, 5], [0, 7]] #Sadece sayılarla indeksleme yaptık.

veri_c1.loc[['İstanbul', 'Bursa'], ['Plaka Kodları', 'Nüfus']]

#Loc ile mantıksal sınama - büyük, küçük, var mı yok mu ? 

veri_c1.loc[veri_c1['Plaka Kodları'] == '34']

veri_c1['Bölge'] = ['Marmara', 'Marmara', 'İç Anadolu'] #Yeni bir sütün eklemek için kullanılır.

veri_c1 


#Üçüncü Veri Yapısı İndeksler - Değiştirilemez Listeler

indeks_1 = pd.Index([1, 2, 3, 4])

indeks_2 = pd.Index([3, 4, 5])

#indeks_1[2] = 99

#Hata vermesi normal, hata verdiğini görmeniz için silmedim.

indeks_1.intersection(indeks_2) #Index 1 - Index 2 arasındaki kesişim kümesi

indeks_1.union(indeks_2) #Index 1 - Index 2'nin birleşim kümesi

indeks_1.difference(indeks_2) #Index 1 - Index 2'nin farkı

print("--------------------------------------------------")

print("Pandas Önemli Fonksiyonlar")

df.head() #Datasetin ilk 5 verisini listeler.

df.tail() #Datasetin son 5 verisini listeler.

#Head ve Tail fonksiyonlarının içerisine girilen sayı kadar veri listeler.

df.head(8) #Python da index sayısı 0'dan başladığı için 0'dan 8'e kadar olan verileri listeler. (0 dahil 8 değil)

df.tail(3) #Bir üst maddedekiyle aynı özelliğe sahiptir.

print("--------------------------------------------------")

df.info() #Kolonların veri tiplerini listeler.

df.transpose() #Yatay eksendekiler dikey eksene, dikey eksendekiler yatay eksene geçer.

df.shape #Sütün ve satır sayısını verir.

df.describe() #Verilerin min, max gibi sayısal değerlerini listeler.

df.mean() #Ortalamasını alır.

df.Team.unique() #Tekil verileri getirir. - Aykırı Veri

df.groupby('Team').sum().iloc[:, 0] #sum, std, min, max gibi matematiksel işlemlerde yapılabilir.

print("--------------------------------------------------")

#Apply ve Map Fonksiyonları

def fonksiyon_ismi(x):
    return x + 200000

fonksiyon_ismi(100000)

df.Salary.map(lambda x: x+200000) #Salary sütünündaki her bir indexe 200000 ekledik. 
df.Salary.apply(fonksiyon_ismi)

print("--------------------------------------------------")

df.sort_values(by = ['Salary', 'Bonus %'], ascending = False) #Maaşı azdan çoka, çokdan aza ve iki kolona göre sıralama.

#Yeniden isimlendirme yaptıktan sonra kalıcı olmasını istiyorsak inplace = True yazmamız yeterlidir.

df.rename(columns = {'Bonus %' : 'Bonus_%', 'Team' : 'Teams'}).head() #Kolonları yeniden isimlendirme.

df['New Column'] = np.random.randint(10, size = df.shape[0])
df

#Yeni bir kolon oluşturarak dizinin sonuna ekler.

df.Team.value_counts(ascending = True) #True ya da False ASC - DESC 





