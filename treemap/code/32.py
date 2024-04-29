import matplotlib.pyplot as plt
import squarify

# Given data in a string format
data_str = """Discipline,Research Funding (%)
Sociology,19
Psychology,17
Anthropology,13
History,12
Linguistics,10
Philosophy,9
Literature,7
Archaeology,7
Gender Studies,6"""

# Splitting the data and transforming into the required format
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]  # The first row, excluding the first column
line_labels = [row.split(',')[0] for row in lines[1:]]  # The labels of each row excluding the first row
data = [float(row.split(',')[1]) for row in lines[1:]]  # The numerical data of each row

# Creating the treemap
fig = plt.figure(figsize=(16, 9))  # Larger figsize for better display and readability
plt.title('Allocation of Research Funds in Social Sciences and Humanities')

# Create a color palette, mapped to these values
cmap = plt.cm.Blues
mini=min(data)
maxi=max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8)

# Adding padding to avoid overlapping of labels, as text length is taken care of by design
plt.axis('off')
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1009.png'
plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

# Clear the current image state
plt.clf()
