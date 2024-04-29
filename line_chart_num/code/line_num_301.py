
import matplotlib.pyplot as plt
import numpy as np

data = [[1000, 800, 900, 1200], [900, 1200, 1100, 1500], [700, 1100, 1300, 1400], [1200, 1500, 1400, 1000]]
months = ['January', 'February', 'March', 'April']
Customer = ['Customer A','Customer B','Customer C','Customer D']

fig, ax = plt.subplots(figsize=(8, 6))

for i in range(len(data[0])):
    ax.plot(months, [row[i] for row in data], label=Customer[i])

for i in range(len(data)):
    for j in range(len(data[i])):
        ax.annotate(str(data[i][j]), xy=(months[i], data[i][j]), xytext=(months[i], data[i][j]+100), fontsize=9, rotation=90)

ax.set_xlabel('Months')
ax.set_ylabel('Customer')
ax.set_title('Number of Customers Shopping Online in Four Retail Stores in 2021')
ax.legend()

ax.xaxis.set_ticks(months)

plt.tight_layout()
plt.savefig('line chart/png/342.png')

plt.clf()