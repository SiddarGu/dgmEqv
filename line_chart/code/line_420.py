
import matplotlib.pyplot as plt
import numpy as np

# data
x = np.arange(1, 6) # Month
Price_A = [20, 25, 22, 30, 27]
Price_B = [30, 35, 32, 40, 37]
Price_C = [18, 20, 15, 20, 17]
Price_D = [25, 30, 27, 35, 32]

# create figure
plt.figure(figsize=(10,6))

# create a subplot
ax=plt.subplot()

# plot the data
ax.plot(x, Price_A, color='red', marker='o', label='Price A')
ax.plot(x, Price_B, color='blue', marker='o', label='Price B')
ax.plot(x, Price_C, color='green', marker='o', label='Price C')
ax.plot(x, Price_D, color='black', marker='o', label='Price D')

# set x ticks
ax.set_xticks(x)

# setting the limit of x axis
ax.set_xlim(1, 5)

# setting the grid
ax.grid(linestyle='--', alpha=0.5)

# set the title
ax.set_title('Average prices of four food items in the US in 2021')

# set the xlabel and ylabel
ax.set_xlabel('Month')
ax.set_ylabel('Price (dollars)')

# set the legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# tight the layout
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/546.png')

# clear the current figure
plt.clf()