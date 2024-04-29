
import matplotlib.pyplot as plt

plt.figure(figsize=(9,6))
plt.subplot()

year = [2018, 2019, 2020, 2021, 2022]
employees = [800, 900, 1000, 1100, 1200]
overtime = [100, 150, 200, 250, 300]

plt.plot(year, employees, label='Employees', marker='o', color='red')
plt.plot(year, overtime, label='Overtime', marker='o', color='blue')

plt.title('Changes in Employee Count and Overtime Hours in a Manufacturing Company from 2018 to 2022')
plt.xlabel('Year')
plt.ylabel('Number of Employees / Overtime Hours')
plt.xticks(year)
plt.legend(loc="center right")
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.tight_layout()
plt.savefig('line chart/png/1.png')
plt.clf()