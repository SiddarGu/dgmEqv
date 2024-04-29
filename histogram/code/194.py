import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ['Product Sales ($ Million)', 'Number of Companies']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data = [18, 22, 17, 13, 11, 9, 7, 5, 3, 2]

# Transform data into the appropriate format for Seaborn
data_dict = {data_labels[0]: line_labels, data_labels[1]: data}
data_df = pd.DataFrame(data_dict)

# Create a figure and a horizontal bar plot
plt.figure(figsize=(10, 7))
ax = sns.barplot(x=data_labels[1], y=data_labels[0], data=data_df, palette="viridis")

# Set the title of the figure
plt.title('Revenue Distribution Among Food and Beverage Companies')

# Rotate and wrap the labels if necessary
ax.set_ylabel(data_labels[0])
ax.set_xlabel(data_labels[1])
plt.setp(ax.get_yticklabels(), rotation=45, horizontalalignment='right', wrap=True)

# Use seaborn's despine to remove the top and right spines
sns.despine()

# Automatically adjust subplot params
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/194.png'
plt.savefig(save_path, dpi=300)

# Clear the current image state
plt.clf()
