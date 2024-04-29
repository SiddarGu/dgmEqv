
import matplotlib.pyplot as plt
import numpy as np

# Create data
Technologies = ['Robotics', 'Artificial Intelligence', 'Machine Learning', 'Internet Of Things', 'Big Data']
Percentage = [25, 20, 25, 15, 15]
 
# Create figure
fig = plt.figure(figsize=(8, 8))

# Create subplot
ax = fig.add_subplot(111)

# Plot data
ax.pie(Percentage, labels=Technologies, autopct='%1.1f%%', startangle=90, shadow=True, textprops={'fontsize': 18})

# Set title
ax.set_title('Distribution of Emerging Technologies in the Global Market, 2023', fontsize=20)

# Set tight layout
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/466.png')

# Clear current state
plt.clf()