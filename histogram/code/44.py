import matplotlib.pyplot as plt

# Creating data from the given dataset
data_labels = ['Engineering', 'Business', 'Health Sciences', 'Education', 'Humanities',
               'Social Sciences', 'Natural Sciences', 'Information Technology', 'Arts']
data = [150.2, 165.5, 120.0, 130.3, 60.4, 140.0, 90.1, 110.2, 70.5]

# Set the figure size to be larger
plt.figure(figsize=(12, 8))

# Add a subplot to the current figure
ax = plt.subplot()

# Create the histogram
ax.bar(data_labels, data, color='skyblue', edgecolor='black')

# Set the title of the figure
ax.set_title('Number of Graduates by Subject Area (Class of 2023)')

# Set the label rotation for long text
plt.xticks(rotation=45, ha='right')

# Add grid to the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set the labels for the axes
plt.xlabel('Subject Area')
plt.ylabel('Number of Graduates (Thousands)')

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/44.png'
plt.savefig(save_path, format='png')

# Clear the current figure after saving it
plt.clf()
