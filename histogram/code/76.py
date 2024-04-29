import matplotlib.pyplot as plt

# Data initialization
data_labels = ['Engineering', 'Health Sciences', 'Business', 'Education', 'Information Technology', 
               'Visual and Performing Arts', 'Humanities', 'Social Sciences', 'Environmental Science']
line_labels = ['Number of Graduates']
data = [1300, 950, 750, 650, 500, 350, 275, 225, 150]

# Create the figure and a single subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data as a vertical histogram
bars = ax.bar(data_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Add some style
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('Number of Graduates by Field of Study in 2023')

# Labeling
plt.xlabel('Field of Study')
plt.ylabel('Number of Graduates')
plt.xticks(rotation=45, ha='right', wrap=True)

# Resize to ensure no overlapping or cut-off content
plt.tight_layout()

# Save the plot to an image file
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/76.png'
plt.savefig(save_path, format='png')

# Clear the current figure's state to prevent interference with subsequent plots
plt.clf()
