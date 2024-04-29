
import matplotlib.pyplot as plt
import numpy as np

#set figure size
plt.figure(figsize=(10, 6))

#create subplot
ax = plt.subplot()

#generate data
x_data = np.arange(2016, 2020, 1)

y_data_1 = [5000, 4500, 5500, 6000]
y_data_2 = [350, 320, 400, 420]
y_data_3 = [20, 22, 24, 26]

#plot line chart
ax.plot(x_data, y_data_1, label='Crop Yield(tons)', marker='o', color='#67d3f3',linestyle='--', linewidth=2)
ax.plot(x_data, y_data_2, label='Average Rainfall(mm)', marker='s', color='#ff0000',linestyle='--', linewidth=2)
ax.plot(x_data, y_data_3, label='Average Temperature(degrees)', marker='*', color='#00ff00',linestyle='--', linewidth=2)

#set title
ax.set_title("Crop yield and climate conditions in the US Midwest region from 2016-2019")

#set xticks
ax.set_xticks(x_data)

#add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, fancybox=True, shadow=True, fontsize=12)

#set label
ax.set_xlabel('Year')
ax.set_ylabel('Values')

#automatically resize the image by tight_layout
plt.tight_layout()

#save the figure
plt.savefig('line chart/png/173.png')

#clear the current image state
plt.cla()
plt.clf()
plt.close()