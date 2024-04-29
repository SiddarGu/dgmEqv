
import matplotlib.pyplot as plt

# Define labels, positions, bar lengths and colors
labels = ['North America', 'South America', 'Europe', 'Asia']
x_pos = [i for i, _ in enumerate(labels)]
beds = [3.5, 2.1, 3.4, 2.2]
doctors = [2.6, 2.2, 2.4, 1.8]
colors = ['#191970', '#00008B', '#483D8B', '#4169E1']

# Create figure and set the size
fig, ax = plt.subplots(figsize=(6,4))

# Plot the bars and annotate the values
ax.bar(x_pos, beds, width=0.6, label='Hospital beds (per 1000 people)', color=colors)
ax.bar([p + 0.6 for p in x_pos], doctors, width=0.6, label='Doctors (per 1000 people)', color=colors)

for i, v in enumerate(beds):
    ax.text(i-0.2, v/2, str(v), color='white', fontsize=12, fontweight='bold')
for i, v in enumerate(doctors):
    ax.text(i+0.4, v/2, str(v), color='white', fontsize=12, fontweight='bold')

# Title and labels
ax.set_title('Healthcare availability in four regions in 2021')
ax.set_xticks([p + 0.3 for p in x_pos])
ax.set_xticklabels(labels, rotation=45, fontsize=10)
ax.set_ylabel('Availability')
ax.legend(loc='upper left')

# Adjust the margins
plt.subplots_adjust(bottom=0.2, top=0.9)

# Enable tight layout
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/190.png')

# Clear the current image state
plt.clf()