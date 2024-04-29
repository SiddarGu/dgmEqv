
import matplotlib.pyplot as plt
import numpy as np

data_labels = np.array(['Infrastructure', 'Public Services', 'Environment', 'Social Welfare', 'Taxation'])
data = np.array([22, 24, 8, 24, 22])
line_labels = np.array(['Category', 'ratio'])

# Create figure
fig = plt.figure(figsize=(10, 5))

# Plotting data
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['#F78A25', '#9F9FAD', '#FFCA79', '#6DBCEB', '#FFCA79'])

# Create white circle
center_circle = plt.Circle((0, 0), 0.7, color='white')

# Add white circle to center of the pie chart
ax.add_artist(center_circle)

# Set title
ax.set_title('Government and Public Policy Results - 2023')

# Add legend
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=5, fontsize='small')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_134.png', dpi=300)

# Clear current image state
plt.clf()