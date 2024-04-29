import matplotlib.pyplot as plt
import os

# Data transformation
data_labels = ['Revenue Growth (%)']
line_labels = ['Q1', 'Q2', 'Q3', 'Q4']
data = [5.2, 7.1, 5.8, 6.3]

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(8, 6))

# Plotting
bars = ax.bar(line_labels, data, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# Add background grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Set the title
ax.set_title('Quarterly Revenue Growth in the Financial Sector', fontsize=15)

# Set the labels
ax.set_xlabel('Quarter')
ax.set_ylabel('Revenue Growth (%)')

# Label rotation for x-axis if necessary
plt.xticks(rotation=45)

# Automatically adjust layout to fit content
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/122.png'
# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.close(fig)
