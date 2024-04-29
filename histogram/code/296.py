import matplotlib.pyplot as plt
import seaborn as sns

# Data Preparation
data_labels = ['Legal Cases (Thousands)', 'Number of Cases Resolved']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data = [45, 50, 55, 48, 40, 30, 20, 15, 10, 5]

# Create figure and axis
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Seaborn style
sns.set_style("whitegrid")

# Generate the histogram
sns.barplot(x=line_labels, y=data, palette='viridis')

# Set histogram title and labels
plt.title('Annual Case Resolution Distribution in the Legal System')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

# Handling long labels
ax.set_xticklabels(line_labels, rotation=45, ha='right')

# Customize legend
plt.legend(title='Case Resolution', loc='upper right')

# Automatically adjust subplot params for better layout
plt.tight_layout()

# Save figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/646.png'
plt.savefig(save_path, format='png')

# Clear plot
plt.clf()
