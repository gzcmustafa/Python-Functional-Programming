x=[1,2,3]
print(len(x)) #liste eleman sayısını verir.
x.append(7)   #listenin en sonuna eleman ekler
print(x)      
x.pop()       #listenin sonundan eleman siler
print(x)
x.insert(0,-1) #listenin 0.indisine -1 değerini atar(değiştirir)
print(x)
del x[0]       #istenilen indisi siler
print(x)
x[1]=12        #istenilen indise yeni değer ataması yapar.
print(x)