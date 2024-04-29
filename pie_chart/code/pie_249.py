
import matplotlib.pyplot as plt
import numpy as np

# Create Figure
plt.figure(figsize=(15,10))

# Data to plot
labels = 'Desktop', 'Mobile', 'Tablet', 'Wearables', 'Voice'
sizes = [45, 25, 15, 10, 5]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Shopping Carts Usage in E-commerce Platforms, 2023')
plt.legend(loc="best", bbox_to_anchor=(0.9, 0., 0.5, 0.5))
plt.axis('equal')
plt.xticks(rotation=90)
plt.tight_layout()

# Save
plt.savefig('pie chart/png/45.png')

# Clear
plt.clf()