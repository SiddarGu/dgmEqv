
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot(1,1,1)
ax.bar(range(4),[2,1.8,3.2,1.2],width=0.2,label="Online Sales(billion)",color='b')
ax.bar(range(4),[3,3.4,2.8,2],bottom=[2,1.8,3.2,1.2],width=0.2,label="Offline Sales(billion)",color='r')

ax.set_xticks(range(4))
ax.set_xticklabels(["North America","Europe","Asia","South America"],rotation=45,ha="right",wrap=True)
ax.set_title("Comparison of online and offline sales in four major regions in 2021")
ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig('bar chart/png/412.png')
plt.clf()