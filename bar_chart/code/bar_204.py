
import matplotlib.pyplot as plt 
import numpy as np

# define data
countries = ['USA','Canada','Mexico','Brazil']
crop_production = [1400, 2000, 1200, 1600]
livestock_production = [800, 1100, 900, 1300]

# plot bar chart
fig = plt.figure(figsize=(10, 5)) 
ax = fig.add_subplot()
ax.bar(countries, crop_production, label='Crop Production', bottom=livestock_production)
ax.bar(countries, livestock_production, label='Livestock Production')

# set title
ax.set_title('Crop and Livestock Production in Four Countries in 2021')

# set xticks
ax.set_xticks(np.arange(len(countries)))
ax.set_xticklabels(countries, rotation=45, ha='right')

# set legend
ax.legend()

# adjust the layout
plt.tight_layout()

# save image
plt.savefig('bar chart/png/285.png')

# clear image state
plt.clf()