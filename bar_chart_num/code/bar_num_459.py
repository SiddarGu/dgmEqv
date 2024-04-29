
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

department = ["IT", "HR", "Finance", "Marketing"]
staff = [40, 35, 20, 30]
full_time = [30, 25, 15, 25]
part_time = [10, 10, 5, 5]

x = np.arange(len(department))
p1 = ax.bar(x, staff, color='#f45c42', label="Staff")
p2 = ax.bar(x, full_time, bottom=staff, color='#6c5ce7', label="Full-time")
p3 = ax.bar(x, part_time, bottom=np.array(staff)+np.array(full_time), color='#2e86de', label="Part-time")

ax.set_xticks(x)
ax.set_xticklabels(department, rotation=45)
ax.set_title("Number of staff and full-time and part-time employees by department in 2021")
ax.legend(loc="best")

for i,j in zip(x,staff):
    ax.annotate('{}'.format(j), xy=(i-0.2,j+3))
for i,j in zip(x,full_time):
    ax.annotate('{}'.format(j), xy=(i-0.2,j+3+staff[i]))
for i,j in zip(x,part_time):
    ax.annotate('{}'.format(j), xy=(i-0.2,j+3+staff[i]+full_time[i]))

fig.tight_layout()
plt.savefig("Bar Chart/png/471.png")
plt.clf()