import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Transform the data into three variables: data_labels, data, line_labels. 
raw_data = """Field of study,Graduates (Thousands),Job availability (Thousands),Research funds (Billion $),Global leadership position (Score)
Sociology,50,30,2,7
Anthropology,40,25,1.5,6
Psychology,70,40,3,8
Literature,60,20,1,7
Philosophy,25,10,0.8,6
Arts,80,50,2.5,8
History,55,35,2,7
Performing Arts,75,60,3.5,9"""
lines = raw_data.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [f"{line.split(',')[0]} {line.split(',')[3]}" for line in lines[1:]]
data = np.array([list(map(float, line.split(",")[1:])) for line in lines[1:]])

# Create figure before plotting
fig, ax = plt.subplots(figsize=(12, 9))

# Create a scatter plot where the third value of each row is mapped to the bubble size, 
# and the fourth value is mapped to the color value.
color_norm  = mcolors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
bubble_size_norm = mcolors.Normalize(vmin=data[:,2].min() - 0.5, vmax=data[:,2].max())
scalar_map = plt.cm.ScalarMappable(norm=color_norm, cmap='viridis')

# Plot the data with the type of bubble chart
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], alpha=0.5, s=bubble_size_norm(data[i, 2])*5000, 
               label=None, c=scalar_map.to_rgba(data[i, 3]))
    ax.scatter([], [], c=scalar_map.to_rgba(data[i, 3]), alpha=0.5, 
               s=20, label=line_labels[i])

# Plot the legend
ax.legend(title=data_labels[2])

# Add a colorbar
colorbar = plt.colorbar(scalar_map, ax=ax)
colorbar.set_label(data_labels[3])

# Adjust the drawing techniques
plt.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Job availability and Global leadership Scores Across Various Humanities Disciplines')

# Automatically resize the image
plt.tight_layout()

# Save and show the chart
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/246_202312310045.png')
plt.show()

# Clear the current image state.
plt.close()
