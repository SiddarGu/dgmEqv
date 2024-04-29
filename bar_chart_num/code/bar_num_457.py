
import matplotlib.pyplot as plt
import numpy as np

Region = [ 'North East', 'South East', 'South West', 'North West' ] 
Total_Houses = [ 400, 500, 450, 380 ]
Average_Price = [ 20000, 25000, 22000, 19000 ]

x = np.arange(len(Region)) 
width = 0.35 

fig, ax = plt.subplots(figsize=(10,6))
rects1 = ax.bar(x - width/2, Total_Houses, width, label='Total Houses', color='orange')
rects2 = ax.bar(x + width/2, Average_Price, width, label='Average Price', color='lightblue')

ax.set_title('Total number of houses and average price in four regions in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Region)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=0, wrap=True)
autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
plt.savefig('Bar Chart/png/368.png')
plt.clf()