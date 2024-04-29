
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Grocery','Clothing','Electronics','Furniture','Home Appliances','Household Items','Beauty and Health','Sports and Outdoors','Books and Toys','Music and Movies']
data = np.array([[100,90,80,70,60,50,40,30,20,10]])
line_labels = ['Number']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111,projection='polar')

for i in range(num_categories):
    ax.bar(sector_angle * i, data[0,i], width=sector_angle, label=data_labels[i])

ax.legend(bbox_to_anchor=(1.1,1), loc="upper left", ncol=1, labels=data_labels, fontsize=10)
ax.set_title('Number of Retail Stores Selling Different Products in 2021', fontsize=14)
ax.set_xticks(np.linspace(0,2*np.pi,num_categories,endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, rotation=0, wrap=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_127.png')
plt.clf()