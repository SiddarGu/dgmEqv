
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# Data
Platforms = ['Online Marketplaces', 'Online Retail Stores', 'E-commerce Apps', 'Social Commerce', 'Mobile Commerce']
Percentage = [45, 25, 15, 10, 5]

# Draw Pie Chart
ax.pie(Percentage, labels=Platforms, autopct='%.2f%%', startangle=90, textprops={'fontsize': 12}, wedgeprops={'linewidth': 2})

# Title
ax.set_title('Percentage of E-Commerce Transactions by Platform in 2023')

# Legend
ax.legend(loc='upper right', bbox_to_anchor=(1, 0.9))

# Make square figure
plt.axis('equal')

# Save figure
plt.tight_layout()
plt.savefig('pie chart/png/329.png')

# Clear the current image state
plt.clf()