import matplotlib.pyplot as plt
import squarify

# Process the input data into the required format
raw_data = """Category,Revenue Share (%)
Electronics,25
Fashion,20
Home & Garden,15
Health & Wellness,10
Automotive,10
Sports & Outdoors,10
Books & Music,5
Groceries,5"""

# Splitting data into rows on the basis of newline and columns on the basis of commas
data_split = [line.split(',') for line in raw_data.split('\n')]
data_labels = data_split[0][1:]  # Column labels (skipping the first 'Category' label)
line_labels = [row[0] for row in data_split[1:]]  # Row labels (skipping the 'Revenue Share (%)' column)
data = [float(row[1]) for row in data_split[1:]]  # Numerical data

# Set up the figure size
fig = plt.figure(figsize=(12, 8))

# Create a treemap
colors = plt.cm.tab20c.colors  # Predefined color cycle, which automatically maps numbers to colors
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':12, 'wrap':True})

# Title of the figure
plt.title("Revenue Distribution Across E-Commerce Categories", fontsize=18)

# Eliminate axis
plt.axis('off')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/48.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()

# Make sure to close the plot
plt.close(fig)
