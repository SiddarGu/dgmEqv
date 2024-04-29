
import matplotlib.pyplot as plt
import numpy as np

# data
state = ["Florida","California","Texas","New York"]
Hydroelectricity = [0.8, 1.2, 1.0, 0.9]
Nuclear = [1.2, 1.5, 1.7, 1.4]
Solar = [0.4, 0.5, 0.6, 0.7]

# create figure
fig = plt.figure(figsize=(10, 6))

# define bar chart
x = np.arange(len(state))  # the label locations
width = 0.2  # the width of the bars

# stacked bar chart
rects1 = plt.bar(x - width, Hydroelectricity, width, label='Hydroelectricity')
rects2 = plt.bar(x, Nuclear, width, label='Nuclear')
rects3 = plt.bar(x + width, Solar, width, label='Solar')

# add title and labeling
plt.title("Energy output from Hydroelectricity, Nuclear and Solar sources in four states in 2021")
plt.xlabel('State')
plt.ylabel('Energy(billion kWh)')
plt.xticks(x, state)
plt.legend(loc="upper right")

plt.tight_layout()

# annotate the value of each data point
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=0)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# save figure
plt.savefig("Bar Chart/png/16.png")

# clear current image state
plt.clf()