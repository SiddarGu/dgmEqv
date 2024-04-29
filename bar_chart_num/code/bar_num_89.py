
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(4)
y1 = [18,22,28,32]
y2 = [82,78,72,68]

ax.bar(x, y1, color='#2196f3', width=0.4, label='Renewable Energy Sources Percentage')
ax.bar(x, y2, bottom=y1, color='#ff9800', width=0.4, label='Fossil Fuel Percentage')

ax.set_xticks(x)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'])

plt.title('Percentage of Renewable Energy Sources and Fossil Fuel in four countries in 2021')
plt.legend()

for i in range(4):
    plt.annotate(str(y1[i])+'%', (x[i] - 0.2, y1[i]/2), fontsize=10, ha='center')
    plt.annotate(str(y2[i])+'%', (x[i] + 0.2, y1[i] + y2[i]/2), fontsize=10, ha='center')

plt.tight_layout()

plt.savefig('Bar Chart/png/91.png')
plt.clf()