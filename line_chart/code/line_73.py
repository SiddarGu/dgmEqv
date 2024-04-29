
import matplotlib.pyplot as plt
import numpy as np

data = [[2001, 80, 70, 65, 60],
        [2002, 75, 65, 70, 55], 
        [2003, 70, 60, 75, 50], 
        [2004, 65, 50, 85, 45]]

years, enrollmentA, enrollmentB, enrollmentC, enrollmentD = zip(*data)

plt.figure(figsize=(10,5))
ax = plt.subplot(111)
ax.set_title('Changes in enrollment rate of four educational institutions from 2001 to 2004')
ax.plot(years, enrollmentA, label = 'Enrollment A', color='red', marker='o')
ax.plot(years, enrollmentB, label = 'Enrollment B', color='blue', marker='o')
ax.plot(years, enrollmentC, label = 'Enrollment C', color='green', marker='o')
ax.plot(years, enrollmentD, label = 'Enrollment D', color='orange', marker='o')
ax.set_xticks(years)
ax.set_xlabel('Year')
ax.set_ylabel('Enrollment(%)')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), shadow=True, ncol=4)
plt.tight_layout()
plt.savefig('line chart/png/402.png')
plt.clf()