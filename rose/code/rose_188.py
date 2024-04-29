
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Energy', 'Carbon Reduction', 'Waste Management', 'Air Pollution', 'Water Pollution', 'Climate Change', 'Sustainable Development', 'Environmental Protection', 'Biodiversity Conservation']
data = [120, 90, 80, 70, 60, 50, 30, 20, 10]
line_labels = ['Category', 'Number']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color='C'+str(i))
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)
ax.set_title('Number of Initiatives to Address Environmental and Sustainability Issues in 2021')
ax.legend(bbox_to_anchor=(1.1, 0.5))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_26.png')
plt.clf()