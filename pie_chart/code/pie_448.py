
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure
fig = plt.figure(figsize=(10, 8))

# Data to plot
labels = 'Education', 'Health', 'Humanitarian Aid', 'Environment', 'Community Development', 'Religion', 'Animal Welfare'
sizes = [25, 20, 20, 15, 10, 5, 5]

# Plot
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Legend
blue_patch = mpatches.Patch(color='blue', label='Education')
green_patch = mpatches.Patch(color='green', label='Health')
orange_patch = mpatches.Patch(color='orange', label='Humanitarian Aid')
yellow_patch = mpatches.Patch(color='yellow', label='Environment')
magenta_patch = mpatches.Patch(color='magenta', label='Community Development')
cyan_patch = mpatches.Patch(color='cyan', label='Religion')
red_patch = mpatches.Patch(color='red', label='Animal Welfare')
plt.legend(handles=[blue_patch, green_patch, orange_patch, yellow_patch, magenta_patch, cyan_patch, red_patch], bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Title
plt.title('Distribution of Donations to Charitable Causes in the US, 2023', fontsize=14)

# Figure Resizing
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/201.png', dpi=300)

# Clear figure
plt.clf()