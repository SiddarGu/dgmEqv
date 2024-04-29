import matplotlib.pyplot as plt
import seaborn as sns

# Data Processing
data_labels = ['Electricity Generation (GWh)', 'Number of Power Plants']
line_labels = ['0-2000', '2000-4000', '4000-6000', '6000-8000', '8000-10000', 
               '10000-12000', '12000-14000', '14000-16000']
data = [11, 15, 12, 9, 5, 4, 2, 1]

# Plotting
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Using Seaborn to plot histogram
sns.barplot(x=line_labels, y=data, ax=ax, palette="viridis")

# Add grid
ax.grid(True)

# Axis labels and title
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)
plt.title('Electricity Generation Capacity of Power Plants', fontsize=16)

# Rotate x-axis labels if too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=10, wrap=True)

# Automatically adjust subplot params for the figure to fit into the subplot area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/186.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear current figure state
plt.clf()
