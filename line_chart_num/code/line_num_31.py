
import matplotlib.pyplot as plt
import numpy as np

Month=['January','February','March','April','May','June']
Facebook_Users=[2.6,2.7,2.8,2.9,3.0,3.1]
Twitter_Users=[0.3,0.5,0.7,0.9,1.0,1.2]
Instagram_Users=[0.2,0.3,0.4,0.5,0.6,0.7]

# Create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

# Plot
ax.plot(Month,Facebook_Users,label='Facebook Users(million)', marker='o', color='#3385ff', linewidth=3)
ax.plot(Month,Twitter_Users,label='Twitter Users(million)', marker='o', color='#00cc66', linewidth=3)
ax.plot(Month,Instagram_Users,label='Instagram Users(million)', marker='o', color='#ffa31a', linewidth=3)

# Annotate
for x, y in zip(Month, Facebook_Users):
    ax.annotate(y, (x, y), xytext=(0, 5), textcoords='offset points', fontsize=12, color='#3385ff')
for x, y in zip(Month, Twitter_Users):
    ax.annotate(y, (x, y), xytext=(0, 5), textcoords='offset points', fontsize=12, color='#00cc66')
for x, y in zip(Month, Instagram_Users):
    ax.annotate(y, (x, y), xytext=(0, 5), textcoords='offset points', fontsize=12, color='#ffa31a')

# Set figure properties
plt.title('Growth of Social Media User Base in the First Half of 2021')
plt.xlabel('Month')
plt.ylabel('Users')
plt.xticks(Month, rotation=60)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid()
plt.tight_layout()

#Save
plt.savefig('line chart/png/93.png')

# Clear current image state
plt.clf()