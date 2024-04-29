
import matplotlib.pyplot as plt
import numpy as np

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
household = [100, 120, 90, 110, 80, 140, 120, 100, 90, 110, 80, 90]
industry = [900, 800, 700, 600, 500, 400, 300, 200, 100, 80, 60, 40]

fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# Add grids
plt.grid(linestyle='--', linewidth=0.5, alpha=0.5)

# Add labels
ax.set_title('Monthly electricity usage comparison between households and industries in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Electricity Usage (kW)')

# Set x ticks
plt.xticks(np.arange(len(month)), month, rotation='vertical')

# Set data
ax.plot(month, household, marker='o', label='Household')
ax.plot(month, industry, marker='o', label='Industry')

# Add legend
ax.legend(loc=2, bbox_to_anchor=(1, 1))

# Annotate data points
for i,j in zip(month, household):
    ax.annotate(str(j), xy=(i, j), xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', rotation=45)
for i,j in zip(month, industry):
    ax.annotate(str(j), xy=(i, j), xytext=(0, 5), textcoords="offset points", ha='center', va='bottom', rotation=45)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/455.png')

# Clear the current image state
plt.clf()