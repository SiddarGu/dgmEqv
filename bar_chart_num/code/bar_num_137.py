
import matplotlib.pyplot as plt
import numpy as np

#Preparing data
country =  np.array(['USA','China','UK','Japan'])
investment = np.array([5.2,4.1,3.2,2.9])
income = np.array([8.0,7.5,6.8,6.2])

#Create figure
fig = plt.figure()
ax = fig.add_subplot()

#Plot data
ax.bar(country,investment,label='Investment', bottom=0, color='skyblue')
ax.bar(country,income, label='Income', bottom=investment, color='orange')

#Label data
for i, v in enumerate(investment):
    ax.text(i, v/2, str(v)+'bn', color='white', va='center', fontweight='bold')
for i, v in enumerate(income):
    ax.text(i, investment[i]+v/2, str(v)+'bn', color='white', va='center', fontweight='bold')

#Configure figure
ax.set_title('Investment and Income from four Countries in 2021')
ax.set_xticks(np.arange(len(country)))
ax.set_xticklabels(country)
ax.set_xlabel('Country')
ax.legend(loc='upper left')
ax.grid(axis="y")

#Adjust figure size
fig.set_figheight(7)
fig.set_figwidth(10)
fig.tight_layout()

#Save figure
plt.savefig('Bar Chart/png/385.png')

#Clear figure
plt.cla()