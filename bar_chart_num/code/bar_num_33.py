
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 230, 450],
        ['UK', 200, 400],
        ['Germany', 180, 380],
        ['France', 220, 450]]

labels, mobile, broadband = zip(*data)

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10,5))
rects1 = ax.bar(x - width/2, mobile, width, label='Mobile devices')
rects2 = ax.bar(x + width/2, broadband, width, label='Broadband connections')

ax.set_ylabel('Counts')
ax.set_title('Number of mobile devices and broadband connections in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='upper right')

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')

autolabel(rects1, "left")
autolabel(rects2, "right")

fig.tight_layout()

plt.savefig("Bar Chart/png/380.png")
plt.clf()