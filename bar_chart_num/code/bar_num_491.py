
import matplotlib.pyplot as plt

x = ['Facebook','Twitter','Instagram','TikTok']
y1 = [2.85,380,1.2,800]
y2 = [1.85,340,1.1,750]

fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111)
ax.bar(x,y1,width=0.4, color='g', label='Monthly Users(million)')
ax.bar(x,y2,width=0.4, bottom=y1, color='r', label='Daily Active Users(million)')
ax.set_title('Monthly and daily active users of popular social media platforms in 2021')
ax.set_xticklabels(x, rotation=45, ha='right')
ax.set_ylabel('Users (million)')
ax.set_xlabel('Platform')
ax.legend(loc='upper left')

# annotate value of each data point for every variables directly on the figure.
for i, v in enumerate(y1):
    ax.text(i , v + 10, str(round(v,2)), ha='center', va='bottom', fontsize=10)

for i, v in enumerate(y2):
    ax.text(i , v + 10 + y1[i], str(round(v,2)), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
# save the figure
plt.savefig('Bar Chart/png/230.png')

# clear the current image state
plt.clf()