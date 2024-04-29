import matplotlib.pyplot as plt
import squarify

# Parsing the data
data_str = "Category,Market Share (%)/nDairy Products,17/nBeverages,25/nConfectionery,15/nBakery Products,13/nMeat and Poultry,10/nSeafood,8/nSnack Foods,7/nGrains and Cereals,5"
data_rows = data_str.split('/n')

# Extracting labels and data
data_labels = data_rows[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in data_rows[1:]]
data = [float(row.split(',')[1]) for row in data_rows[1:]]

# Create a figure object with an appropriate size to ensure readability
plt.figure(figsize=(12, 8))

# Using squarify to plot the treemap
colors = plt.cm.Paired(range(len(data)))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.6)

# Setting the title of the figure
plt.title('Market Share Distribution in the Food and Beverage Industry', fontsize=14)

# Improving the layout to prevent content overlapping
plt.axis('off')
plt.tight_layout()

# Saving the figure to the specified absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/208.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure to avoid conflicts in subsequent plots
plt.clf()
