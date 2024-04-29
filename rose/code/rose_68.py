
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Airport', 'Hotel', 'Cruise', 'Tourist Attraction', 'Tour Operators', 'Transportation', 'Restaurants']
line_labels = ['Number of Passengers', 'Number of Guests', 'Number of Tourists', 'Number of Visitors', 'Number of Travelers', 'Number of Riders', 'Number of Diners']
data = [97, 54, 35, 25, 18, 15, 12]

# Create figure before plotting
fig = plt.figure(figsize = (8, 8))

# Set up the axes in polar coordinates, which is necessary for creating a rose chart
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i/num_categories))

# Add legend outside of the main chart area
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', labels=data_labels, fontsize='x-large')

# Set the number of ticks
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))

# Set the labels for each sector
ax.set_xticklabels(line_labels, fontsize='x-large')

# Set the title
ax.set_title("Number of People Engaged in Tourism and Hospitality Activities in 2021", fontsize='xx-large')

# Resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_36.png')

# Clear the current image state
plt.clf()