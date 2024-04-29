
import matplotlib.pyplot as plt
import numpy as np

data = [[2001,20,10],
        [2002,25,12],
        [2003,30,15],
        [2004,35,20],
        [2005,40,25]]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

x_label = [i[0] for i in data]
y_highschool = [i[1] for i in data]
y_college = [i[2] for i in data]

ax.plot(x_label,y_highschool,label="High School Graduates")
ax.plot(x_label,y_college,label="College Graduates")

ax.set_title("Increase in the number of High School and College Graduates between 2001 and 2005")
ax.set_xlabel('Year')
ax.set_ylabel('Number of Graduates')
ax.legend()

for i in range(len(x_label)):
    ax.annotate(y_highschool[i],xy=(x_label[i],y_highschool[i]))
    ax.annotate(y_college[i],xy=(x_label[i],y_college[i]))

ax.grid(linestyle='--')
ax.set_xticks(x_label)
plt.tight_layout()
plt.savefig('line chart/png/510.png')
plt.cla()