import matplotlib.pyplot as plt
import numpy as np
import os

# Data
data_string = """Disease Incidence (per 100,000),Number of Cases
Heart Disease,252.4
Cancer,208.6
Stroke,72.3
Diabetes,93.5
Chronic Respiratory Diseases,58.2
Influenza and Pneumonia,65.7
Kidney Diseases,43.9
Alzheimer's Disease,37.6"""

# Transform data into variables
lines = data_string.strip().split('\n')
data_labels = [label.strip() for label in lines[0].split(',')][1:]
line_labels = [line.split(',')[0].strip() for line in lines[1:]]
data = np.array([float(line.split(',')[1].strip()) for line in lines[1:]])

# Plotting
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Create histogram
colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
ax.bar(line_labels, data, color=colors)

# Customizing the plot
ax.set_title('Prevalence of Major Diseases in the Population')
ax.set_xlabel('Diseases')
ax.set_ylabel('Incidence (per 100,000)')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate and wrap the x-axis labels if they are too long
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", wrap=True)

# Automatically adjust subplot params for a nicer fit
plt.tight_layout()

# Ensure the directory exists
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png'
os.makedirs(save_path, exist_ok=True)

# Save the figure
plt.savefig(f'{save_path}/8.png', format='png')

# Clear the current figure state to avoid overlap with future plots
plt.clf()
