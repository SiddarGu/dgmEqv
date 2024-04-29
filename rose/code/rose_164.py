
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Fruit Production','Livestock Production','Dairy Production','Grain Production','Vegetable Production','Forestry','Fishing']
data = np.array([[50,150,90,170,80,60,30]])
line_labels = ['Category']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1,projection='polar')
num_categories = data.shape[1]
sector_angle = (2 * np.pi) / num_categories
# Create the sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, bottom=0.0, label=data_labels[i], color=np.random.rand(3,))
ax.set_thetagrids(np.degrees(np.arange(0, 2*np.pi, sector_angle)), labels=data_labels, fontsize=12, rotation=90)
ax.legend(bbox_to_anchor=(1.05, 0.7))
ax.set_title("Production of Major Agricultural Products in 2021")
plt.tight_layout()
plt.savefig(r"/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_59.png")
plt.clf()