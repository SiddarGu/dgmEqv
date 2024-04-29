
import matplotlib.pyplot as plt
import numpy as np

#prepare data
x = np.array([2001, 2002, 2003, 2004])
y1 = np.array([10, 12, 14, 15])
y2 = np.array([20, 22, 25, 27])
y3 = np.array([30, 33, 36, 39])

#create figure
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

#plot
ax.plot(x, y1, label='Prevalence of Disease A(%)', marker='o', color='b')
ax.plot(x, y2, label='Prevalence of Disease B(%)', marker='o', color='r')
ax.plot(x, y3, label='Prevalence of Disease C(%)', marker='o', color='g')

#add title and legend
plt.title('Increase in prevalence of three diseases in the United States from 2001 to 2004')
ax.legend(loc='best')

#label each data point
for i, txt in enumerate(y1):
    ax.annotate(txt, (x[i], y1[i]), ha='center', va='bottom', color='b')
for i, txt in enumerate(y2):
    ax.annotate(txt, (x[i], y2[i]), ha='center', va='bottom', color='r')
for i, txt in enumerate(y3):
    ax.annotate(txt, (x[i], y3[i]), ha='center', va='bottom', color='g')

#set x ticks
plt.xticks(x)

#adjust layout
plt.tight_layout()

#save image
plt.savefig("line chart/png/59.png")

#clear current image
plt.clf()