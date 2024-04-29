
import matplotlib.pyplot as plt
import numpy as np

#set data 
x = np.array([2018, 2019, 2020, 2021, 2022, 2023]) 
y1 = np.array([10,12,14,16,18,20]) 
y2 = np.array([1,2,3,4,5,6]) 
y3 = np.array([5,7,9,11,13,15])

# create figure
fig = plt.figure(figsize=(10,6))

# create subplot 
ax = fig.add_subplot(111)

# plot line chart
ax.plot(x, y1, color = 'green', marker='o', linestyle='--',label='Car Sales(million)') 
ax.plot(x, y2, color = 'blue', marker='o', linestyle='--',label='Train Sales(million)') 
ax.plot(x, y3, color = 'red', marker='o', linestyle='--',label='Bike Sales(million)')

# set title 
ax.set_title('Sales of Cars, Trains and Bikes Worldwide from 2018-2023')

# set x and y labels 
ax.set_xlabel('Year') 
ax.set_ylabel('Sales (million)') 


# add grids
ax.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='both',alpha=0.4)

# set legend
ax.legend(loc='upper left')

#save image
fig.tight_layout()
plt.savefig('line_166.png')

# clear image
plt.clf()