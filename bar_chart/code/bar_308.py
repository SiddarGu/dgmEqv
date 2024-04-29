
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10, 8))
# Add subplot
ax = plt.subplot(1, 1, 1)

# Set the data
Mode = ['Air', 'Sea', 'Road']
Average_Cost = [200, 100, 50]
Average_Time = [90, 60, 30]

# Plot bar chart
ax.bar(Mode, Average_Cost, label="Average Cost($)", color='#78C850', width=0.4)
ax.bar(Mode, Average_Time, bottom=Average_Cost, label="Average Time(min)", color='#F08030', width=0.4)

# Set title
plt.title('Average Cost and Time for Air, Sea and Road Transportation in 2021')
# Set x/y axis label
ax.set_xlabel('Mode')
ax.set_ylabel('Average Cost($) and Average Time(min)')
# Rotate x ticks
ax.set_xticklabels(Mode, rotation=0)
# Set y ticks
ax.set_yticks(np.arange(0, 250, 50))
# Set legend
ax.legend(loc=2, fontsize='small')
# Set grids
ax.grid(True, axis='y', linestyle='--', color='#A9A9A9', linewidth=1)
# Tight layout
plt.tight_layout()
# Save figure
plt.savefig('bar chart/png/92.png')
# Clear the current image state
plt.clf()