
import matplotlib.pyplot as plt
import numpy as np

# Define the data
region = ['North', 'South', 'East', 'West']
cases_filed = [400, 500, 425, 475]
cases_closed = [350, 450, 400, 425]

# Create the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
ax.bar(region, cases_filed, label='Cases Filed', width=0.4, align='edge', color='#ff6600')
ax.bar(region, cases_closed, label='Cases Closed', width=0.4, align='edge', bottom=cases_filed, color='#009933')

# Add labels and title
ax.set_title('Legal cases filed and closed in four regions in 2021')
ax.set_xlabel('Region')
ax.set_ylabel('Number of Cases')

# Add the legend
ax.legend(loc='upper left')

# Add grid
ax.grid(linestyle='--', linewidth=0.5, alpha=0.5)

# Add value labels
for x, y1, y2 in zip(region, cases_filed, cases_closed):
    ax.annotate(f'{y1+y2}', (x, y1+y2/2),
                ha='center', va='center', fontsize=10, color='#202020')

# Set xticks
ax.set_xticks(region)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/276.png')

# Clear the current image state
plt.clf()