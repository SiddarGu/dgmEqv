

import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(6,6))

# Data to plot
labels = ['Google','YouTube','Facebook','Instagram','Twitter','Reddit','Others']
sizes = [25,20,20,15,10,5,5]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', wedgeprops={'linewidth': 1.2}, shadow=True, textprops={'fontsize': 11})

# Legend
plt.legend(labels, loc="upper right", bbox_to_anchor=(1.3,1))

# Title
plt.title('Distribution of Popular Social Media Platforms in the USA, 2023')

# Tight layout
plt.tight_layout()

# Save png
plt.savefig('pie chart/png/503.png')

# Clear the current image state
plt.clf()