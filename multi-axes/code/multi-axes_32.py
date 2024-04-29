

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Patient Visits (Millions)', 'Patient Satisfaction Score (1-10)', 'Average Wait Time (Minutes)']
line_labels = ['Emergency Care', 'Primary Care', 'Specialty Care', 'Mental Health Services', 'Diagnostic Care', 
               'Women\'s Health Services', 'Pediatric Care', 'Urgent Care']
data = np.array([[12, 8, 45], [18, 7, 30], [28, 9, 45], [6, 10, 60], [15, 6, 15], [7, 7, 35], [8, 9, 25], [10, 8, 20]])

# Create figure before plotting
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)

# Plot the data with the type of multi-axes chart
ax1.bar(line_labels, data[:,0], width=0.3, color='#FFC222', alpha=0.8)
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='#00BFFF', linestyle='--', marker='o')
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(line_labels, data[:,2], color='#228B22', linestyle='-', marker='s')

# Label all axes
ax1.set_ylabel(data_labels[0], color='#FFC222')
ax2.set_ylabel(data_labels[1], color='#00BFFF')
ax3.set_ylabel(data_labels[2], color='#228B22')

# Set the title of the figure
plt.title('Healthcare and Health Providers Performance Overview')

# Automatic resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/30_2023122261325.png')

# Clear the current image state at the end of the code
plt.clf()