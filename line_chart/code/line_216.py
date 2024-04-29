
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(figsize = (12, 6))
ax = plt.subplot(111)
ax.set_title('Crop Production in Different Regions in 2021')

x = [1,2,3,4]
regions = ['North America','South America','Europe','Asia']
wheat = [10000,8000,20000,30000]
rice = [15000,12000,25000,40000]
corn = [20000,18000,30000,50000]

ax.plot(x,wheat,label='Wheat Production', marker='o')
ax.plot(x,rice,label='Rice Production', marker='o')
ax.plot(x,corn,label='Corn Production', marker='o')

ax.xaxis.set_major_locator(ticker.FixedLocator(x))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(regions))
plt.xticks(rotation=45, ha='right')
plt.legend(loc=1, bbox_to_anchor=(1.2, 1.05))

plt.tight_layout()
plt.savefig('line chart/png/31.png')
plt.clf()