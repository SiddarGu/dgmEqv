
import matplotlib.pyplot as plt
import numpy as np
country = ['USA', 'UK', 'Germany', 'France']
Policies = [20, 25, 18, 22]
Legislations = [30, 35, 32, 34]

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)
ax.bar(country, Policies, width=0.3, label='Policies')
ax.bar(np.arange(len(country)) + 0.3, Legislations, width=0.3, label='Legislations')
ax.set_xticks(np.arange(len(country))+0.3/2)
ax.set_xticklabels(country, rotation=90, ha='center', va='top', wrap=True)
ax.set_title('Number of Policies and Legislations in four countries in 2021')
ax.legend(loc='best')
ax.grid(linestyle='--')
plt.tight_layout()
plt.savefig('bar chart/png/210.png')
plt.clf()