
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables.
y_values = ['Number of Tourists (Millions)', 'Average Spent per Tourist ($ Hundred)', 'Hotel Occupancy Rate (%)'] 

data = np.array([[50,50,80],
                 [25,60,70],
                 [35,45,75],
                 [20,40,65],
                 [15,55,78]])

x_values = ['USA', 'UK', 'France', 'Spain', 'Germany']

#Create figure before plotting
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

#Plot the data with the type of 3D bar chart
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), 0, 0.5, 0.5, data[:, i],
            color='b', alpha=0.5, edgecolor='k')

#Set the dimensions of the bars
ax.set_zlabel('Number of Tourists (Millions)')
ax.set_ylabel('Average Spent per Tourist ($)')
ax.set_xlabel('Hotel Occupancy Rate (%)')

#Set the title of the figure 
ax.set_title('Tourism and Hospitality in Major Countries - An Overview')

#Rotate the X-axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

#Automatically resize the image
plt.tight_layout()

#Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/14_202312270030.png')

#Clear the current image state
plt.clf()