import time

t1=time.time()
t1=t1+60*60 # 1 saat ekler

t2=time.gmtime(t1)

print(t2)

# Time-Sleep

for i in range(5):
    print(i)
    time.sleep(6)