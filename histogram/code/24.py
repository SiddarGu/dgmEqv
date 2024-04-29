import matplotlib.pyplot as plt

# Given data
data_labels = ['CO2 Emission Range (Million Metric Tons)', 'Number of Countries']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data = [18, 14, 9, 5, 2, 1, 0, 1, 1, 0]

# Create figure with larger figsize to prevent content from being displayed improperly
plt.figure(figsize=(10, 8))

# Create a horizontal histogram
ax = plt.subplot(111)
ax.barh(line_labels, data, color=plt.cm.viridis(np.linspace(0, 1, len(data))))

# Set title
plt.title('Global Distribution of CO2 Emissions by Country')

# Adding grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add x and y labels
plt.xlabel(data_labels[1])
plt.ylabel(data_labels[0])

# Ensure labels with long text are not stacked upon each other
plt.xticks(rotation='vertical')  # Optional: Use plt.yticks if the y labels are too long
ax.tick_params(axis='both', which='major', labelsize=8)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure to the specified path with tight layout
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/24.png')

# Clear the current figure state to prevent interference with subsequent plots
plt.clf()
