
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure and a subplot
fig, ax = plt.subplots(figsize=(8, 8))

 # Labels of each wedge
labels = ['Computer Science','Mathematics','Engineering','Physics','Chemistry']

# Percentage of each wedge
sizes = [25,20,35,15,5]

# Colors for each wedge
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#a3acff']

# Draw pie chart
wedges, texts, autotexts = ax.pie(sizes, labels=labels, 
                        autopct='%1.1f%%', 
                        colors=colors,
                        shadow=True, 
                        startangle=90,
                        radius=1.2,
                        textprops={'fontsize': 12, 'color':'black'},
                        wedgeprops={'linewidth': 2, 'edgecolor':'white'})

# Make sure text is inside the plot
plt.setp(autotexts, size=10, weight="bold")

# Legend
patches = [mpatches.Patch(color=colors[i], label=labels[i]) for i in range(len(labels))]
plt.legend(handles=patches, bbox_to_anchor=(1.2, 0.5), fontsize=10)

# Title
plt.title('Distribution of Science and Engineering Fields in 2023', fontsize=15, y=1.08)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/530.png')

# Clear the current image state
plt.clf()