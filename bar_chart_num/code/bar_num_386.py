
import matplotlib.pyplot as plt
import numpy as np

# Define data
State = ["Texas", "California", "New York", "Florida"]
Charity_Organizations = [50, 60, 70, 80]
Donations = [750, 850, 800, 950]

# Set figure size
fig = plt.figure(figsize=(8, 6))

# Set up a subplot with 1 row and 1 column
ax = fig.add_subplot(1, 1, 1)

# Set the width of each bar
width = 0.4

# Create a bar chart with Charity Organizations in the window
org_bar = ax.bar(State, Charity_Organizations, width, color="green")

# Create a bar chart with Donations in the window
don_bar = ax.bar(State, Donations, width, color="blue", bottom=Charity_Organizations)

# Set the title of the figure
plt.title("Number of charity organizations and donations in four states in 2021")

# Label the x-axis
ax.set_xlabel("State")

# Label the y-axis
ax.set_ylabel("Number")

# Set grid
ax.grid(True, axis='y', ls='--', lw=0.5, alpha=0.5)

# Set the legend
ax.legend((org_bar, don_bar), ("Charity Organizations", "Donations (million)"))

# Set the x-axis ticks
ax.set_xticks(np.arange(len(State)) + width/2)
ax.set_xticklabels(State)

# Set annotation
for org_bar, don_bar in zip(org_bar, don_bar):
    ax.annotate("{0}\n{1}".format(org_bar.get_height(), don_bar.get_height()), xy=(org_bar.get_x() + org_bar.get_width() / 2, org_bar.get_height() + don_bar.get_height() / 2), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

# Adjust figure size
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/615.png')

# Clear current image state
plt.clf()