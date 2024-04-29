
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,6))

# set the x-axis
x_axis=['2018','2019','2020','2021','2022']
# set the y-axis
y_axis=[130,150,80,140,160]
# set the y-axis
z_axis=[4.5,5.2,2.6,4.8,6.3]

# draw line chart
plt.plot(x_axis, y_axis, label='Attendance', color='green', marker='o')
plt.plot(x_axis, z_axis, label='Revenue', color='blue', marker='o')

# set title
plt.title('Attendance and Revenue of Major Sporting Events from 2018 to 2022')
# set labels
plt.xlabel('Year')
plt.ylabel('Values')

# set legend
plt.legend(loc='upper right')

# set x ticks
plt.xticks(x_axis, rotation=0, wrap=True)

# set grid
plt.grid(axis='y', linestyle='--', color='gray', linewidth=0.5)

# adjust the image size
plt.tight_layout()

# save and show the figure
plt.savefig('./line chart/png/276.png')
plt.show()

# clear the current image state 
plt.clf()