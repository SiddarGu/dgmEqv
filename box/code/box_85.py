import matplotlib.pyplot as plt

# data
utilities = ['Utility A','Utility B','Utility C','Utility D','Utility E']
data = [[200,500,700,1000,1300], [250,560,730,1080,1500], [220,520,750,950,1250], [210,510,760,1005,1290], [230,490,730,980,1320]]
outliers = [[1500,1700], [], [7,1900], [1850], [6,1720]]

# create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# create an axes instance
ax = fig.add_subplot()

# create the boxplot
bp = ax.boxplot(data, vert=0, whis=1.5)

# add outliers
for i, outlier in enumerate(outliers):
    if outlier:  
        x = [i + 1] * len(outlier)
        ax.plot(outlier, x, 'ro', markersize=8)
        
# set labels and title  
ax.set_yticklabels(utilities)
ax.set_xlabel('Energy Consumption (KWh)')
ax.set_title('Monthly Energy Consumption Distribution in Utility Companies (2021)')

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/128_202312270030.png', bbox_inches='tight')
plt.clf()  # clear current figure
