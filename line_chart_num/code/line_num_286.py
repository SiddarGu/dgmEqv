
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)
x=np.array([2015,2016,2017,2018,2019])
y1=np.array([120,150,200,190,220])
y2=np.array([150,180,210,220,230])
y3=np.array([45,50,60,70,80])
plt.plot(x, y1, label="Novels published", linewidth=2, color="red")
plt.plot(x, y2, label="Movies released", linewidth=2, color="green")
plt.plot(x, y3, label="Art exhibitions held", linewidth=2, color="blue")
plt.xticks(x)
ax.set_title("Arts and Culture Output in the Last Five Years")
ax.set_xlabel("Year")
ax.set_ylabel("Output")
ax.legend(loc="upper right")
for xa, ya, za in zip(x, y1, y1):
    plt.text(xa, ya, '%.0f' % ya, ha='center', va='bottom', fontsize=10, color="red")
for xb, yb, zb in zip(x, y2, y2):
    plt.text(xb, yb, '%.0f' % yb, ha='center', va='bottom', fontsize=10, color="green")
for xc, yc, zc in zip(x, y3, y3):
    plt.text(xc, yc, '%.0f' % yc, ha='center', va='bottom', fontsize=10, color="blue")
plt.tight_layout()
plt.savefig('line chart/png/298.png')
plt.clf()