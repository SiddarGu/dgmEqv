import matplotlib.pyplot as plt
import squarify

# Transforming the given data
data_labels = ['Freight Volume (%)']
line_labels = ['Road', 'Rail', 'Air', 'Sea', 'Pipeline', 'Intermodal']
data = [40, 25, 15, 10, 5, 5]

# Defining colors for each segment
colors = plt.cm.Spectral([0.1, 0.25, 0.5, 0.75, 0.9, 1.0])

# Creating the figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, aspect="auto")

# Creating the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':10, 'wrap':True})

# Customizing the chart
plt.title("Modal Split of Freight Volume in Transportation and Logistics Industry", fontsize=16)
plt.axis('off')

# Adjust layout to prevent content from being cut off
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1029.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.cla()
plt.clf()
plt.close()
