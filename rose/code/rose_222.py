
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Fiscal Policy', 'Social Policy', 'Monetary Policy', 'Environmental Policy', 'Trade Policy', 'Defense Policy', 'Education Policy', 'Health Policy', 'Transportation Policy', 'Technology Policy']
data = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
line_labels = []

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2*np.pi) / num_categories

# Create the sectors in the plot
for index, value in enumerate(data):
    ax.bar(index*sector_angle, value, width=sector_angle, color=plt.cm.jet(index/num_categories), label=data_labels[index])

# Set the xticks to the middle of each sector
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
# Set the xticklabels to the data_labels
ax.set_xticklabels(data_labels, size='small', rotation=90, wrap=True)

# Position the legend
ax.legend(bbox_to_anchor=(1.2, 0.5))

# Give the plot a title
plt.title("Distribution of Government Regulations by Policy Area in 2021")

# Change the limits of the plot
ax.set_ylim(0, np.max(data))

# Draw a grid in the plot
ax.grid(linestyle='dotted', color='gray')

# Save the plot
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_4.png')

# Clear the current image state 
plt.gcf().clear()