
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Sightseeing','Accommodation','Food and Beverage','Attraction','Reviews']
data = [20,35,25,10,10]
line_labels = ['Category','ratio']

# Create figure
fig, ax = plt.subplots(figsize=(10,5))

# Plotting data
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, wedgeprops={"edgecolor":"k",'linewidth': 0.5})

# Add white center to make the chart as a ring chart
centre_circle = plt.Circle((0,0),0.7,fc='white')
ax.add_artist(centre_circle)

# Adjusting the legend
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.2, 1))

# Set title
ax.set_title('Tourism and Hospitality Performance Review - 2023')

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_17.png')

# Clear the current image state
plt.clf()