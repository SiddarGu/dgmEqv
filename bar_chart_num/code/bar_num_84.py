
import matplotlib.pyplot as plt
import numpy as np

# create figure before plotting
fig, ax = plt.subplots(figsize=(10, 8))

# define parameters
x = np.arange(4)
hospitals = [800, 650, 750, 700]
doctors = [4500, 4000, 4250, 4750]
nurses = [9000, 8000, 8500, 9000]
labels = ['USA', 'UK', 'Germany', 'France']

# set the bar chart
ax.bar(x, hospitals, label='Hospitals', bottom=0)
ax.bar(x, doctors, label='Doctors', bottom=np.array(hospitals))
ax.bar(x, nurses, label='Nurses', bottom=np.array(hospitals)+np.array(doctors))

# set the title
plt.title('Number of hospitals, doctors, and nurses in four countries in 2021')

# set the legend
plt.legend(loc='best')

# set the x ticks
plt.xticks(x, labels)

# set the font size
plt.tick_params(labelsize=11)

# label the value of each data point for every variables
for xpos, ypos, yval in zip(x, hospitals, hospitals):
    ax.text(xpos, ypos + 10, yval, ha='center', va='top')
for xpos, ypos, yval in zip(x, [sum(i) for i in zip(hospitals, doctors)], doctors):
    ax.text(xpos, ypos + 10, yval, ha='center', va='top')
for xpos, ypos, yval in zip(x, [sum(i) for i in zip(hospitals, doctors, nurses)], nurses):
    ax.text(xpos, ypos + 10, yval, ha='center', va='top')

# automatically resize the image
plt.tight_layout()

# save image
plt.savefig('Bar Chart/png/344.png')

# clear the current image state
plt.clf()