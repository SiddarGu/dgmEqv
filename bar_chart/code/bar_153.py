
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
ax = plt.subplot()
year = [2017, 2018, 2019, 2020]
employ_rate = [76, 78, 80, 82]
unemploy_rate = [7, 6, 4, 2]

ax.bar(year, employ_rate, width=0.5, color='b', label='Employment rate')
ax.bar(year, unemploy_rate, bottom=employ_rate, width=0.5, color='y', label='Unemployment rate')

ax.set_xlabel('Year')
ax.set_ylabel('Rate(%)')
ax.set_title('Employment and Unemployment rate in 2017-2020')
ax.legend(loc='upper left')
ax.set_xticks(year)
plt.tight_layout()
plt.savefig('bar chart/png/20.png')
plt.clf()