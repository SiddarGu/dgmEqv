
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

region = ['North','South','East','West']
price = [200000, 220000, 240000, 210000]
rent = [900, 970, 1050, 900]

x_pos = np.arange(len(region))

ax.bar(x_pos, price, width=0.3, bottom=0, color='red', label='Price')
ax.bar(x_pos+0.3, rent, width=0.3, bottom=0, color='blue', label='Rent')

for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(bottom='off', top='off', left='off', right='off')
ax.set_xticklabels(region,rotation=45, ha="right", rotation_mode="anchor", wrap=True)
ax.set_title("Average House Price and Rent in four regions in 2021")
ax.set_ylabel('Average Price & Rent')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=2)

plt.tight_layout()
plt.xticks(x_pos+0.15, region)
plt.savefig('bar chart/png/243.png')
plt.clf()