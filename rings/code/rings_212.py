
import matplotlib.pyplot as plt
import numpy as np

# transform data
data_labels=np.array(['Financial Planning','Cost Management','Risk Management','Investment Strategies','Market Analysis'])
data=np.array([20,30,15,25,10])
line_labels=np.array(['Category','ratio'])

# create figure
fig, ax = plt.subplots(figsize=(8, 6))

# plot data
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%.1f%%')

# add a white circle to the center of the pie chart
centre_circle = plt.Circle((0,0),0.75, color='white', fc='white',linewidth=1.25)
ax.add_artist(centre_circle)

# add legend
ax.legend(data_labels, bbox_to_anchor=(1.2,1.0), loc="upper right")

# title
ax.set_title('Financial Management Strategies - 2023')

# adjust the image
plt.tight_layout()

# save image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_66.png")

# clear
plt.clf()