import matplotlib.pyplot as plt
import numpy as np

# Given data
data_string = "Category,Enrollment,Graduation Rate,Research Funding/subject,Humanities,28000,80%,$10 million/subject,Social Sciences,35000,75%,$12 million"
plot_types = ["bar chart","bar chart","bar chart"]

# Transform data to required format
data_rows = data_string.split("/")
data_labels = data_rows[0].split(",")[1:]
line_labels = [row.split(",")[1] for row in data_rows[1:]]
data = np.array([[float(item.replace('%','').replace('$','').replace(' million','e6')) for item in row.split(",")[2:]] for row in data_rows[1:]])

# Plot data
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], width=0.4, color='b', alpha=0.7)
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')

ax2 = ax1.twinx()
ax2.bar(line_labels, data[:,1], width=0.2, color='g', alpha=0.7, tick_label=line_labels)
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params(axis='y', colors='g')

if data.shape[1]>2:
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 70))
    ax3.bar(line_labels, data[:,2], width=0.1, color='r', alpha=0.7, tick_label=line_labels)
    ax3.set_ylabel(data_labels[2], color='r')
    ax3.tick_params(axis='y', colors='r')

plt.title('Education Data Analysis: Enrollment, Graduation Rate, and Research Funding by Field')
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/266_202312311430.png')
plt.clf()
