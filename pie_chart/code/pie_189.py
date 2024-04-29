
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure and set size
fig = plt.figure(figsize=(8, 8))

# Set labels 
labels = ['Single-family Houses', 'Multi-family Houses', 'Townhouses', 'Condominiums', 'Other']

# Set percentages
sizes = [42, 26, 18, 8, 6]

# Set colors
colors = ['#FF9999', '#FFE5CC', '#FFFF99', '#CCFFCC', '#99CCFF']

# Plot pie chart
plt.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%', textprops={'fontsize': 14})

# Create legend
legend_elements = [mpatches.Patch(facecolor=color, label=label) for label, color in zip(labels, colors)]
plt.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1.1, 0.5))

# Disable interpolation
plt.xticks([])

# Set title
plt.title('Distribution of Home Types in the US Housing Market in 2023', fontsize=16)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/47.png', dpi=200)

# Clear the current image state
plt.clf()