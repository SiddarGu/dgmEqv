import matplotlib.pyplot as plt
import squarify

# Data setup
data = "Product Type,Production Volume (%)/n Consumer Electronics,25/n Automobiles,20/n Pharmaceuticals,15/n Textiles,12/n Food Processing,10/n Machinery,8/n Plastics,5/n Chemicals,3/n Metals,2"
data = data.split('/n ')
data_labels = data[0].split(',')[1:]
line_labels = [item.split(',')[0] for item in data[1:]]
data = [float(item.split(',')[1]) for item in data[1:]]

# Visualize as a treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.8, text_kwargs={'fontsize':10, 'wrap':True})
plt.title('Proportional Manufacturing Output by Product Type')
plt.axis('off')

# Adjust layout, save and clear figure
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/132.png'
plt.savefig(save_path, format='png')
plt.clf()
