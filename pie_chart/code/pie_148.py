

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure
fig = plt.figure(figsize=(7,7))

# Data
labels = ['Air', 'Rail', 'Road', 'Sea']
sizes = [25, 20, 35, 20]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        startangle=90, shadow=True, 
        explode=(0, 0.1, 0, 0),
        textprops={'fontsize': 12, 'wrap': True, 'rotation': 0})

# Legend
blue_patch = mpatches.Patch(color='blue', label='Air')
orange_patch = mpatches.Patch(color='orange', label='Rail')
green_patch = mpatches.Patch(color='green', label='Road')
purple_patch = mpatches.Patch(color='purple', label='Sea')
plt.legend(handles=[blue_patch, orange_patch, green_patch, purple_patch],
bbox_to_anchor=(1.05, 0.5), loc='center left', borderaxespad=0)

# Title
plt.title('Modes of Transportation Used in the Global Logistics Industry in 2023', fontsize=15)

# xticks
plt.xticks(())

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/256.png', dpi=256)

# Clear figure
plt.clf()