
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(6, 6))

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Dairy Products', 'Fruits and Vegetables', 'Bakery items', 'Meat and Fish', 'Beverages', 'Snacks']
sizes = [20, 20, 15, 15, 15, 15]

explode = [0, 0, 0, 0, 0, 0]  # only "explode" the 2nd slice (i.e. 'Hogs')

ax = fig.add_subplot(111)
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Distribution of Food categories in the Global Market, 2023', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.xticks(rotation=90)

# Save Figure
plt.savefig('pie chart/png/17.png')

# Clear the current image state
plt.clf()