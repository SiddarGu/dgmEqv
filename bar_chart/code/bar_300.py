
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6))
destination = ['USA', 'UK', 'Germany', 'France']
tourists = [20,25,15,30]
income = [200,250,150,300]

x = np.arange(len(destination))
width = 0.35

ax = plt.subplot()
ax.bar(x - width/2, tourists, width, label='Tourists (million)')
ax.bar(x + width/2, income, width, label='Income (million)')

ax.set_ylabel('Number')
ax.set_title('Number of tourists and income generated in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(destination, rotation=45)
ax.legend(loc=2, bbox_to_anchor=(1.0, 1.0))
plt.tight_layout()
plt.savefig('bar chart/png/449.png')
plt.clf()