
import numpy as np
import matplotlib.pyplot as plt

country = ['USA','UK','Germany','France']
g_spend = np.array([4000,3500,2500,3000])
tax_rev = np.array([5000,4500,3000,4000])

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
width = 0.35
ax.bar(country, g_spend, width, label='Government Spending')
ax.bar(country, tax_rev, width, bottom=g_spend, label="Tax Revenue")

plt.xticks(country, fontsize=15, rotation=45)
plt.title('Government Spending versus Tax Revenue in four countries in 2021', fontsize=18)
plt.legend(loc='best', fontsize=15)

for i in range(len(country)):
    ax.annotate(f'{g_spend[i]}', xy=(i - width/2, g_spend[i]/2), fontsize=15)
    ax.annotate(f'{tax_rev[i]}', xy=(i + width/2, tax_rev[i] + g_spend[i]/2), fontsize=15)
    
plt.tight_layout()
plt.savefig('Bar Chart/png/449.png')

plt.cla()