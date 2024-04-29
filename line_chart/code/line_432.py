
import matplotlib.pyplot as plt
import numpy as np

data = [[2020,2,1.5,2.5],[2021,2.5,1.7,2.8],[2022,2.2,2.0,3.0],[2023,2.8,2.2,3.5]]
year = [i[0] for i in data]
A = [i[1] for i in data]
B = [i[2] for i in data]
C = [i[3] for i in data]
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.plot(year,A,label='Stadium A')
ax.plot(year,B,label='Stadium B')
ax.plot(year,C,label='Stadium C')
ax.set_title('Attendance at Three Major Sporting Events')
ax.set_xlabel('Year')
ax.set_ylabel('Attendance (millions)')
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
ax.grid('True')
plt.xticks(year)
plt.tight_layout()
plt.savefig('line chart/png/379.png')
plt.clf()