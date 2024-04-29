
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
GDP = [22, 2.5, 4.7, 2.9]
Growth = [3.4, 1.3, 2.1, 1.5]

x = np.arange(len(Country))
width = 0.35

fig, ax = plt.subplots(figsize=(10,7))
p1 = ax.bar(x, GDP, width, label='GDP')
p2 = ax.bar(x, Growth, width, bottom=GDP, label='Economic Growth')

ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()
ax.set_title('GDP and Economic Growth of four countries in 2021')

for i in range(len(GDP)):
    ax.text(x[i]-0.1, GDP[i]/2, str(GDP[i]), color='white', fontweight='bold', fontsize=14)
    ax.text(x[i]-0.1, GDP[i]+Growth[i]/2, str(Growth[i]), color='white', fontweight='bold', fontsize=14)

plt.tight_layout()
plt.savefig('Bar Chart/png/416.png')
plt.clf()