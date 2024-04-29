
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Social Media Engagement', 'Online Traffic', 'Web Design', 'User Experience', 'Digital Advertising']
data = np.array([41, 20, 22, 12, 5])
line_labels = ['Category', 'Ratio']

# Create figure before plotting, i.e., add_subplot() follows plt.figure()
fig, ax = plt.subplots(figsize=(7, 7))

# Plot the data with the type of rings chart
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%.1f%%', colors=['b', 'g', 'r', 'purple', 'orange'])

# Change the pie chart into a ring chart 
circle = plt.Circle(xy=(0, 0), radius=0.7, color='white')
ax.add_artist(circle)

# Plot the legend
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(1, 0.5))

# Set the title
plt.title('Impact of Social Media and the Web on Businesses -2023', fontsize=18)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_80.png')

# Clear the current image state
plt.clf()