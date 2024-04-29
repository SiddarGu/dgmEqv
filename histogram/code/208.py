import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Under 50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', 'Over 350']
data = np.array([12, 35, 50, 40, 20, 5, 3, 2])
line_labels = ['Number of Hotels']

# Create a figure
plt.figure(figsize=(12, 8))
ax = plt.subplot(111)

# Plotting the histogram
bars = plt.bar(data_labels, data, color=plt.cm.viridis(np.linspace(0.3, 0.7, len(data_labels))))

# Add grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set title and labels
plt.title('Hotel Pricing Trends in the Tourism Industry')
plt.xlabel('Average Daily Rate (USD)')
plt.ylabel('Number of Hotels')

# If the text length of label is too long, rotate the labels
plt.xticks(rotation=45, ha='right')
plt.yticks(np.arange(0, max(data) + 1, 5))

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/208.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
