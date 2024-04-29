
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA", "UK", "Germany", "France"]
Crops = [140, 50, 80, 90]
Livestock = [25, 10, 15, 20]

x = np.arange(len(Country))
width = 0.4

fig, ax = plt.subplots(figsize=(10,6))
rects1 = ax.bar(x - width/2, Crops, width, label='Crops')
rects2 = ax.bar(x + width/2, Livestock, width, label='Livestock')

ax.set_title('Crop and Livestock Production in Four Countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()

def autolabel(rects, loc):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, loc),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1, -10)
autolabel(rects2, 10)

plt.tight_layout()
plt.savefig('Bar Chart/png/584.png')
plt.clf()