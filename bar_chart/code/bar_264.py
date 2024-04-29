
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
x_data = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']
y_data1 = [10, 9, 12, 11]
y_data2 = [8, 9, 7, 10]
y_data3 = [12, 13, 14, 15]
ax.bar(x_data, y_data1, width=0.25, color='b', label='Air Transport(million)')
ax.bar(x_data, y_data2, width=0.25, bottom=y_data1, color='r', label='Rail Transport(million)')
ax.bar(x_data, y_data3, width=0.25, bottom=[i+j for i, j in zip(y_data1, y_data2)], color='g', label='Road Transport(million)')
ax.set_title('Transportation and Logistics in four cities in 2021', fontsize=16)
ax.set_xlabel('City')
ax.set_ylabel('Transport(million)')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fancybox=True, shadow=True)
plt.xticks(x_data, rotation=45)
plt.tight_layout()
plt.savefig('bar chart/png/411.png')
plt.clf()