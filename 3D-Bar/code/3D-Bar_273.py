import numpy as np
import matplotlib.pyplot as plt

# initial data
data_str = "Year,Number of Cases (Thousands),Conviction Rate (%),Acquit Rate (%),Pending Cases (Thousands)\
/n 2015,295,45,25,325/n 2016,300,48,22,330/n 2017,320,50,20,340/n 2018,350,52,18,370/n 2019,375,53,17,400"
data_str = data_str.replace(' ', '').replace("/n","\n")
data_ = [row.split(',') for row in data_str.split('\n')]

# creating numpy array    
data = np.array(data_)
y_values = data[0, 1:].astype(str).tolist() # excluding first column as it's Years
x_values = data[1:, 0].astype(str).tolist() # excluding first row as it's Headers
data = data[1:, 1:].astype(np.float32) # the numerical data to be plotted

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r','g','b','m'] # colors for distinct bars

# iterating over each column of data to be plotted
for c in range(data.shape[1]):
    xs = np.arange(len(x_values))
    ys = data[:,c]
    ax.bar(xs, ys, c, zdir='y', color=colors[c % len(colors)], alpha=0.8)

# Setting labels and other visual enhancements
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')
ax.set_zlabel('Z')
ax.set_title('Analysis of Legal Cases and Outcomes from 2015 to 2019')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/265_202312310050.png')
plt.cla() # to clear the current image
