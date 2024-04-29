import matplotlib.pyplot as plt
import random

# define data 
companies = ["Company A", "Company B", "Company C", "Company D", "Company E"]
data_stats = [[2, 6, 9, 12, 16], [1, 4, 7, 11, 15], [3, 7, 10, 13, 18], [2, 5, 8, 11, 15], [1, 6, 9, 12, 17]]
data_outliers = [[], [0.5,17], [19], [20], [0.2,18]]

# create figure and add subplot
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

# box plot
bp = ax.boxplot(data_stats, notch=True, vert=True, patch_artist=True, whis=1.5)

# color for each box
colors = ['#D7191C', '#FDAE61', '#ABDDA4', '#2B83BA', '#FFFFBF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
# changing color and line width of whiskers 
for whisker in bp['whiskers']: 
    whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =":") 

# changing color and line width of caps 
for cap in bp['caps']: 
    cap.set(color ='#8B008B', linewidth = 2) 

# changing color and line width of medians 
for median in bp['medians']: 
    median.set(color ='black', linewidth = 3)

# outliers manually
for i, outlier in enumerate(data_outliers):
    ax.plot([i + 1] * len(outlier), outlier, 'x', color="black")

# setting labels 
ax.set_xticklabels(companies, rotation = 15, wrap=True)
ax.set_xlabel('Food Company')
ax.set_ylabel('Processing Time (Days)')

ax.grid(True)
ax.set_title("Product Processing Time Distribution in Food Companies (2025)")

plt.tight_layout()

# save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/219_202312310058.png")

# clear the figure
plt.clf()
