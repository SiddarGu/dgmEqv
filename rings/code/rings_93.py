
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Robotics','Artificial Intelligence','Nanotechnology','Biotechnology','Aerospace Engineering']
data = [19,29,13,12,27]
line_labels = ['Field', 'ratio']

# Plot
plt.figure(figsize=(8,8))
ax = plt.subplot(111)
ax.pie(data, startangle=90,counterclock=False, autopct='%.2f%%', pctdistance=0.8, wedgeprops={'width': 0.4, 'edgecolor':'black'})

# Create a white circle to add the ring effect
centre_circle = plt.Circle((0,0),0.7,fc='white')
ax.add_artist(centre_circle)

# Add legend
ax.legend(data_labels, loc="upper right")

# Add title
plt.title('Advances in Science and Engineering - 2023')

# Adjust the figure
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_35.png')

# Clear the current figure
plt.cla()