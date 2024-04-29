
import matplotlib.pyplot as plt
import numpy as np

#transform the given data into three variables
data_labels = ['Education', 'Healthcare', 'Social Services', 'Economic Development', 'Public Safety', 'Transportation', 'Environmental Management', 'Infrastructure Development', 'Local Government']
data = [90, 45, 60, 92, 82, 86, 73, 65, 50]
line_labels = ['Category', 'Number']

#create figure before plotting
plt.figure(figsize=(10,10))

#plot the data
ax = plt.subplot(polar=True)
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

#assign a different color to each sector
colors = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c", "#98df8a", "#d62728", "#ff9896", "#9467bd"]

#create sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(x=i*sector_angle, width=sector_angle, height=data[i], color=colors[i], edgecolor='black', label=data_labels[i])

#set the labels of each sector
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=10)
ax.set_rlabel_position(0)

#position legend outside of chart area
ax.legend(bbox_to_anchor=(1, 0), loc=3, fontsize=10, edgecolor='black')

#give the figure a title
ax.set_title('Quantifying Government and Public Policy Programs in 2021')

#show the plot
plt.show()

#save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_11.png', bbox_inches='tight')

#clear the current image state
plt.clf()