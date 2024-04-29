
import matplotlib.pyplot as plt
import numpy as np

#restructure data into two 2D lists
data_list1 = [[30,90,150,210,300], [45,75,130,190,280], [60,120,180,240,320], [15,60,100,140,200], [20,50,90,130,170]]
data_list2 = [[], [400], [10,15], [300], [320]]
line_labels = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
#draw and save a chart
plt.figure(figsize=(10,6)) #create figure
ax = plt.subplot() #add_subplot
ax.boxplot(data_list1, whis=1.5) #plot box plot

#plot outliers
for i, outlier in enumerate(data_list2):
    if len(outlier) > 0:
        ax.plot(np.repeat(i + 1, len(outlier)), outlier, 'ro')

ax.grid(linestyle='dotted') #draw background grids

#set title, x-axis and y-axis
ax.set_title('Sales Revenue Distribution in Retail Stores (2020)')
ax.set_xlabel('Retail Store')
ax.set_xticklabels(line_labels)
ax.set_ylabel('Sales Revenue (dollars)')

#resize and save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/42_202312270030.png')

#clear the current image state
plt.clf()