
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ['Food Cost', 'Beverage Cost', 'Labor Cost', 'Overhead Cost', 'Profit']
data = np.array([25, 25, 25, 15, 10])
line_labels = ['Category', 'Ratio']

# Create a pie chart with different colors
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%.1f%%')

# Change Chart Type To Ring Chart
centre_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Add legend
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.05))

# Set title
ax.set_title("Financial Health of Food and Beverage Industry - 2023", fontsize=14)

# Resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_25.png')

# Clear the current image state
plt.cla()