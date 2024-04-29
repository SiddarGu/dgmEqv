
import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(10,6))

# add subplot
ax = fig.add_subplot()

# define data
months = np.array(['January','February','March','April','May'])
bakery_sales = np.array([100,120,150,180,130])
produce_sales = np.array([200,220,210,230,190])
grocery_sales = np.array([250,280,270,300,290])
beverage_sales = np.array([400,450,420,350,400])

# plot lines
ax.plot(months, bakery_sales, linewidth=2, label='Bakery sales(million pounds)')
ax.plot(months, produce_sales, linewidth=2, label='Produce sales(million pounds)')
ax.plot(months, grocery_sales, linewidth=2, label='Grocery sales(million pounds)')
ax.plot(months, beverage_sales, linewidth=2, label='Beverage sales(million pounds)')

# set labels
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Sales(million pounds)', fontsize=14)

# set title
plt.title('Monthly sales of food and beverage products in the US, 2021', fontsize=18)

# display grid
plt.grid()

# set ticks
plt.xticks(months)

# set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=4, fancybox=True, shadow=True, fontsize=14)

# resize image
plt.tight_layout()

# save image
plt.savefig('line chart/png/334.png')

# clear current image state
plt.clf()