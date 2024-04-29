
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.plot([2000,2001,2002,2003,2004,2005], [1000,1100,1200,1400,1300,1500], label='Grain Yields')
ax.plot([2000,2001,2002,2003,2004,2005], [2.5,2.7,3.0,3.4,3.2,2.9], label='Crop Prices')
ax.set_title('Yield and Price of Grains in the US from 2000 to 2005')
ax.set_xlabel('Year')
ax.set_ylabel('Grain Yields/Crop Prices')
ax.legend(loc='upper left')
plt.xticks([2000,2001,2002,2003,2004,2005])
plt.tight_layout()
plt.savefig('line chart/png/71.png')
plt.clf()