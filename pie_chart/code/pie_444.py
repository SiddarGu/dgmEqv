

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 8))

# Data to plot
labels = 'Technology', 'Construction', 'Finance', 'Retail', 'Healthcare', 'Education', 'Manufacturing', 'Agriculture'
sizes = [20, 15, 25, 15, 10, 10, 10, 5]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        wedgeprops={'linewidth': 1.5, 'edgecolor': 'black'},
        textprops={'fontsize': 14, 'color': 'black'})

# Title
plt.title('Distribution of Sectors in the US Economy, 2023')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/204.png', bbox_inches='tight')
plt.clf()