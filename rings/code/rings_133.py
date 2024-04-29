
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle

data_labels = ['Vaccinations','Disease Prevention','Healthcare Access','Treatment Quality','Research Funding']
data = [14,20,21,25,20]
line_labels = ['Category','ratio']

fig, ax = plt.subplots(figsize=(7,7))

ax.pie(data, labels=data_labels, startangle=90,counterclock=False, autopct='%1.1f%%',labeldistance=1.2)

# Create a white circle to turn the pie chart into a ring.
my_circle=plt.Circle( (0,0), 0.7, color='white')

# add the circle to the axes
ax.add_artist(my_circle)

# Set the title of the figure
plt.title('Healthcare Quality in 2023')

# Set the legend positioning
ax.legend(data_labels,loc='upper left', bbox_to_anchor=(-0.1, 1))

# Add grids
plt.grid(which='both')

# Automatically adjust the size of the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_87.png')

# Clear the current image state
plt.clf()