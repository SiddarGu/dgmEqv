
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Transform data into three variables: data_labels, data, line_labels.
data_labels = ['Quality Control', 'Supply Chain', 'Production Efficiency', 'Cost Management', 'Safety Compliance']
data = [21, 23, 20, 17, 19]
line_labels = ['Category', 'Ratio']

# Create figure and plot the data.
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(data, startangle=90, counterclock=False, colors=['#F2A2B8', '#FAB2AC', '#F2D39B', '#F2F2B3', '#D8F2B3'])

# Add an inner circle to the figure to make it a ring chart.
inner_circle = plt.Circle((0, 0), 0.7, color='white', fc='white', linewidth=1.25)
ax.add_artist(inner_circle)

# Set title and legend.
ax.set_title('Manufacturing and Production Evaluation - 2023', fontsize=20)
ax.legend(data_labels, loc='lower right', fontsize=12, bbox_to_anchor=(1.2, 0.5))

# Automatically resize the image by tight_layout().
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_101.png')

# Clear the current image state.
plt.clf()