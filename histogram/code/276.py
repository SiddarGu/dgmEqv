import matplotlib.pyplot as plt
import numpy as np

# Parsing the data
raw_data = """Product Category,Annual Sales ($Billion)
Alcoholic Beverages,48.3
Non-Alcoholic Drinks,60.4
Packaged Foods,77.2
Snacks,33.9
Dairy Products,51.7
Meat and Poultry,43.6
Seafood,12.5
Confectionery,29.8
Bakery Goods,36.1"""

# Transforming the data into variables
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot()

# Drawing a horizontal bar chart
y_pos = np.arange(len(line_labels))
ax.barh(y_pos, data, align='center', color='skyblue')
ax.set_yticks(y_pos)
ax.set_yticklabels(line_labels, rotation=0, ha='right', wrap=True)
ax.set_xticks(np.arange(0, max(data) + 10, 10))
ax.set_xlabel(data_labels[0])
ax.set_title('Annual Sales Performance in the Food and Beverage Industry')

# Adding the grid
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically resizing the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/626.png', bbox_inches='tight')

# Clear the current image state
plt.clf()
