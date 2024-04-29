
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
y1 = [500, 700, 400, 600]
y2 = [2, 3, 1, 2.5]

# Create figure before plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Plot the data with the type of bar chart
ax.bar(x-0.2, y1, width=0.4, label='Users')
ax.bar(x+0.2, y2, width=0.4, label='Average Time Spent')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Do not set special fonts such as sans-serif and Arial etc.
plt.rcParams['font.family'] = 'SimHei'

# Use xticks to prevent interpolation
plt.xticks(x, ('Twitter', 'Instagram', 'LinkedIn', 'TikTok'))

# The positioning of the legend should not interfere with the chart and title
ax.legend(loc='upper left')

# Drawing techniques such as background grids can be used
ax.grid(True, linestyle='--', color='grey', alpha=0.3)

# The title of the figure should be  Social media usage in four platforms in 2021
ax.set_title('Social media usage in four platforms in 2021')

# Save the image
plt.savefig('bar chart/png/416.png', bbox_inches='tight')

# Clear the current image state at the end of the code
plt.clf()