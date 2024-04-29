
import matplotlib.pyplot as plt
import numpy as np

# create figure
fig = plt.figure(figsize=(10,6))

# extract data
Country = ["USA","Canada","Mexico","Brazil"]
Crops = [50, 40, 60, 45]
Livestock = [25, 20, 30, 35]

# set bar chart
index = np.arange(len(Country))
bar_width = 0.35

rects1 = plt.bar(index, Crops, bar_width, color='#87ceeb', label='Crops')
rects2 = plt.bar(index + bar_width, Livestock, bar_width, color='#ffa07a', label='Livestock')

# set label
plt.xlabel('Country')
plt.ylabel('Production')
plt.title('Crop and Livestock Production in Four Countries in 2021')
plt.xticks(index + bar_width/2, Country)
plt.legend()

# add value label
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

# adjust figure
plt.tight_layout()

# save figure
plt.savefig('Bar Chart/png/582.png')

# clear current figure
plt.clf()