
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,8))
ax = plt.subplot()

x = np.arange(4)
y1 = [20000, 25000, 30000, 27000]
y2 = [14000, 17000, 19000, 21000]
y3 = [25000, 22000, 21000, 25000]

plt.plot(x,y1, label = "Attendance at museum A")
plt.plot(x,y2, label = "Attendance at museum B")
plt.plot(x,y3, label = "Attendance at museum C")

plt.xticks([0,1,2,3],['2015','2016','2017','2018'])
plt.title("Attendance at three museums from 2015 to 2018")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Attendance", fontsize=12)
plt.legend(loc="best", fontsize=12)

for a,b in zip(x,y1):
    ax.text(a, b, b, ha='center', va='bottom',fontsize=12)
for a,b in zip(x,y2):
    ax.text(a, b, b, ha='center', va='bottom',fontsize=12)
for a,b in zip(x,y3):
    ax.text(a, b, b, ha='center', va='bottom',fontsize=12)

plt.tight_layout()
plt.savefig(r"line chart/png/502.png")
plt.clf()