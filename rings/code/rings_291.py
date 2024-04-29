

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Extract data from data
data_labels = ['Retention Rate', 'Training Satisfaction', 'Recruiting Time', 'Performance Evaluation', 'Employee Engagement']
data = [30,10,20,30,10]

# Create figure
fig = plt.figure(figsize=(7,7))

# Plot data
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['red','green','blue','yellow','purple'])

# Create the ring chart
inner_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(inner_circle)

# Add data labels
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.3, 0.9))

# Set title
ax.set_title('Employee Management Evaluation - 2023')

# Resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_21.png')

# Clear figure
plt.clf()