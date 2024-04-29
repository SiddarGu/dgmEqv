import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Tennis\n Championship", 
              "Soccer\n League", 
              "Baseball\n Game", 
              "Music\n Festival", 
              "Movie\n Premiere"]

ticket_summary = [[20, 50, 95, 150, 260],
                  [10, 35, 85, 130, 210],
                  [15, 45, 80, 120, 190],
                  [40, 70, 120, 170, 240],
                  [25, 60, 100, 140, 200]]

outliers = [[], [285], [5, 235], [10, 330], [5, 350]] 

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

bp = ax.boxplot(ticket_summary, vert=False, patch_artist=True, notch=True, whis=1.5, widths = 0.4)
colors = ['#f7b2b2', '#b2c2f7', '#b2f7ce', '#f7edb2', '#d5b2f7']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Outliers
for i, outlier in enumerate(outliers):
    if outlier: 
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# Formatting
ax.yaxis.grid(False)
ax.xaxis.grid(True)
ax.set_title('Ticket Price Distribution for Sports and Entertainment Events in 2022')
ax.set_xlabel('Ticket Price ($)')
ax.set_yticklabels(categories)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/145_202312270030.png')
plt.clf()  
