#ortalaması %20'den daha uzak olanları seçen bir liste üretici yazın.
x=[10,20,50,60,60,70,40,60,55,53,32,31,11,7,23,34,20,14,18,19,90,80,70,98,97,99,100,21,45,67,50,52,32,45,67,65,45,78,45,90]

y=[i for i in x if i>sum(x)/len(x)]
print(y)