
import matplotlib.pyplot as plt
import numpy as np

# set data
orgs = ['Red Cross','UNICEF','World Food Program','Global Fund']
income = [25,30,20,15]
expenditure = [12,14,16,18]

# create figure and plot data
fig = plt.figure()
ax = fig.add_subplot()
width = 0.4
x = np.arange(4)
ax.bar(x - width/2, income, width, label='Income')
ax.bar(x + width/2, expenditure, width, label='Expenditure')

# setting labels, title, legend
ax.set_ylabel('Value(million)')
ax.set_title('Financial performance of four charity organizations in 2021')
ax.set_xticks(x)
ax.set_xticklabels(orgs)
ax.legend()

# add value labels
for i in range(4):
    ax.annotate(str(income[i]), (x[i] - width/2, income[i]+1), rotation=90)
    ax.annotate(str(expenditure[i]), (x[i] + width/2, expenditure[i]+1), rotation=90)

#resize the image and save
fig.tight_layout()
fig.set_figwidth(10)
fig.set_figheight(7)
plt.savefig("Bar Chart/png/347.png")
plt.clf()