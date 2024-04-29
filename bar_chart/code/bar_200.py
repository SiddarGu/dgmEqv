
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
ax = plt.subplot(111)
ax.set_title('Average House Price and Number of Houses Sold in four Regions in 2021')
ax.set_xlabel('Region')
ax.set_ylabel('Price and Number')

region = ['North', 'South', 'East', 'West']
price = [250, 200, 180, 220]
number = [100, 90, 80, 95]
bar_width = 0.35

ax.bar(region, price, width=bar_width, label='Price')
ax.bar(region, number, bottom=price, width=bar_width, label='Number')

ax.legend()
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('bar chart/png/447.png')
plt.clf()