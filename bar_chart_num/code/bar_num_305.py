
import matplotlib.pyplot as plt
import numpy as np

# data
year = np.array([2000,2005,2010,2015])
anthropology = np.array([60,70,80,90])
psychology = np.array([80,90,100,110])
sociology = np.array([70,80,90,100])

# figure
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# plot
ax.bar(year,anthropology,label='Anthropology',bottom=psychology+sociology,width=2,color='#FFD700')
ax.bar(year,psychology,label='Psychology',bottom=sociology,width=2,color='#98FB98')
ax.bar(year,sociology,label='Sociology',width=2,color='#FFA500')

# label
for x,y in zip(year,anthropology+psychology+sociology):
    ax.annotate(y,xy=(x,y+2))

# ticks
ax.set_xticks(year)

# legend
ax.legend(loc='upper right',bbox_to_anchor=(1.2,1))

# title
ax.set_title('Number of Social Science and Humanities Publications from 2000 to 2015')

# tight_layout
plt.tight_layout()

# save
plt.savefig('Bar Chart/png/443.png')

# clear
plt.clf()