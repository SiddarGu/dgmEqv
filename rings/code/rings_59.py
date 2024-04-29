

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Ticket Sales','Broadcast Revenue','Sponsorship','Merchandise','Other']
data = [40, 15, 30, 10, 5]
line_labels = ['Category','ratio']

# Plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the pie chart
ax.pie(data, startangle=90, counterclock=False, labeldistance=1.2,
       wedgeprops={'linewidth': 1.5, 'edgecolor': 'black'},
       textprops={'fontsize': 14}, autopct='%1.1f%%')

# Create a white circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Label the pie chart
ax.legend(data_labels, fontsize=14, loc='upper left')

# Adjust the radius of the inner circle to create different ring widths.
centre_circle.set_radius(0.5)

# Set the title of the figure
ax.set_title("Sports and Entertainment Industry Profitability - 2023", fontsize=16)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_124.png')

# Clear the current image state
plt.clf()