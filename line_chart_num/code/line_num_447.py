
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(20, 10))

x = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August', 'September'] 
attendance = [750, 800, 900, 1000, 850, 900, 950, 800, 750] 
income = [20, 25, 30, 35, 40, 45, 50, 60, 70]

ax.plot(x, attendance, color='b', marker='o', linestyle='--', label='Attendance') 
ax.plot(x, income, color='r', marker='o', linestyle='--', label='Income') 
  
for x_, y_ in zip(x, attendance): 
    label = "{:.0f}".format(y_)
    ax.annotate(label, (x_, y_), textcoords="offset points", xytext=(0,10), ha='center')

for x_, y_ in zip(x, income): 
    label = "{:.0f}".format(y_)
    ax.annotate(label, (x_, y_), textcoords="offset points", xytext=(0,10), ha='center')
    
ax.set_title('Attendance and Income of Major Sports Events in 2021') 
ax.set_xlabel('Month') 
ax.set_ylabel('Attendance/Income') 
ax.legend(loc='lower right')
ax.set_xticks(x)
plt.tight_layout() 
plt.savefig('line chart/png/373.png') 
plt.clf()