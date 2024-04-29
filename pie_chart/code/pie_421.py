
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()

# Set labels
labels = ['Democrats', 'Republicans', 'Independents', 'Other']

# Set data
data = [35,35,20,10]

# Plot pie chart
ax.pie(data, labels=labels, autopct='%1.1f%%', textprops={'wrap': True, 'rotation': 0})

# Set title
ax.set_title('Political Party Distribution in the USA, 2023', fontsize=20)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/168.png')

# Clear the current image state
plt.clf()