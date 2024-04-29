

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
ax = plt.subplot()
ax.bar('North', 400, bottom=0, label='North', width=0.6)
ax.bar('South', 300, bottom=400, label='South', width=0.6)
ax.bar('East', 350, bottom=700, label='East', width=0.6)
ax.bar('West', 250, bottom=1050, label='West', width=0.6)
plt.title('Number of Houses Sold and Average Price in Four Areas of the Country in 2021')
ax.set_xticks(['North', 'South', 'East', 'West'])
ax.set_xlabel('Area')
ax.set_ylabel('Number of House Sold')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/131.png')
plt.clf()