import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data input
data_labels = ["Donation Range (USD Millions)", "Number of Charities"]
line_labels = ["0-1", "1-5", "5-10", "10-20", "20-30", "30-40", "40-50", "50-100", "100-200", "200-500", "500-1000"]
data = [75, 68, 52, 45, 38, 25, 15, 12, 7, 4, 2]

# Create a DataFrame from the data
df = pd.DataFrame(data, index=line_labels, columns=data_labels[1:])

# Set up the matplotlib figure
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Create horizontal bar plot
sns.barplot(x=data, y=line_labels, palette="viridis", ax=ax)

# Customize the plot
ax.set_title('Charity Income Distribution Across Donation Ranges', fontsize=16)
ax.set_xlabel(data_labels[1], fontsize=14)
ax.set_ylabel(data_labels[0], fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Setting the rotation for the x-tick labels to ensure they fit well
for item in ax.get_xticklabels():
    item.set_rotation(45)

# Adding grid to background
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)

# Automatically adjust subplot params for the figure layout to fit into the figure area.
plt.tight_layout()

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/644.png"
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state after saving
plt.clf()
