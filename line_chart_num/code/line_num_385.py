
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15, 8))
ax = plt.subplot()

year = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007])
total_crop_yield = np.array([10, 12, 14, 16, 18, 20, 22])
fertilizer_consumption = np.array([20, 22, 24, 26, 28, 30, 32])

plt.plot(year, total_crop_yield, '-o', label='Total Crop Yield (tonnes)')
plt.plot(year, fertilizer_consumption, '-o', label='Fertilizer Consumption (kg/hectare)')

ax.set_xticks(year)
plt.title('Relationship between total crop yield and fertilizer consumption in farming industry from 2001 to 2007')
plt.xlabel('Year')
plt.ylabel('Quantity')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', color='gray', linewidth=1)

# label the value of each data point directly on the figure
for x, y1, y2 in zip(year, total_crop_yield, fertilizer_consumption):
    plt.annotate('({},{})'.format(x, y1), xy=(x, y1), xytext=(-6, 12), textcoords='offset points')
    plt.annotate('({},{})'.format(x, y2), xy=(x, y2), xytext=(-6, 12), textcoords='offset points')

# Automatically resize the image by tight_layout()
plt.tight_layout()

plt.savefig('line chart/png/18.png')

# Clear the current image state
plt.clf()