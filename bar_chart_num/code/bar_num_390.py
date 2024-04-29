
import matplotlib.pyplot as plt
import numpy as np

# Define the data
data = [['North America', 50000, 25000, 2500],
        ['Europe', 60000, 20000, 3000],
        ['Asia', 70000, 30000, 4000],
        ['South America', 40000, 15000, 3500]]
region, roads, railways, airports = zip(*data)

# Plot the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Set the x-axis ticks
ax.set_xticks(np.arange(len(region)))
ax.set_xticklabels(region, fontsize=12)

# Plot the bars
ax.bar(region, roads, bottom=railways, label='Roads (km)', width=0.5)
ax.bar(region, railways, bottom=airports, label='Railways (km)', width=0.5)
ax.bar(region, airports, label='Airports', width=0.5)

# Add labels to the bars
for r, rd, rl, a in zip(region, roads, railways, airports):
    ax.annotate('{}'.format(rd), xy=(r, rd+rl+a/2), ha='center', fontsize=12)
    ax.annotate('{}'.format(rl), xy=(r, rl+a/2), ha='center', fontsize=12)
    ax.annotate('{}'.format(a), xy=(r, a/2), ha='center', fontsize=12)

# Configure the legend
ax.legend(loc='upper left', fontsize=12)

# Set the title and labels
ax.set_title('Transportation infrastructure in four regions in 2021', fontsize=16)

# Tight layout
fig.tight_layout()

# Save the figure
fig.savefig('Bar Chart/png/297.png')

# Clear the figure
plt.clf()