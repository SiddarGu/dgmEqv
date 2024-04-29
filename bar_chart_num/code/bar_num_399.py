
import matplotlib.pyplot as plt
import numpy as np

# data
Location = ['USA','UK','Germany','France']
Homes_Sold = [1000, 1100, 900, 1200]
Average_Price=[500000,470000,490000,450000]

x = np.arange(len(Location))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(11,7))

rects1 = ax.bar(x - width/2, Homes_Sold, width, label='Homes Sold', color='blue')
rects2 = ax.bar(x + width/2, Average_Price, width, label='Average Price', color='orange')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Numbers')
ax.set_title('Number of Homes Sold and Average Price in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Location)
ax.legend(loc='upper center')

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.xticks(x,Location,rotation='vertical',wrap=True)
plt.savefig('Bar Chart/png/226.png')
plt.close(fig)