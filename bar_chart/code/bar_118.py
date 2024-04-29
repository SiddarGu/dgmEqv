
import matplotlib.pyplot as plt
import numpy as np

data = [['North America',1000,3000],['Europe',2000,4000],['Asia',3000,5000],['South America',1500,3500]]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

x = np.arange(len(data))
width = 0.3

renewable = [i[1] for i in data]
non_renewable = [i[2] for i in data]

ax.bar(x, renewable, width=width, label='Renewable Energy (million KW)', color='green')
ax.bar(x + width, non_renewable, width=width, label='Non-Renewable Energy (million KW)', color='red')

ax.set_xticks(x + width/2)
ax.set_xticklabels([i[0] for i in data], rotation=45, ha='right', wrap=True)

ax.set_title('Energy production from renewable and non-renewable sources in four regions in 2021')
ax.legend()
fig.tight_layout()
plt.savefig('bar chart/png/72.png')
plt.clf()