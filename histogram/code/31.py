import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ['Revenue Range (Million $)', 'Number of Organizations']
line_labels = [
    '0-10', '10-50', '50-100', '100-200', '200-300',
    '300-400', '400-500', '500-600', '600-700', '700-800'
]
data = [150, 80, 45, 30, 20, 10, 5, 2, 2, 1]

# Initialize the figure
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create horizontal bar plot using Seaborn
sns.barplot(x=data, y=line_labels, palette="viridis", ax=ax)

# Add gridlines and other visual enhancements
ax.set_title('Revenue Distribution across Charity and Nonprofit Organizations', fontsize=16)
ax.set_xlabel(data_labels[1], fontsize=14)
ax.set_ylabel(data_labels[0], fontsize=14)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Set labels to display on multiple lines if they are too long
ax.set_yticklabels([label if len(label) <= 10 else '\n'.join(label.split('-')) for label in line_labels], 
                   fontsize=12, wrap=True)

# Adjust layout to prevent content from overlapping
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/31.png')

# Clear the current figure's state to avoid interference with future plots
plt.clf()
