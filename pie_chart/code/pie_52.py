
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 8))

# Define labels and data
labels = ['Domestic', 'Adventure', 'Business', 'Cultural', 'Beach']
data = [45, 25, 15, 10, 5]

# Create pie chart
ax = fig.add_subplot()
ax.pie(data, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 14})

# Set title
plt.title('Types of Tourism in the USA, 2023')

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/473.png')

# Clear current image state
plt.clf()