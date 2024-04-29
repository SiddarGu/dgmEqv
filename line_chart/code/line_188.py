
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
ax = plt.subplot()

x = [2009, 2010, 2011, 2012, 2013, 2014]
y1 = [1000, 1100, 1200, 1300, 1400, 1500]
y2 = [80, 82, 84, 86, 88, 90]
y3 = [20, 18, 16, 14, 12, 10]

ax.plot(x, y1, color='blue', marker='o', linestyle='--', label='Enrolled Students(thousands)')
ax.plot(x, y2, color='red', marker='^', linestyle='-.', label='Graduation Rate(%)')
ax.plot(x, y3, color='green', marker='s', linestyle=':', label='Dropout Rate(%)')

ax.set_title('The Change of Enrollment and Graduation Rates in Universities in the US from 2009 to 2014')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Students(thousands)/Rate(%)')

plt.xticks(x)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/187.png')
plt.clf()