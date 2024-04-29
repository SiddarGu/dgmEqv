
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Biomedical Engineering", "Chemical Engineering", "Aerospace Engineering", "Materials Science"]
data = [250, 200, 150, 100, 80, 60, 40, 20]
line_labels = np.arange(1,9)

#Create figure before plotting
fig, ax = plt.subplots(figsize=(20,20))

#Plot the data with the type of rose chart
ax = plt.subplot(111, projection="polar") 

#Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

#Draw sectors corresponding to different categories
for i in range(len(data)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, bottom=0.0, label=data_labels[i], color=plt.cm.jet(i/num_categories))

#Set xticks
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=10)

#Reposition the legend
ax.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0.5)

#Set the title
plt.title("Number of Engineering Graduates in 2021")

#Save the chart
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_15.png")

#Clear the current image state
plt.clf()