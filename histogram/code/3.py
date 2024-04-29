import matplotlib.pyplot as plt
import seaborn as sns
import os

# Given data
data = [
    [210],
    [320],
    [305],
    [275],
    [260],
    [240],
    [190]
]
data_labels = ['Number of Patents']
line_labels = [
    'Biotechnology',
    'Computer Science',
    'Electrical Engineering',
    'Mechanical Engineering',
    'Chemical Engineering',
    'Environmental Science',
    'Aerospace Engineering'
]

# Set up the matplotlib figure
plt.figure(figsize=(14, 9))
ax = plt.subplot()

# Create a seaborn histogram
sns.barplot(x=line_labels, y=[x[0] for x in data], palette="viridis")

# Improve the plot aesthetics
ax.set_title('Number of Patents Issued Across Fields of Science and Engineering', fontsize=16)
ax.set_xlabel('Field of Study', fontsize=14)
ax.set_ylabel('Number of Patents', fontsize=14)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=12)
sns.despine()  # Remove the top and right spines from plot
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add a grid

# Automatically adjust subplot specs so that the subplot(s) fits in to the figure area.
plt.tight_layout()

# Make sure the saving directory exists, if not, create it
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png"
os.makedirs(save_dir, exist_ok=True)

# Save the figure
plt.savefig(f"{save_dir}/3.png", bbox_inches="tight", dpi=300)

# Clear the current figure state afterwards
plt.clf()
