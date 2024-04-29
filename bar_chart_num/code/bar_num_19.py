
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(1, 1, 1)

Region = np.arange(4)
Median_Home_Price = [500, 400, 600, 300]
Mortgage_Interest_Rate = [2.5, 1.6, 3.2, 2.1]

ax.bar(Region, Median_Home_Price, color='#3182bd', width=0.5, label='Median Home Price')
ax.bar(Region, Mortgage_Interest_Rate, color='#de2d26', bottom=Median_Home_Price, width=0.5, label='Mortgage Interest Rate')

ax.set_xticks(Region)
ax.set_xticklabels(['North America', 'Europe', 'Asia', 'Africa'], fontsize=10, wrap=True)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=2, prop={'family':'Times New Roman', 'size':'14'})
ax.set_title('Median Home Price and mortgage interest rate in four regions in 2021', fontsize=16, fontweight='bold', family='Times New Roman')

for i, j in zip(Region, Median_Home_Price):
    ax.annotate(str(j), xy=(i-0.2, j+10), fontsize=14, family='Times New Roman')

for i, j in zip(Region, np.add(Median_Home_Price, Mortgage_Interest_Rate)):
    ax.annotate(str(j), xy=(i-0.2, j+10), fontsize=14, family='Times New Roman')

plt.tight_layout()
plt.savefig('Bar Chart/png/167.png')
plt.clf()