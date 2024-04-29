

import matplotlib.pyplot as plt

# get data
data=[[0,3,4],[1,4,5],[2,6,7],[3,7,8],[4,8,9],[5,10,11],[6,11,12],[7,12,13]]
hours=[d[0] for d in data]
solar=[d[1] for d in data]
wind=[d[2] for d in data]

# setup figure
plt.figure(figsize=(10,6))
ax=plt.subplot()

# plot data
plt.plot(hours, solar, label="Solar Energy Production(MW)", color='#FF7F00')
plt.plot(hours, wind, label="Wind Energy Production(MW)", color='#377EB8')

# configure
plt.legend(loc='upper right', fontsize=12, frameon=False)
plt.xticks(hours, rotation=45)
plt.title("Renewable Energy Production in North America on April 1, 2021", fontsize=14)
plt.grid(True, linestyle='dashed')
ax.set_axisbelow(True)

# save
plt.tight_layout()
plt.savefig('line chart/png/506.png')
plt.clf()