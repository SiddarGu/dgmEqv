
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot(111)
year = [2020, 2021, 2022, 2023]
revenue = [400, 450, 500, 550]
expenditure = [350, 400, 450, 500]
profit = [50, 50, 50, 50]
ax.bar(year, revenue, width=0.3, label='Revenue', color='blue')
ax.bar(year, expenditure, bottom=revenue, width=0.3, label='Expenditure', color='red')
ax.bar(year, profit, bottom=[i+j for i,j in zip(revenue, expenditure)], width=0.3, label='Profit', color='green')
ax.set_xticks(year)
ax.set_ylabel('million')
ax.set_title('Revenue, Expenditure and Profit of a Business from 2020 to 2023')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('bar chart/png/441.png')
plt.clf()