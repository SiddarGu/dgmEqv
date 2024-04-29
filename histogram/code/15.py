import matplotlib.pyplot as plt
import seaborn as sns
import os

# Transforming the data into the required variables
data_labels = ['Number of Employees']
line_labels = ['Very High', 'High', 'Moderate', 'Low', 'Very Low']
data = [125, 215, 165, 95, 40]

# Create a figure for plotting
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Create the histogram
sns.barplot(x=line_labels, y=data, ax=ax, palette="bright")

# Add grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add the title
ax.set_title("Employee Job Satisfaction Levels Across the Corporation", fontsize=16)

# Set the labels
ax.set_xlabel("Satisfaction Level", fontsize=14)
ax.set_ylabel("Number of Employees", fontsize=14)

# Rotate the x labels if necessary to prevent overlap
plt.xticks(rotation=45)

# Automatically adjust layout
plt.tight_layout()

# Save the histogram image to a specific path and then clear the plot
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1014.png"
dir_name = os.path.dirname(save_path)

if not os.path.exists(dir_name):
    os.makedirs(dir_name)

plt.savefig(save_path)
plt.clf()
