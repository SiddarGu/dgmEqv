
import matplotlib.pyplot as plt
import numpy as np

x = ['Facebook','Instagram','Twitter','Snapchat']
y = np.array([[2.5,1.2,0.8,0.5],[50,40,30,20]]) 

fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot()
ax.bar(x, y[0], label='Users(million)', bottom=0, width=0.4)
ax.bar(x, y[1], label='Engagement(% of users)', bottom=y[0], width=0.4)

ax.set_title('Social media users and engagement percentage in 2021')
ax.set_xticks(x)
ax.set_xlabel('Platform')
ax.set_ylabel('Number(million) & Percentage(%)')
ax.legend()

for i in range(len(x)):
    ax.annotate(str(y[0][i])+"("+str(y[1][i])+"%)", xy=(x[i], y[0][i]+y[1][i]/2))

plt.tight_layout()
plt.savefig("Bar Chart/png/520.png")
plt.clf()