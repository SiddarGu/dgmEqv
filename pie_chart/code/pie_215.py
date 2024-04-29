
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# set up figure size
fig = plt.figure(figsize=(7,7))

# create subplot and labels
ax = fig.add_subplot(111)
labels = ["Hydroelectric","Solar","Wind","Nuclear","Natural Gas","Oil"]

# data
energy_sources = [20,20,20,20,15,5]

# plotting
ax.pie(energy_sources, labels=labels,autopct='%1.1f%%', startangle=90)

# title
plt.title("Percentage of Energy Sources in the USA, 2023")

#rotate x ticks
ax.xaxis.set_major_locator(ticker.MultipleLocator(90))

# resize the image
plt.tight_layout()

# save 
plt.savefig("pie chart/png/1.png")

# clear current image state
plt.clf()