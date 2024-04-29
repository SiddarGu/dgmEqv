
import matplotlib.pyplot as plt
import numpy as np

# Create a figure
plt.figure(figsize=(8, 4))

# Plot data
x = np.arange(5)
plt.plot(x, [2, 2.2, 2.4, 2.6, 2.8], marker='o', label='Facebook')
plt.plot(x, [1.5, 1.6, 1.7, 1.8, 2], marker='o', label='Twitter')
plt.plot(x, [1, 1.2, 1.4, 1.6, 1.8], marker='o', label='Instagram')

# Setting up the labels
plt.xticks(x, ('January', 'February', 'March', 'April', 'May'))
plt.title("Growth of Social Media Platforms Users in 2021")
plt.xlabel('Month')
plt.ylabel('Users(million)')

# Setting up the legend position and label for each point
plt.legend(loc='upper left')
for a, b in zip(x, [2, 2.2, 2.4, 2.6, 2.8]):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, [1.5, 1.6, 1.7, 1.8, 2]):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, [1, 1.2, 1.4, 1.6, 1.8]):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

# Drawing background grids
plt.grid(linestyle = '--', axis = 'y')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/425.png')

# Clear figure
plt.clf()