
import matplotlib.pyplot as plt
import numpy as np

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.bar(["USA", "UK", "Germany", "France"],
       [2000, 1750, 1800, 1900], label="Criminal Cases",
       bottom=[3000, 2500, 2700, 3100], color='b')
ax.bar(["USA", "UK", "Germany", "France"],
       [3000, 2500, 2700, 3100], label="Civil Cases",
       color='r')

# Set title and labels for axes
ax.set(xlabel="Country",
       ylabel="Number of Cases",
       title="Number of criminal and civil cases in four countries in 2021")

# Define the position of the legend
ax.legend(loc="upper left")

# Add text annotation to the plot
for p in ax.patches:
    ax.annotate(np.round(p.get_height(),decimals=2),
                (p.get_x()+p.get_width()/2., p.get_height()),
                ha='center', va='center',
                xytext=(0, 10),
                textcoords='offset points',
                rotation='vertical',
                fontsize = 14)

# Resize the figure
plt.tight_layout()

# Set ticks
plt.xticks(rotation=45)

# Save Figure
plt.savefig('Bar Chart/png/484.png')

# Clear the current image state
plt.clf()