
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Arts and Culture", "Education", "Social Sciences", "Humanities", "Politics and Law", "Economics and Business"]
data = np.array([24,18,17,17,15,9])
line_labels = ["Topic", "ratio"]

# Plot the data with the type of rings chart.
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(data, 
       labels=data_labels, 
       startangle=90, 
       counterclock=False, 
       colors=plt.cm.Set3.colors[:len(data_labels)])
inner_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(inner_circle)
ax.set_title("Social Sciences and Humanities Overview - 2023")
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(1.3,1))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_71.png')
plt.clf()