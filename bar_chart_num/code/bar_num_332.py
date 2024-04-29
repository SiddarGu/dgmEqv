
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(8,6))

# data
labels = ['USA', 'UK', 'Germany', 'France']
Hotels = [100, 120, 110, 90]
Restaurants = [150, 170, 160, 130]
Tourist_Attractions = [50, 60, 70, 80]

# plot bar chart
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, Hotels, width, label='Hotels')
rects2 = ax.bar(x, Restaurants, width, label='Restaurants')
rects3 = ax.bar(x + width, Tourist_Attractions, width, label='Tourist Attractions')

# add title and x,y label
ax.set_ylabel('Number')
ax.set_title('Number of Hotels, Restaurants and Tourist Attractions in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='upper left')

# add value label
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# adjust the figure
plt.tight_layout()

# save the figure
plt.savefig('Bar Chart/png/208.png')

# clear the current image state
plt.clf()