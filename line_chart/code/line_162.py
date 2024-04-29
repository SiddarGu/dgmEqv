
import matplotlib.pyplot as plt                         
plt.figure(figsize=(10,7))
ax = plt.subplot()

x = [2015,2016,2017,2018,2019]
y1 = [1000,1100,1200,1400,1500]
y2 = [80,85,90,95,98]
y3 = [50,75,100,120,150]
ax.plot(x, y1, color='#1f77b4', linestyle='--', marker='o', label='Employees')
ax.plot(x, y2, color='#ff7f0e', linestyle='--', marker='o', label='Retention Rate')
ax.plot(x, y3, color='#2ca02c', linestyle='--', marker='o', label='Training Hours')

plt.title('Employee Retention and Training Hours in a Company from 2015 to 2019')
ax.set_xticks(x)
plt.xlabel('Year')
plt.ylabel('Count (thousands)')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/250.png')
plt.clf()