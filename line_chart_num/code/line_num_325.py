
import matplotlib.pyplot as plt
import numpy as np 

# Create figure before plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Set x,y coordinates
x = np.array([2020, 2021, 2022, 2023, 2024])
y1 = np.array([700, 800, 900, 1000, 1100])
y2 = np.array([1200, 1100, 1300, 1500, 1600])

# Plot the data
ax.plot(x, y1, color='blue', linewidth=2.5, linestyle='solid', label='Online Sales')
ax.plot(x, y2, color='red', linewidth=2.5, linestyle='dashed', label='Store Sales')

# Set the xticks to prevent interpolation
plt.xticks(x)

# Add a title, legend and grid
ax.set_title('Comparison of Online and Store Sales in the Retail Industry')
ax.legend(loc='upper center')
ax.grid(linestyle='--', linewidth=1)

# Label the value of each data point directly on the figure
for a, b in zip(x, y1):
    ax.text(a - 0.2, b + 20, b, fontsize=10)
for a, b in zip(x, y2):
    ax.text(a + 0.1, b - 20, b, fontsize=10, rotation=90, wrap=True)
    
# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/435.png')

# Clear the figure
plt.clf()