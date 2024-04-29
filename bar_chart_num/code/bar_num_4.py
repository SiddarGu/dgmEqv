
import matplotlib.pyplot as plt
import numpy as np
 
# data to plot
Grade = [1,2,3,4]
English = [80,85,90,95]
Math = [90,95,100,105]
Science = [85,90,95,100]
 
# create plot
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(Grade, English, bottom=[sum(x) for x in zip(Math, Science)], color='b',label='English')
ax.bar(Grade, Math, bottom=Science, color='g',label='Math')
ax.bar(Grade, Science, color='r',label='Science')
 
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_title('Average grades of students in English, Math and Science from Grade 1 to 4')
ax.set_xticks(Grade)
ax.legend()


plt.tight_layout()

# save the figure
plt.savefig('bar_4.png')

# clear current image state
plt.clf()