import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
import matplotlib

# Prepare data
raw_data = """
Platform,Active Users (Billions),Daily Time Spent (Minutes),Profit (Billion $),User Satisfaction (Score)
Facebook,2.8,58,29.5,80
YouTube,2.0,40,15.1,85
Instagram,1.3,53,20.5,90
Twitter,0.33,31,3.4,80
LinkedIn,0.76,10,2.7,70
Snapchat,0.53,26,5.1,75"""
lines = raw_data.split('\n')[2:-1]
data_labels = np.array(raw_data.split('\n')[1].split(','))[1:]
line_labels = [line.split(',')[0]+', '+line.split(',')[-2] for line in lines]
data = np.array([list(map(float,line.split(',')[1:])) for line in lines])

# Normalize color and size values
norm = Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
cmap = get_cmap('viridis')
norm_size = Normalize(vmin=min(data[:,2]), vmax=max(data[:,2]))

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plotting
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], color=cmap(norm(data[i, 3])), s=600 + 4400*norm_size(data[i, 2]), edgecolors='black', linewidth=0.5)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_labels[i])
    
# Legend and color bar
ax.legend(title=data_labels[2], loc='upper left')
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

# Titles and labels    
ax.set_title('Social Media Platforms: User Engagement and Profit Analysis')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Display and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/231_202312310045.png')
plt.show()

plt.clf()
