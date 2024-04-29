

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

data_labels=['Artistic Expression', 'Cultural Diversity', 'Historic Preservation', 'Education', 'Arts Funding']
line_labels=['Category', 'ratio']
data=np.array([[20, 38, 18, 14, 10]])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

colors = ['#ff3300','#ff9900', '#ffcc00', '#66ccff','#0099ff']
ax.pie(data.flatten(), colors=colors, startangle=90, counterclock=False)

# Create a white circle to make the pie chart into a ring chart
centre_circle = Circle((0,0), 0.7, color='white')
ax.add_artist(centre_circle)

# Set the parameters of legend
ax.legend(data_labels, loc='upper center', fontsize='large',
          bbox_to_anchor=(0.5, -0.1))

# Set the title for the figure
plt.title('Arts and Culture Landscape - 2023')

# Set the parameters of figure
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_131.png')

# Clear the current state of figure
plt.clf()