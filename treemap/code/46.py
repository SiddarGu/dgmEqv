import matplotlib.pyplot as plt
import squarify

# Given data in multiline string format
data_str = """Research Area,R&D Funding Allocation (%)
Biotechnology,22
Artificial Intelligence,18
Renewable Energy,17
Aerospace Engineering,15
Material Science,10
Electrical Engineering,8
Chemical Engineering,5
Nanotechnology,3
Environmental Science,2"""

# Splitting the given data by lines and then by commas to extract labels and values
lines = data_str.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = []
data = []

# Iterate over each line (skipping the header)
for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(float(parts[1]))  # Convert the percentage to float for the tree map

# Define color palette
colors = plt.cm.Spectral_r([i / float(len(data)) for i in range(len(data))])

# Plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'wrap': True})

# Adding the title to the plot
plt.title('Research and Development Funding Distribution in Science and Engineering')

# Removing the axes
plt.axis('off')

# Automatically adjust subplot params for a nicer layout
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/46.png', format='png', dpi=300)

# Clear the current figure state to prevent overlapping of figures
plt.clf()
