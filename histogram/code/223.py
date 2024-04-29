import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ['Monthly Sales (Billion $)', 'Number of Retailers']
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
data = [1.5, 1.2, 1.7, 2.0, 2.4, 2.3, 2.5, 2.2, 1.9, 2.6, 2.8, 3.0]

# Setting up the figure and axis
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plotting the data
sns.barplot(x=line_labels, y=data, ax=ax, palette='viridis')

# Set title
plt.title('Monthly Retail E-commerce Sales Distribution', fontsize=16)

# Enhance x-label appearance
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=10, wrap=True)
ax.set_ylabel('Number of Retailers')
# Add grid
ax.grid(axis='y')

# Automatically adjust layout to prevent clipping labels and title
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/223.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure
plt.clf()
