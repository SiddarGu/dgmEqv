
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Connectivity', 'Digital Security', 'Network Reliability', 'User Experience', 'Innovation']
data = [39, 25, 19, 16, 1]
line_labels = ['Category', 'Ratio']

#Create figure before plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

#Plot the data with the type of rings chart
radius = 1.
wedges, texts, autotexts = ax.pie(data, radius=radius, labels=data_labels, autopct='%1.1f%%', colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], startangle=90, counterclock=False)

#Creating the white circle to make the chart into a ring chart
centre_circle = plt.Circle((0, 0), radius/2, color='white')
ax.add_artist(centre_circle)

#Adding legend
ax.legend(data_labels, loc='upper left')

#Drawing techniques such as background grids can be used
ax.grid(True, ls='--', color='#848484')

#Set the title of the figure
plt.title('Technology and the Internet - 2023 Performance Overview', fontsize=20)

#Automatically resize the image by tight_layout()
plt.tight_layout()

#Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_107.png')

#Clear the current image state
plt.cla()
plt.clf()
plt.close()