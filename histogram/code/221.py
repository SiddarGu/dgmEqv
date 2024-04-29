import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data preparation
data_labels = ['Freight Volume (million tons)']
line_labels = ['Trucks', 'Rail', 'Air', 'Maritime', 'Pipelines']
data = [1500.5, 1285.2, 450.3, 980.7, 635.1]

# Creating a DataFrame for seaborn
df = pd.DataFrame(data={'Vehicle Type': line_labels, 'Freight Volume': data})

# Setting the figure size to ensure content is displayed properly
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Create the histogram using seaborn
sns.barplot(x='Vehicle Type', y='Freight Volume', data=df, ax=ax)

# Set title
ax.set_title('Freight Volume Distribution Across Transportation Modes')

# Improve the readability of x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", wrap=True)

# Automatically adjust subplot params for a better layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/221.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
