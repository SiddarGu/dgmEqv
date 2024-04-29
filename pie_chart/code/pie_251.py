
import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydroelectric', 'Nuclear', 'Geothermal']
percentages = [25, 20, 30, 15, 10]

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()

# Plot data
ax.pie(percentages, labels=energy_sources,
       autopct='%1.1f%%', startangle=90,
       textprops={'fontsize': 14, 'color': 'black'},
       wedgeprops={'linewidth': 2, 'edgecolor': 'black'})

# Title
ax.set_title('Energy Sources Used in the USA in 2023')

# Display legend outside of plot
ax.legend(loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Save figure
plt.savefig('pie chart/png/523.png', bbox_inches='tight')

# Clear figure
plt.clf()