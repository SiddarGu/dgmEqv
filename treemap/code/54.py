import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Crop Type,Production Volume (%)
Cereals,30
Vegetables,25
Fruits,20
Dairy,10
Meat,9
Poultry,4
Fisheries,2"""

# Processing data to extract labels and values
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Plotting the treemap
fig, ax = plt.subplots(figsize=(12, 8))
cmap = plt.cm.viridis
norm = plt.Normalize(vmin=min(data), vmax=max(data))
colors = [cmap(norm(value)) for value in data]

squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'fontsize': 9})

plt.title('Proportion of Global Agricultural Production by Crop Type', fontsize=14)
plt.axis('off')

# Automatically resize the image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/54.png', format='png', dpi=300)

# Clear the current image state
plt.clf()
plt.close()
