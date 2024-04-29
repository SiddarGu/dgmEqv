
import matplotlib.pyplot as plt
import numpy as np

# Create figure 
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot()

# Set data
Country = np.arange(4)
Wind_Energy = [200,120,150,110]
Solar_Energy = [210,130,160,120]
Hydro_Energy = [220,140,170,130]

# Plot bar chart
ax.bar(Country, Wind_Energy, width=0.2, label='Wind Energy')
ax.bar(Country+0.2, Solar_Energy, width=0.2, label='Solar Energy')
ax.bar(Country+0.4, Hydro_Energy, width=0.2, label='Hydro Energy')

# Set x axis label
ax.set_xticks(Country+0.3)
ax.set_xticklabels(['USA','UK','Germany','France'])

# Set title
ax.set_title('Renewable energy sources in four countries in 2021')

# Add legend
ax.legend()

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('bar chart/png/60.png')

# Clear the current image state
plt.cla()