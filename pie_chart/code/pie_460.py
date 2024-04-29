
import matplotlib.pyplot as plt
import numpy as np

# Create figure and subplot
fig, ax = plt.subplots()
fig.set_figwidth(12)
fig.set_figheight(8)

# Labels and sizes
labels = ['Visual Arts', 'Music', 'Dance', 'Literature', 'Theatre']
sizes = [25, 20, 30, 15, 10]

# Set title
plt.title('Popular Art Forms in the USA, 2023')

# Set colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#ff99cc']

# Plot pie chart
ax.pie(sizes, labels=labels, colors=colors, 
       autopct='%1.1f%%', shadow=True, startangle=90)

# Set aspect ratio to be equal so that pie is drawn as a circle.
ax.axis('equal')

# Add grid
plt.grid(True)

# Adjust figure
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/471.png')

# Clear figure
plt.clf()