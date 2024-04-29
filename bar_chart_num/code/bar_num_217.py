
import matplotlib.pyplot as plt
import numpy as np

x = ['North America', 'Europe', 'Asia', 'Africa']
y1 = [20, 25, 22, 23] 
y2 = [200, 230, 250, 220]

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(x, y1, color='#4E79A7', width=0.4, align='center', label='Tax Rate(%)')
ax.bar(x, y2, color='#F28E2C', width=0.4, bottom=y1, align='center', label='Government Spending(billion)')

plt.title('Tax rate and government spending in four regions in 2021', fontsize=14)
plt.xticks(x, rotation=45)
ax.legend(loc='upper left')

for a, b in zip(x, y1):
    ax.annotate('{:.2f}%'.format(b), xy=(a, b+5))
for a, b in zip(x, y2):
    ax.annotate('{:.2f}b'.format(b), xy=(a, b+5))

plt.tight_layout()
plt.savefig('Bar Chart/png/170.png', dpi=200)

plt.clf()