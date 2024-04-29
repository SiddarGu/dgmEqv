
import matplotlib.pyplot as plt
import numpy as np

# Data
data = [[2017,200,500,400],
        [2018,210,550,450],
        [2019,220,600,500],
        [2020,230,650,550]]

# Creating figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Extracting data
years = [i[0] for i in data]
beverage = [i[1] for i in data]
grocery = [i[2] for i in data]
restaurant = [i[3] for i in data]

# Plotting
ax.plot(years, beverage, color="red", label="Beverage")
ax.plot(years, grocery, color="green", label="Grocery")
ax.plot(years, restaurant, color="blue", label="Restaurant")

# Setting ticks
ax.set_xticks(years)

# Setting title
ax.set_title("Sales of Food and Beverage Industry in the US from 2017 to 2020")

# Setting legend
ax.legend(loc="upper left")

# Labeling
ax.annotate("{}".format(beverage[0]), xy=(years[0], beverage[0]), xytext=(years[0], beverage[0] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(beverage[1]), xy=(years[1], beverage[1]), xytext=(years[1], beverage[1] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(beverage[2]), xy=(years[2], beverage[2]), xytext=(years[2], beverage[2] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(beverage[3]), xy=(years[3], beverage[3]), xytext=(years[3], beverage[3] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(grocery[0]), xy=(years[0], grocery[0]), xytext=(years[0], grocery[0] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(grocery[1]), xy=(years[1], grocery[1]), xytext=(years[1], grocery[1] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(grocery[2]), xy=(years[2], grocery[2]), xytext=(years[2], grocery[2] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(grocery[3]), xy=(years[3], grocery[3]), xytext=(years[3], grocery[3] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(restaurant[0]), xy=(years[0], restaurant[0]), xytext=(years[0], restaurant[0] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(restaurant[1]), xy=(years[1], restaurant[1]), xytext=(years[1], restaurant[1] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(restaurant[2]), xy=(years[2], restaurant[2]), xytext=(years[2], restaurant[2] + 25), rotation=45, fontsize=10)
ax.annotate("{}".format(restaurant[3]), xy=(years[3], restaurant[3]), xytext=(years[3], restaurant[3] + 25), rotation=45, fontsize=10)

# Resizing
fig.tight_layout()

# Saving
fig.savefig("line chart/png/551.png")

# Clear
plt.cla()