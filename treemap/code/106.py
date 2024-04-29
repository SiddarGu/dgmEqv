import matplotlib.pyplot as plt
import squarify

# Given data as a string
raw_data = """
Medicine,22
Engineering,18
Computer Science,15
Biology,12
Chemistry,10
Physics,8
Social Sciences,7
Environmental Science,5
Mathematics,3
"""

# Transform the data into the required format
data_labels = ["Research Funding (%)"]
line_labels = []
data = []

# Split the data into lines and extract labels and values
for line in raw_data.strip().split('\n'):
    label, value = line.split(',')
    line_labels.append(label)
    data.append(int(value))

# Create a figure to draw the plot on
plt.figure(figsize=(12, 8))

# Create a color palette
colors = plt.cm.Spectral_r([i/float(len(data)) for i in range(len(data))])

# Create and display the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.6, text_kwargs={'wrap': True})

# Set the title of the figure
plt.title("Percentage Distribution of Research Funding Across Academic Disciplines")

# Automatically resize the image
plt.tight_layout()

# Ensure that the labels do not overlap by rotation or increasing figure size
for ax in plt.gcf().axes:
    for label in ax.get_xticklabels():
        label.set_rotation(45)  # Or 'label.set_rotation_mode("anchor")'
    for label in ax.get_yticklabels():
        label.set_rotation(45)  # Or 'label.set_rotation_mode("anchor")'

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/106.png"
plt.savefig(save_path, format="png", bbox_inches="tight")

# Clear the current image state
plt.clf()
