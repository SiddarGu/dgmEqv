import matplotlib.pyplot as plt
import os

# Given data
data = [
    [75, 150, 125, 100, 200, 90, 160, 60, 40]
]
data_labels = [
    "HR", "Sales", "IT", "R&D", "Operations",
    "Marketing", "Customer Service", "Finance", "Legal"
]
line_labels = ["Number of Employees"]

# Creating a histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Plotting the data
for index in range(len(data)):
    ax.bar(data_labels, data[index], label=line_labels[index])

# Adding grid, labels, title, and legend
ax.set_xlabel('Departments', fontsize=12)
ax.set_ylabel('Number of Employees', fontsize=12)
ax.set_title('Employee Distribution Across Departments in a Corporate Organization', fontsize=14)
ax.legend()
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.yticks(fontsize=10)

# Adding grid for better readability
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Resizing layout
plt.tight_layout()

# Save the figure
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png'
os.makedirs(save_dir, exist_ok=True)
plt.savefig(f"{save_dir}/128.png", format='png')

# Clearing the current figure state
plt.clf()
