import matplotlib.pyplot as plt
import os

# Provided data
data_labels = ['Biotechnology', 'Aerospace', 'Renewable Energy', 'Materials Science', 'Robotics', 'Information Technology', 'Pharmaceuticals', 'Artificial Intelligence', 'Quantum Computing']
data = [5.2, 6.8, 4.9, 3.7, 5.1, 7.3, 6.1, 4.5, 3.2]
line_labels = 'Research Expenditure ($Billion)'

# Create a new figure with a suitable figsize
plt.figure(figsize=(12, 8))

# Add a subplot to the figure
ax = plt.subplot()

# Create vertical histograms
ax.bar(data_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Add title and labels to the plot
ax.set_title('Research and Development Expenditure Across Scientific Disciplines')
ax.set_xlabel('Scientific Disciplines')
ax.set_ylabel('Expenditure ($ Billion)')

# Set rotation for the x-axis labels if they are too long
plt.xticks(rotation=45, ha='right', wrap=True)

# Adding background grid
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Tight layout to automatically adjust parameters to give specified padding
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/79.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure's state
plt.clf()
