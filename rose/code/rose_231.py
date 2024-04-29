
import matplotlib.pyplot as plt
import numpy as np

#transform the data into three variables
data_labels = ["Pre-School", "Elementary School", "Middle School", "High School", "College", "Graduate School"]
data = [120,350,450,650,1100,480]
line_labels = ["Level of Education", "Number of Students"]

#create figure before plotting
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(111, projection='polar')

#calculate the sector angle
sector_angle = (2 * np.pi) / len(data)

#plot the data with the type of rose chart
for i in range(len(data)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

#add legend
ax.legend(data_labels, bbox_to_anchor=(1.5, 0.8))

#set the ticks, labels and title
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)
ax.set_title("Student Enrollment in Different Levels of Education in 2021", fontsize=20)

#resize the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_65.png')

#clear the current image state
plt.clf()