import matplotlib.pyplot as plt
import squarify

# Raw data provided
raw_data = """
Category,Online Sales Percentage (%)/n Electronics,30/n Apparel,22/n Home Furnishings,15/n Books,10/n Groceries,9/n Beauty Products,7/n Sports Equipment,4/n Toys,3
"""

# Parsing the data
raw_data = raw_data.replace('/n', '\n').strip()  # Replacing '/n' with actual newline and stripping the leading/trailing whitespace
lines = raw_data.split('\n')  # Splitting into lines
data_labels = lines[0].split(',')[1:]  # Extracting data labels
line_labels = [line.split(',')[0] for line in lines[1:]]  # Extracting line labels
data = [int(line.split(',')[1]) for line in lines[1:]]  # Extracting data

# Plotting the data as a treemap
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.7)
plt.title('E-commerce Sales Distribution by Category in 2023')
plt.axis('off')  # Hide the axis

# Enhancing label readability by checking the label length
for index, label in enumerate(ax.texts):
    if len(label.get_text()) > 10:
        new_label = '\n'.join(label.get_text()[i:i+10] for i in range(0, len(label.get_text()), 10))  # Wrapping long labels
        ax.texts[index].set_text(new_label)

plt.tight_layout()

# Saving the figure to the absolute path given
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/175.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear the current image state
plt.clf()
plt.close(fig)
