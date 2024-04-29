
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Online Shopping", "Social Networking", "Online Advertising", "Online Video Streaming", "Online Dating", "Online Payments", "Online Gaming", "Online Music Streaming"]
data = [87, 97, 67, 83, 77, 48, 50, 36]
line_labels = ["Category", "Number"]

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# draw the sectors with different colors
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])

# set the axis labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=8, wrap=True)

# set the legend outside the chart
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)

# set the title
ax.set_title("Frequency of Online Activities in 2021", fontsize=10)

# set the figure size
fig.set_figwidth(8)
fig.set_figheight(8)

# set figure display
plt.tight_layout()

# save the figure
fig.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_129.png")

# clear the current figure
plt.clf()