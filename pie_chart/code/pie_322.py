
import matplotlib.pyplot as plt
import numpy as np

labels = ['Defense', 'Education', 'Health Care', 'Social Security', 'Infrastructure']
sizes = [25, 20, 30, 15, 10]

# Create figure before plotting
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)

# Plot the data with the type of pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 14, 'wrap': True, 'rotation': 0})

# Set title
plt.title("Breakdown of US Federal Government Spending in 2023", fontsize=14)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig("pie chart/png/435.png")

# Clear the current image state
plt.clf()