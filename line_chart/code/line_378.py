
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(10, 8))

# set data
country = np.array(['USA', 'UK', 'Canada', 'India'])
dairy = np.array([100, 120, 130, 80])
meat = np.array([200, 180, 190, 220])
fruit = np.array([150, 130, 140, 100])

# add subplot and customize labels
ax = plt.subplot()
ax.set_xticks(np.arange(len(country)))
ax.set_xticklabels(country, rotation=45, wrap=True)

# draw line chart
ax.plot(country, dairy, label='Consumption of Dairy', color='blue')
ax.plot(country, meat, label='Consumption of Meat', color='red')
ax.plot(country, fruit, label='Consumption of Fruits and Vegetables', color='green')

# labels
ax.set_title("Dietary consumption of different food items in four countries")
ax.set_xlabel('Country')
ax.set_ylabel('Consumption')

# legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# save
plt.tight_layout()
plt.savefig('line chart/png/54.png')

# clear
plt.clf()