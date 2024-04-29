
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
ax = plt.subplot()
month = ['January', 'February', 'March', 'April']
a = [2000,1900,2100,1800]
b = [2200,2300,2400,2500]
c = [1800,2100,2200,2400]

ax.bar(month, a, width=0.3, label='Factory A')
ax.bar(month, b, bottom=a, width=0.3, label='Factory B')
ax.bar(month, c, bottom=np.array(a)+np.array(b), width=0.3, label='Factory C')

plt.xlabel('Month')
plt.ylabel('Working hours')
plt.title('Working hours of three factories from January to April 2021')
plt.legend(loc='upper left')
ax.set_xticks(month)
ax.set_xticklabels(month, rotation=45, ha="right")

for i, v in enumerate(a):
    ax.text(i-0.15, v/2+900, str(v), color='black', fontweight='bold')
for i, v in enumerate(b):
    ax.text(i-0.15, v/2+a[i]+900, str(v), color='black', fontweight='bold')
for i, v in enumerate(c):
    ax.text(i-0.15, v/2+a[i]+b[i]+900, str(v), color='black', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/349.png')
plt.clf()