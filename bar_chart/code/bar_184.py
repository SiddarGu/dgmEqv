
import matplotlib.pyplot as plt
import matplotlib as mpl

# set figure size
fig = plt.figure(figsize=(8,5)) 

# get data
year = [2020, 2021, 2022, 2023]
renewable_energy = [20000, 23000, 26000, 29000]
fossil_fuel = [40000, 45000, 50000, 55000]

# draw the bar chart
ax = fig.add_subplot()
ax.bar(year, renewable_energy, width=0.4, label="Renewable Energy Production(MWh)")
ax.bar(year, fossil_fuel, width=0.4, bottom=renewable_energy, label="Fossil Fuel Production(MWh)")

# set the title
plt.title("Renewable and Fossil Fuel Production in the Years 2020-2023")

# set the size of the x and y axis
plt.xticks(year, rotation=10, wrap=True) 
plt.yticks(range(0, 70000, 5000))

# set the background grid
plt.grid(axis="y", alpha=0.6)

# set the legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=2)

# adjust the display
plt.tight_layout()

# save the image
plt.savefig("bar chart/png/50.png")

# clear the current image state
plt.clf()