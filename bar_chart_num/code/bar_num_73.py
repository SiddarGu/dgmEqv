

import matplotlib.pyplot as plt
import numpy as np
 
data = [['Investment', 5000], ['Credit', 4000], ['Savings', 7000], ['Grants', 2000]]
 
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
 
types = [i[0] for i in data]
amounts = [i[1] for i in data]
 
ax.bar(types, amounts, color = '#008080')
 
for i, v in enumerate(amounts):
    ax.text(i, v+200, str(v), color='#008080', fontsize=15, rotation=45, ha='center', va='bottom')
 
plt.title('Amount of Investment, Credit, Savings and Grants in 2021')
plt.ylabel('Amount (million)')
plt.xlabel('Type')
plt.xticks(np.arange(len(types)), types)
plt.tight_layout()
plt.savefig('Bar Chart/png/571.png')
plt.clf()