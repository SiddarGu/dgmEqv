
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111)

data =[[20,10],[15,8],[17,7],[18,9]]
countries = ['USA','UK','Germany','France']

x_pos = np.arange(len(countries))
output = [i[0] for i in data]
investment = [i[1] for i in data]

bars = ax.bar(x_pos, output, width=0.4, alpha=0.8, label='Manufacturing Output', color='blue')
bars2 = ax.bar(x_pos+0.4, investment, width=0.4, alpha=0.8, label='Investment', color='green')

ax.set_xticks(x_pos)
ax.set_xticklabels(countries, fontsize=20)
ax.set_ylabel('billion')
plt.title('Manufacturing Output and Investment in four countries in 2021', fontsize=20)
ax.legend(loc=2, fontsize=20)

plt.tight_layout()
plt.savefig('bar chart/png/427.png')
plt.clf()