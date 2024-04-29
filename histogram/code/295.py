import matplotlib.pyplot as plt
import os

# Given data parsed into required variables
data_labels = ['Freshman', 'Sophomore', 'Junior', 'Senior', 'Graduate Students', 'PhD Candidates']
data = [2.9, 3.1, 3.2, 3.4, 3.7, 3.8]

# Create a figure and a subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting the histogram
ax.bar(data_labels, data, color='skyblue', edgecolor='gray')

# Title and labels
ax.set_title('Average Grade Point Average (GPA) by Academic Level', fontsize=15, pad=20)
ax.set_xlabel('Academic Level', fontsize=12)
ax.set_ylabel('Average GPA', fontsize=12)

# Rotate the labels on the x-axis to prevent overlap
ax.set_xticklabels(data_labels, rotation=45, ha="right")

# Adding grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ensure everything fits without overlapping
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/645.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the figure to prevent re-use
plt.clf()
