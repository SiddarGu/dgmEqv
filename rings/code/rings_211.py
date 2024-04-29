
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ['Online Sales', 'Store Sales', 'Advertising', 'Customer Service', 'Logistics']
data = np.array([45, 30, 12, 10, 3])
line_labels = ['Category', 'Ratio']

# Change to percentage
data = data/np.sum(data) * 100

# Set colors
colors = cm.rainbow(np.linspace(0, 1, len(data)))

# Set figsize
plt.figure(figsize=(10,10))

# Create subplot
ax = plt.subplot()

# Draw ring
ax.pie(data, startangle=90, counterclock=False, colors=colors, wedgeprops={'linewidth': 3, 'edgecolor': 'black'})

# Create inner circle
centre_circle = plt.Circle((0,0),0.6, fc='white')
ax.add_artist(centre_circle)

# Set legend
ax.legend(data_labels, loc='upper right')

# Set title
plt.title('Retail and E-commerce Performance - 2023')

# Fit figure
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_65.png')

# Clear current image state
plt.clf()