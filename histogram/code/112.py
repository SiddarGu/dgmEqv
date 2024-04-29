import matplotlib.pyplot as plt
import seaborn as sns
import os

# Given data
data_labels = ["Number of Graduates (Thousands)"]
line_labels = [
    "Social Sciences",
    "Humanities",
    "Education",
    "Law",
    "Economics",
    "Psychology",
    "Visual and Performing Arts",
    "History",
    "Philosophy",
]
data = [75, 45, 60, 25, 55, 85, 40, 30, 20]

# Set the style
sns.set(style="whitegrid")

# Create the histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create a barplot
sns.barplot(x=line_labels, y=data, palette="viridis", ax=ax)

# Set the title and labels
ax.set_title('Number of Graduates by Major in Social Sciences and Humanities', fontsize=16)
ax.set_ylabel(data_labels[0], fontsize=12)
ax.set_xlabel('Majors', fontsize=12)

# Rotate the x-axis labels to prevent overlapping and ensure clarity
plt.xticks(rotation=45, ha='right', wrap=True)

# Set the figure layout to be tight 
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/112.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='png', dpi=300)

# Clear the figure to prevent overlap with any future plots
plt.clf()
