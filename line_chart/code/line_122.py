
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(12, 8))

# Set axis
ax = plt.subplot()

# Set data
age_groups = ["0-17", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
percentage_people = [20, 30, 25, 15, 7, 2, 1]

# Set line color
ax.plot(age_groups, percentage_people, color='#00A0B0', linewidth=3)

# Set x-axis
ax.set_xticklabels(age_groups, rotation=45, wrap=True)

# Set y-axis
ax.set_yticks(np.arange(0, 100, 10))
ax.set_yticklabels(np.arange(0, 100, 10), fontsize=12)

# Set title
ax.set_title("Percentage of People in Different Age Groups in the United States in 2021", fontsize=20)

# Set legend
ax.legend(["Percentage of People"], loc="upper left", fontsize=15)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/166.png")

# Clear current image state
plt.clf()