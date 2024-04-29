
import matplotlib.pyplot as plt
import numpy as np

# Generate figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# Data
labels = ['Pop','Hip-hop','Rock','Country','Jazz','Latin','Other']
sizes = [30, 20, 15, 10, 10, 10, 5]

# Pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, pctdistance=0.8, labeldistance=1.1)

# Title
ax.set_title("Music Genre Popularity in the USA, 2023", fontsize=20, pad=15)

# Make sure labels are not overwritten and stacked on top of each other
plt.tight_layout()
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=15, labelspacing=2)

# Save the figure
plt.savefig('pie chart/png/193.png', bbox_inches='tight')

# Clear the current image state
plt.clf()