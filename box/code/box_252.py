import matplotlib.pyplot as plt
import seaborn as sns

# restructure the data
data = [ ['Logistics Van',[3,6,8,10,12],[]], ['Semi-Truck',[4,8,12,16,20],[1,24]], ['Cargo Train',[10,15,20,25,30],[40,50]], ['Air Freight',[1,2,3,4,5],[6,7]], ['Ocean Frieght',[50,75,100,125,150],[200]] ]

category = [x[0] for x in data]
values = [x[1] for x in data]
outliers = [x[2] for x in data]

# plotting
fig = plt.figure(figsize=(12, 6)) 
ax = fig.add_subplot(111) 

bp = ax.boxplot(values, notch=0, vert=1, patch_artist=True, whis=1.5)
colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#006400']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "ro")

# modify axes
ax.set(title='Delivery Time Distribution for Transportation Vehicles in the Logistics Industry (2022)',
       xlabel='Vehicle Type',
       ylabel='Delivery Time (Hours)')
ax.set_xticklabels(category, rotation=90)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)

# save and clear
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/134_202312270030.png')
plt.close(fig)
