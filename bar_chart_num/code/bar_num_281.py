
import matplotlib.pyplot as plt
import numpy as np

country = ['USA','UK','Germany','France']
average_production = [2000,1800,1700,1500]

# create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# plot the data
ax.bar(country, average_production, color=['#4286f4','#44c7f4','#46dcf4','#47f3f4'])

# labels & titles
ax.set_title('Average Production Output of Four Countries in 2021')
ax.set_ylabel('Average Production (million)')
ax.set_xticklabels(country, rotation=45)

# add values to each bar
for x,y in zip(country,average_production):
    label = y
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center', wrap=True) # horizontal alignment can be left, right or center

plt.tight_layout()

# save
plt.savefig('Bar Chart/png/129.png', dpi=300)

# clear the current image state
plt.clf()