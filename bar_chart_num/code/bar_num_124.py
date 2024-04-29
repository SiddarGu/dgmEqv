

import matplotlib.pyplot as plt
import numpy as np

# Plot the data with the type of Bar Chart
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

data = np.array([[14000, 9500, 2500],
                 [18000, 11000, 3000],
                 [16000, 10000, 3500],
                 [19000, 13000, 4000]])

primary_schools = np.array([14000, 18000, 16000, 19000])
secondary_schools = np.array([9500, 11000, 10000, 13000])
universities = np.array([2500, 3000, 3500, 4000])

ind = np.arange(len(primary_schools))
width = 0.3

primary_bar = ax.bar(ind, primary_schools, width, color='#ff7f50', label='Primary Schools')
secondary_bar = ax.bar(ind + width, secondary_schools, width, color='#87ceeb', label='Secondary Schools')
universities_bar = ax.bar(ind + 2 * width, universities, width, color='#da70d6', label='Universities')

ax.set_title("Number of primary schools, secondary schools and universities in four countries in 2021")
ax.set_xticks(ind + width)
ax.set_xticklabels(('USA', 'UK', 'Germany', 'France'))
ax.legend()

# Annotate the value of each data point for every variables directly on the figure
def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

autolabel(primary_bar, "center")
autolabel(secondary_bar, "center")
autolabel(universities_bar, "center")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('Bar Chart/png/325.png')

# Clear the current image state
plt.clf()