import matplotlib.pyplot as plt
import squarify

# parsing the provided data
data_string = """Product Category,Online Sales (%)
Electronics,25
Clothing,20
Home & Garden,15
Health & Beauty,13
Books & Media,10
Groceries,8
Toys & Hobbies,5
Jewelry,4"""

# Splitting the data string into lines and then into labels and values
lines = data_string.strip().split('\n')
labels = [line.split(',')[0] for line in lines[1:]]  # exclude the header
sizes = [int(line.split(',')[1]) for line in lines[1:]]  # exclude the header

# Create a colormap
cmap = plt.cm.viridis
mini = min(sizes)
maxi = max(sizes)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in sizes]

# Treemap plotting
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7)

plt.title('E-commerce Sales Distribution by Product Category')
plt.axis('off')  # Disable the axis lines and labels

# Resize the image to fit the labels and prevent clipping
plt.tight_layout()

# Save the figure with an absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/228.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
