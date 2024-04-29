import matplotlib.pyplot as plt
import numpy as np

# Process data
data_string = 'Year,Grains (Million Metric Tons),Vegetables (Million Metric Tons),Fruits (Million Metric Tons),Meat (Million Metric Tons),Dairy (Million Metric Tons)/n 2010,2113,982,769,317,690/n 2011,2065,990,780,321,702/n 2012,2187,1002,791,326,714/n 2013,2239,1014,803,332,726/n 2014,2301,1027,816,339,737/n 2015,2364,1041,830,345,749/n 2016,2428,1056,844,351,762/n 2017,2492,1072,859,358,776/n 2018,2557,1089,876,365,790/n 2019,2623,1107,894,373,804'
data = []
line_labels = []
data_labels = data_string.split("/n")[0].split(",")[1:]
for row in data_string.split("/n")[1:]:
    line = row.split(",")
    line_labels.append(int(line[0]))
    data.append([int(num) for num in line[1:]])

data = np.array(data)

# Create plot
fig = plt.figure(figsize=(20, 15))

ax1 = fig.add_subplot(111)
line1, = ax1.plot(line_labels, data[:, 0], color = 'tab:blue',label=data_labels[0])
ax1.set_ylabel(data_labels[0], color = 'tab:blue')

# Create the second plot on the same x-axis
ax2 = ax1.twinx()
line2, = ax2.plot(line_labels, data[:, 1], color = 'tab:orange' ,label=data_labels[1])
ax2.set_ylabel(data_labels[1], color = 'tab:orange')

# Create the third plot on the same x-axis
ax3 = ax1.twinx()
line3, = ax3.plot(line_labels, data[:, 2], color ='tab:green', label=data_labels[2])
ax3.spines["right"].set_position(("axes", 1.1))
ax3.set_ylabel(data_labels[2], color ='tab:green')

# Create the fourth plot on the same x-axis
ax4 = ax1.twinx()
line4, = ax4.plot(line_labels, data[:, 3], color ='tab:red', label=data_labels[3])
ax4.spines["right"].set_position(("axes", 1.2))
ax4.set_ylabel(data_labels[3], color ='tab:red')

# Create the fifth plot on the same x-axis
ax5 = ax1.twinx()
line5, = ax5.plot(line_labels, data[:, 4], color ='tab:purple', label=data_labels[4])
ax5.spines["right"].set_position(("axes", 1.3))
ax5.set_ylabel(data_labels[4], color ='tab:purple')

plt.title("Progression of Global Agricultural and Food Production from 2010 to 2019")

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/162_202312310108.png')
plt.clf()
