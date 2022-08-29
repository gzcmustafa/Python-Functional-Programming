x=["python","java","perl","scala"]
y=["ruby","python","java","php"]

kesisim=[i for i in x if (i in x and i in y)]
print("kesişim= " + str(kesisim))

fark=[i for i in x if ( i in x and i not in y)]
print("fark = " + str(fark))
