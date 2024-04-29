
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Transform data into three variables
data_labels = ["Fundraising", "Grants and Donations", "Volunteer Time", "Outreach Programs", "Community Engagement"]
data = [41, 29, 14, 13, 3]
line_labels = ["Category", "Ratio"]

# Plot the data with a ring chart
fig = plt.figure()
ax = fig.add_subplot()
ax.pie(data, shadow=True, startangle=90, counterclock=False, colors=['orange', 'green', 'red', 'blue', 'purple'])
inner_circle = patches.Circle((0,0), 0.70, color='white') # create a white circle
ax.add_patch(inner_circle) # add the white circle to the axes
ax.legend(data_labels, loc="best")
ax.set_title("Nonprofit Organizations - 2023")
plt.tight_layout()
# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_31.png')
# Clear the current image state
plt.clf()