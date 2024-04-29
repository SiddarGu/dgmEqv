import matplotlib.pyplot as plt
import squarify

# Parsing the provided data
data_str = """
Product Category,Production Share (%)
Cereals,25
Vegetables,20
Fruits,20
Dairy,15
Meats,10
Oilseeds,5
Sugar Crops,3
Fibre Crops,2
"""

# Preparing the data
data_lines = data_str.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [float(line.split(',')[1]) for line in data_lines[1:]]

# Plotting the treemap
fig = plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=.8, text_kwargs={'wrap': True})
plt.title("Shares of Global Agriculture Production by Category", fontsize=14)
plt.axis('off')

# Automatically resize the image and save it
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/70.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current image state
plt.clf()
