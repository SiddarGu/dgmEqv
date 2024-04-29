
import matplotlib.pyplot as plt
import numpy as np

# data
modes = ['Road', 'Rail', 'Air', 'Sea']
percentage = [45, 30, 15, 10]

# Create figure
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()

# Plot
ax.pie(percentage, labels=modes, autopct='%.2f%%',
       textprops={'fontsize': 14, 'wrap': True, 'rotation': 90})
ax.set_title('Distribution of Cargo Transportation Modes in the USA, 2023')

# Resize
plt.tight_layout()

# Save
plt.savefig('pie chart/png/355.png')

# Clear
plt.cla()