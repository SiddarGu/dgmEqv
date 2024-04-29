
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
x=np.array([2015,2016,2017,2018,2019,2020])
y1=np.array([1000,1200,900,1100,950,1100])
y2=np.array([2000,1700,1900,1500,1800,1600])
y3=np.array([700,750,800,850,900,950])

plt.plot(x,y1,label='Criminal Cases')
plt.plot(x,y2,label='Civil Cases')
plt.plot(x,y3,label='Family Cases')
plt.xticks(x,rotation=45)
plt.title('US Court Cases from 2015 to 2020')
plt.xlabel('Years')
plt.ylabel('Cases')
plt.legend()

for a,b in zip(x,y1):
    plt.text(a,b+5,b,ha='center',va='bottom',fontsize=11)
for a,b in zip(x,y2):
    plt.text(a,b+5,b,ha='center',va='bottom',fontsize=11)
for a,b in zip(x,y3):
    plt.text(a,b+5,b,ha='center',va='bottom',fontsize=11)

plt.tight_layout()
plt.savefig('line chart/png/400.png')
plt.cla()