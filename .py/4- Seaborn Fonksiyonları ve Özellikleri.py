#!/usr/bin/env python
# coding: utf-8

# In[77]:

import pandas as pd
import seaborn as sns 

# In[78]:

tips = sns.load_dataset("tips") #Seaborn içerisindeki tips verisini ekleme.

# In[79]:

df = tips.copy() #Dataseti kopyalama.

# In[80]:

df.head()

# In[81]:

df.shape

# # Eksik Değer Kontrolü

# In[82]:

df.isnull() #Eksik verileri tablo olarak gösterir.

# In[83]:

df.isnull().sum() #Her değişkende kaç adet eksik olduğunu gösterir.

# In[84]:

df.info() #Veriseti yapısı

# In[85]:

kat_df = df.select_dtypes(include = ["category"])

# In[86]:

#Kategorilerin içerisinde kaç sınıfa sahip oldukları ve sınıfların isimleri
print("SEX")
print(kat_df.sex.unique())
print()
print("SMOKER")
print(kat_df.smoker.unique())
print()
print("DAY")
print(kat_df.day.unique())
print()
print("TIME")
print(kat_df.time.unique())
print()

# In[87]:

df["sex"].value_counts().plot.barh().set_title("SEX");

# In[88]:

df["smoker"].value_counts().plot.barh().set_title("SMOKER");

# In[89]:

df["day"].value_counts().plot.barh().set_title("DAY")

# In[90]:

df["time"].value_counts().plot.barh().set_title("TIME");

# In[91]:

#set_title() ile başlık,
#value_counts() NaN olmayan unique değerin kaç kez kullanıldığını gösterir.

# In[92]:

sns.barplot(x = 'day', y = 'total_bill', data = df)

# In[93]:

sns.barplot(x = 'day', y = 'total_bill', hue = 'size', data = df)
#Grafiğe bir boyut daha eklemek için hue parametresi kullanılır.

# # Distplot

# In[94]:

sns.distplot(df.tip) #Tek değişkenli bir dağılımı incelemenin en kolay yolu
#Hist + Yoğunluk Grafiği
#Grafik üzerindeki eğriyi kde parametresini değiştirerek kaldırabilirsiniz.
#Grafik üzerindeki histogramı kaldırmak için hist parametresini değiştirebilirsiniz.

# In[95]:

sns.distplot(df.tip, kde = False)

# In[96]:

sns.distplot(df.total_bill, hist = False)

# # Kdeplot

# In[97]:

sns.kdeplot(df.total_bill, shade = True) 
#shade grafiğin alt kısmını boyar.

# # Boxplot

# In[98]:

sns.boxplot(x = 'day', y = 'total_bill', hue = 'smoker', data = df)

# # Violinplot

# In[99]:

sns.violinplot(x = 'size', y = 'tip', hue = 'time', data = df)

# # Scatterplot

# In[100]:

sns.scatterplot(x = 'total_bill', y = 'tip', hue = 'time', data = df)

# # Lmplot

# In[101]:

sns.lmplot(x = 'total_bill', y = 'tip', hue = 'smoker', data = df)

# # Pairplot

# In[102]:

sns.pairplot(df, hue = 'smoker')

# In[103]:

sns.pairplot(df, kind = 'reg') #Grafiğe doğru eklemek için kind methodu kullanabilirsiniz.

# In[104]:

sns.heatmap(df.corr(), annot = True, linewidths = 2)
#Annot parametresi True olursa sayı değerlerini görebiliriz.
#Linewidths kutular arası boşluk bırakmayı sağlar.
#Corr = Data

# # Pointplot

# In[105]:

sns.pointplot(x = 'time', y = 'total_bill', hue = 'smoker', data = df)

# # FacetGrid

# In[106]:

#Grafik üzerine eklenen boyutları bölerek göstermek için kullanıır. sns.xplot(x, y, hue)

# In[107]:

diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()
df.head()

# In[108]:

df.info()

# In[109]:

#Cut değişkenimizin sınıflarını ordinal sıraya getirmeliyiz. Bu sıra (Fair, Good, Very Good, Premium, Ideal) şeklinde olacak.
from pandas.api.types import CategoricalDtype
cut_kategoriler = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories = cut_kategoriler, ordered = True))
#pandas.api.types içinden CategoricalDtype’ı dahil ettikten sonra astype() metodu ile sıralamasını yapıyoruz.

# In[110]:

sns.FacetGrid(df, hue="cut", height=5, xlim=(0, 1000)).map(sns.kdeplot, data=df, x="price", shade=True).add_legend()
#hue parametresi ile cut değişkenini boyut olarak ekledik.
#height parametresi bize grafiğimizin boyunu söylemektedir.
#xlim parametresinde ise x eksinini (0,1000) arasında kısıtlamış olduk
#add_legend() metodu ile cut değişkeninin kategori bilgilerini eklemiş olduk.

# In[118]:

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# In[119]:

mart = pd.read_excel("supermarket_sales.xlsx") #Dataseti import ettik.

# In[120]:

mart

# In[121]:

mart.shape #Datasetin satır ve sütün sayısını verir.

# In[122]:

mart.head() #Datasetin ilk 5 verisini verir.

# In[123]:

mart.tail() #Datasetin son 5 verisini verir.

# In[124]:

mart.describe() #Verilerin matematiksel işlemlerini yapar.


# In[125]:

plt.figure(figsize = (15,5)) #Grafik boyutu belirleme 

sns.countplot(x = 'Product line', data = mart)

# In[126]:

sns.countplot(y = 'Product line', data = mart) #Horizontal barplot

# In[127]:

sns.countplot(y = 'Product line', hue = "Gender", data = mart) #Kadın - Erkek kategorilerine göre listeler.

# In[128]:

plt.figure(figsize = (15,5))
sns.countplot(x = 'Product line', hue = "Gender", data = mart, palette = "gist_gray") #Grafik renginin belirlenmesi.

# In[129]:

plt.figure(figsize = (15,5))

sns.countplot(x = 'Product line', data = mart,
             facecolor = (1, 0, 1, 0),
              linewidth = 10,
              edgecolor = sns.color_palette('dark', 3))

# # Barplot

# In[130]:

sns.get_dataset_names() #Seabornun içindeki hazır datasetleri listeler.

# In[131]:

titanic = sns.load_dataset('titanic') #Hazır olan verisetini yükleme.

# In[132]:

titanic.head() #Verinin ilk 5 satırını verir.

# In[133]:

plt.figure(figsize = (15,3))
sns.barplot(x = 'Product line', y = 'Total', hue = 'Gender', data = mart)

# In[134]:

sns.barplot(x = 'Total', y = 'Product line', hue = 'Gender', data = mart)

# In[135]:

plt.figure(figsize = (15,5))
sns.barplot(x = 'Product line', y = 'Total', hue = "Gender", data = mart) #order komutuyla alfabetik bir şekilde sıralanabilir.
#order = ['column_name']
