import matplotlib.pyplot as plt
import numpy as np

# Restructuring the data 
positions = ['Manager', 'Engineer', 'Sales', 'HR Specialist', 'Analyst']
data = [[50,70,90,110,130], [40,60,80,100,120], [30,50,70,90,110], [35,55,75,95,115], [45,65,85,105,125]]
outliers = [[], [150], [130,140], [20,23], [140,150]]

fig = plt.figure(figsize=(10,7)) 
ax = fig.add_subplot(111)

# Creating axes instance 
bp = ax.boxplot(data, vert=0, patch_artist=True, notch=True, whis=1.5, 
                 positions=np.arange(len(data))+1, widths=0.6)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Changing color and line width of whiskers 
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =":")

# Changing color and linewidth of caps 
for cap in bp['caps']:
    cap.set(color ='#8B008B', linewidth = 2)

# Changing color and linewidth of medians 
for median in bp['medians']:
    median.set(color ='red', linewidth = 3)

# Changing style of fliers 
for flier in bp['fliers']:
    flier.set(marker ='D', color ='#e7298a', alpha = 0.5)
  
# Plotting outliers manually    
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i+1]*len(outlier), 'ro')

# x-axis labels 
ax.set_yticklabels(positions)

# Adding title  
plt.title("Salary Distribution Across Different Positions in Human Resources and Employee Management (2021)") 

# Removing top axes and right axes 
ax.get_xaxis().tick_bottom() 
ax.get_yaxis().tick_left() 

ax.set_xlabel('Salary (Thousands)')
plt.xticks(rotation=90)
plt.grid()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/61_202312270030.png')

# Clear the current figure's content
plt.clf()
