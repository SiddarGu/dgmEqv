
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,5))
plt.title('Hours worked and salary of four employees in 2021')

employee=['John','Jane','Jack','Jill']
hours_worked=[40,50,45,48]
salary=[1000,1200,1100,1050]

ax=fig.add_subplot()
rects1=ax.bar(employee,hours_worked,width=.4,color='orange',label='Hours worked')
rects2=ax.bar(employee,salary,width=.4,bottom=hours_worked,color='green',label='Salary')

plt.xticks(employee)
ax.legend(loc='upper left')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom',wrap=True)

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.savefig('Bar Chart/png/184.png')
plt.clf()