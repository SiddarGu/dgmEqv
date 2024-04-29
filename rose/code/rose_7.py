
import matplotlib.pyplot as plt
import numpy as np
 
data_labels = ['Apparel','Electronics','Home Appliances','Groceries','Beauty Products','Home Decor','Books','Toys','Sports Equipment']
data = [54,45,38,36,34,31,28,24,19]
line_labels = ['Category','Number']
 
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111,projection='polar')
 
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
 
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width = sector_angle, color = 'C' + str(i), label = data_labels[i])
 
ax.legend(bbox_to_anchor=(1.1, 1.05), frameon = False)
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint = False))
ax.set_xticklabels(data_labels, fontsize = 12)

plt.title('Sales of Different Product Categories in the Retail and E-Commerce Sector',fontsize = 15)
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_13.png')
plt.clf()