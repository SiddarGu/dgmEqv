
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[100,200,50,30], [120,250,60,35], [140,300,80,40], [160,350,90,45], [140,400,100,50], [120,350,90,45], [100,300,80,40], [90,250,60,35]])

# set figure
plt.figure(figsize=(16,8))

# plot line
plt.plot(data)

# add labels
plt.xlabel('Month')
plt.ylabel('Transportation of goods')

# add title
plt.title('Transportation of goods in different ways from January to August 2023')

# add legend
plt.legend(['Truck', 'Car', 'Train', 'Airplane'], loc=2)

# add grid
plt.grid(True)

# add xticks
plt.xticks(np.arange(8), ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'))

# add annotation
for i in range(8):
    for j in range(4):
        plt.annotate(data[i][j], (i, data[i][j]))

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('line chart/png/386.png')

# clear current image state
plt.cla()