
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ["Mathematics", "Sciences", "Language Arts", "Social Sciences", "Arts", "Physical Education", "Technology", "Music"] 
data = [400, 350, 300, 250, 200, 150, 100, 50]
line_labels = ["Field", "Number of Students"]

fig = plt.figure(figsize=(8, 8)) 
ax = fig.add_subplot(111, projection='polar') 

num_categories = len(data_labels) 
sector_angle = (2 * np.pi) / num_categories 

for i in range(num_categories): 
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i)) 

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False)) 
ax.set_xticklabels(data_labels, wrap=True, horizontalalignment="center", fontsize=15)

ax.legend(bbox_to_anchor=(1.1, 1), loc="upper left") 
ax.set_title("Student Enrollment by Academic Field for 2021", fontsize=15) 

plt.tight_layout() 
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_86.png")
plt.clf()