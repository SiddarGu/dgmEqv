import matplotlib.pyplot as plt
import seaborn as sns

# Data setup
data_labels = ['Online Campaigns', 'Direct Mail', 'Fundraising Events',
               'Corporate Donations', 'Legacy Gifts', 'Telethons', 'Street Fundraising']
line_labels = ['Amount Raised ($Million)']
data = [75.2, 55.3, 68.4, 82.1, 40.3, 61.7, 53.9]

# Create the figure and the axes
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plotting the histogram using seaborn
sns.barplot(x=data_labels, y=data, ax=ax, palette='viridis')

# Rotate the x-axis labels if they're too long
plt.xticks(rotation=45, ha='right', wrap=True)

# Setting the title of the histogram
plt.title('Fundraising Revenue for Charitable Nonprofit Organizations')

# Adding grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjusting the layout to fit the figure neatly
plt.tight_layout()

# Save the chart as a .png file
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1015.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the pyplot state to prevent any further changes to this figure
plt.clf()
