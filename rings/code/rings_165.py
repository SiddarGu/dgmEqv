
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Transform the given data into three variables
data_labels = ['Music', 'Dance', 'Theatre', 'Visual Arts', 'Cinematography']
data = [25, 10, 17, 35, 13]
line_labels = ['2023']

# Plot the data with rings chart
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, autopct='%.1f%%',labels=data_labels, colors=mpl.rcParams['axes.prop_cycle'].by_key()['color']) 

# Change the pie chart into a ring chart
inner_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(inner_circle) 

# Add legend
ax.legend(data_labels, bbox_to_anchor=(1.2,1))

# Set title
ax.set_title("Cultural Appreciation - 2023")

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_138.png')

# Clear the current image state
plt.clf()