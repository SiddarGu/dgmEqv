
import matplotlib.pyplot as plt

# set the figure size
plt.figure(figsize=(10, 6))

# set the legend position
plt.legend(loc="upper left")

# set the title of the figure
plt.title("Cultural Institutions in Four Major Countries")

# draw the line chart
plt.plot(["USA", "UK", "Canada", "France"], [3000, 2000, 2500, 3500], label="Museums")
plt.plot(["USA", "UK", "Canada", "France"], [5000, 4000, 4500, 5500], label="Galleries")
plt.plot(["USA", "UK", "Canada", "France"], [7000, 6000, 6500, 7500], label="Libraries")

# set the label of the x-axis
plt.xlabel("Country")

# set the label of the y-axis
plt.ylabel("Number of Cultural Institutions")

# show the ticks of the x-axis
plt.xticks(rotation=30, wrap=True)

# display the legend
plt.legend()

# adjust the figure size to prevent content from being displayed
plt.tight_layout()

# save the figure
plt.savefig("line chart/png/454.png")

# clear the current image state
plt.clf()