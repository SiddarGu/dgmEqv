
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

data_labels = ["User Engagement", "User Experience", "Social Media Reach", "Web Traffic", "Digital Advertising"]
data = [31, 19, 18, 15, 17]
line_labels = ["Category", "ratio"]

# construct figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# construct pie chart
ax.pie(data, 
       labels=data_labels, 
       startangle=90, 
       counterclock=False, 
       colors=['#FF7F00', '#FFB000', '#FFF700', '#00FF40', '#00BFFF'])

# construct ring chart
inner_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(inner_circle)

# adjust the position of legend
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=5)

# set title
ax.set_title("Social Media and Web Performance - 2023")

# save and clear image
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_60.png")
plt.clf()