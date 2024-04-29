
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,6))
attendance = np.array([[1000, 800, 1200],
                     [1200, 1100, 1600],
                     [800, 900, 1300],
                     [1500, 1200, 1400]])

labels = np.array(['Football', 'Baseball', 'Basketball'])
x_pos = np.arange(len(labels))

years = np.array(['2001','2002','2003','2004'])
y_pos = np.arange(len(years))

for i, c in enumerate(attendance.T):
    plt.plot(y_pos, c, label=labels[i])

plt.xticks(y_pos, years, rotation=45)
plt.title("Comparison of Attendance of Major Sports Leagues in the United States from 2001 to 2004")
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/68.png')
plt.clf()