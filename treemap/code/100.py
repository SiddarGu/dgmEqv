import matplotlib.pyplot as plt
import squarify

# Raw data
raw_data = """Product Category,Sales Revenue (%)
Packaged Foods,25
Beverages,20
Fresh Produce,15
Meat & Poultry,14
Dairy Products,10
Snacks & Sweets,8
Seafood,4
Grains & Cereals,2
Specialty Foods,2"""

# Transform raw data into variables data_labels, data, line_labels
lines = raw_data.split('\n')
data_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]
line_labels = ['{0} ({1}%)'.format(label, value) for label, value in zip(data_labels, data)]

# Define the color palette
cmap = plt.cm.tab20
mini, maxi = min(data), max(data)
norm = plt.Normalize(mini, maxi)
colors = [cmap(norm(value)) for value in data]

# Create a figure
plt.figure(figsize=(12, 8))

# Create a treemap with squarify
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':9, 'wrap':True})

# Set the title and axis off
plt.title('Market Share of Food and Beverage Categories', fontsize=16)
plt.axis('off')

# Automatically resize layout to prevent overlap
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/100.png', dpi=300)

# Clear the current figure state for future plots
plt.clf()
