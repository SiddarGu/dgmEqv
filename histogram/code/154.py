import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_str = """Packaged Beverages,18.75
Fresh Produce,12.30
Bakery and Confectionery,9.20
Dairy Products,13.65
Meat and Poultry,16.80
Seafood,7.40
Snack Foods,14.55
Frozen Foods,11.95
Beverage Manufacturing,19.80
Organic Foods,8.50"""

# Preprocess the data
data_lines = data_str.split('\n')
data_labels = ['Product Category', 'Annual Sales (Billion $)']
line_labels = [line.split(',')[0] for line in data_lines]
data = [float(line.split(',')[1]) for line in data_lines]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Create a figure and a set of subplots
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

# Plotting the histogram
df.plot(kind='bar', ax=ax, rot=45, fontsize=9, legend=False)

# Set title, labels and grid
ax.set_title('Annual Sales by Product Category in the Food and Beverage Industry')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to make sure everything fits without overlapping
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/154.png', format='png')

# Clear the current figure's state to ensure no information is left
plt.clf()
