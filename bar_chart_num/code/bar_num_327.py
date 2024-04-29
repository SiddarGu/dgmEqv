
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig = plt.figure()
ax = fig.add_subplot(111)

#Set the x-axis
Region = ['North America', 'South America', 'Europe', 'Asia']
x_pos = np.arange(len(Region))

#Set the y-axis
Sports_Fans = [200, 180, 230, 270]
Entertainment_Fans = [600, 550, 510, 480]

#Draw the figure
ax.bar(x_pos, Sports_Fans, color='lightblue', edgecolor='black', width=0.6, label='Sports Fans')
ax.bar(x_pos, Entertainment_Fans, bottom=Sports_Fans, color='orange', edgecolor='black', width=0.6, label='Entertainment Fans')

#Set the title and x-axis label
ax.set_title('Number of sports and entertainment fans in four regions in 2021', fontsize=20, fontweight='bold')
ax.set_xlabel('Region', fontsize=15, fontweight='bold')

#Set the xticks
ax.set_xticks(x_pos)
ax.set_xticklabels(Region, fontsize=12)

#Set the legend
ax.legend(loc='upper right', fontsize=15)

#Set the grid
ax.grid(linestyle='--', linewidth=1)

#Label each bar
for x,y1,y2 in zip(x_pos, Sports_Fans, Entertainment_Fans):
    ax.annotate(f'{y1}', xy=(x, y1), ha='center', va='bottom', fontsize=12)
    ax.annotate(f'{y2}', xy=(x, y1+y2/2), ha='center', va='bottom', fontsize=12)

#Set the figsize and resize the image
fig.set_figwidth(10)
fig.set_figheight(8)
plt.tight_layout()

#Save the image
plt.savefig(r'Bar Chart/png/273.png')

#Clear the current image state
plt.clf()