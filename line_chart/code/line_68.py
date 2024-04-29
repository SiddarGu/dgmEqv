
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
x = ['2020','2021','2022','2023']
y1 = [10000,12000,14000,16000]
y2 = [4000,5000,6000,7000]
y3 = [6000,7000,8000,9000]
ax.plot(x, y1, label='Revenue', marker='s', color='#2196F3')
ax.plot(x, y2, label='Profit', marker='o', color='#F44336')
ax.plot(x, y3, label='Expense', marker='*', color='#FF9800')
ax.set_title('Financial Performance of XYZ Company, Year 2020-2023')
ax.set_xlabel('Year')
ax.set_ylabel('Amount')
ax.legend(loc='best', ncol=3, fontsize='medium', columnspacing=1, labelspacing=1, frameon=True)
plt.xticks(x)
plt.tight_layout()
plt.savefig('line chart/png/38.png')
plt.clf()