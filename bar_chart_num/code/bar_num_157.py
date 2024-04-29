

import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Define Data
states = ['California', 'New York', 'Texas', 'Florida']
scientists = [500, 400, 700, 450]
engineers = [800, 700, 1000, 750]

# Plot Bar Chart
x = np.arange(len(states))
width = 0.35

ax.bar(x - width/2, scientists, width=width, label='Scientists', color='b')
ax.bar(x + width/2, engineers, width=width, label='Engineers', color='r')

# Set Title
ax.set_title('Number of scientists and engineers in four states in 2021')

# Set X-axis
ax.set_xticks(x)
ax.set_xticklabels(states)

# Add Grid
ax.grid(linestyle='dotted')

# Add legend
ax.legend(loc='upper right')

# Add labels
for i, scientists in enumerate(scientists):
    ax.annotate(scientists, (x[i] - 0.15, scientists + 25))
for i, engineers in enumerate(engineers):
    ax.annotate(engineers, (x[i] + 0.15, engineers + 25))

# Resize image
fig.tight_layout()

# Save and clear current image state
plt.savefig('Bar Chart/png/53.png')
plt.clf()