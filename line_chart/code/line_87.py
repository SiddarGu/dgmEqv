
import matplotlib.pyplot as plt

x = [2000, 2001, 2002, 2003, 2004]
y1 = [1100, 1200, 800, 1100, 1200]
y2 = [900, 1000, 1200, 1300, 1400]
y3 = [800, 900, 1100, 1200, 1400]
y4 = [1000, 1100, 900, 1000, 1300]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

ax.plot(x, y1, label='Wheat Production(tons)', color='#7f6d5f')
ax.plot(x, y2, label='Rice Production(tons)', color='#557f2d')
ax.plot(x, y3, label='Soybean Production(tons)', color='#2d7f5e')
ax.plot(x, y4, label='Corn Production(tons)', color='#2d7f5e')

plt.title('Global Crops Production in 2000-2004')
plt.xticks(x)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., frameon=False)
plt.grid(True,which='both',axis='y')
plt.tight_layout()

plt.savefig('line chart/png/182.png')

plt.clf()