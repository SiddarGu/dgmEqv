
import matplotlib.pyplot as plt
import numpy as np

data = [[2019,25,2000,500],[2020,27,2200,600],[2021,30,2500,700],[2022,32,2700,800]]

x = np.array([data[0][0],data[1][0],data[2][0],data[3][0]])
y1 = np.array([data[0][1],data[1][1],data[2][1],data[3][1]])
y2 = np.array([data[0][2],data[1][2],data[2][2],data[3][2]])
y3 = np.array([data[0][3],data[1][3],data[2][3],data[3][3]])

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111)
ax.plot(x, y1, color='#FF9900', linestyle='-.', label='Tax Rate(%)', linewidth=3)
ax.plot(x, y2, color='#6699CC', linestyle='-', label='Expenditure(billion dollars)', linewidth=3)
ax.plot(x, y3, color='#CC0033', linestyle=':', label='Savings(billion dollars)', linewidth=3)

ax.set_title('Changes in Tax Rate and Government Expenditures in the USA from 2019 to 2022', fontsize=20)
ax.set_xlabel('Year', fontsize=15)
ax.set_xlim(2019, 2022)
ax.set_xticks(x)
ax.set_ylabel('Values', fontsize=15)
ax.set_ylim(0, 3000)

ax.grid(axis='y', linestyle='--', linewidth=1, alpha=0.5)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)

for i in range(len(x)):
    ax.annotate(str(data[i][1])+'%', xy=(x[i], y1[i]), xytext=(x[i], y1[i] + 100), fontsize=13, rotation=30, wrap=True)
    ax.annotate(str(data[i][2]), xy=(x[i], y2[i]), xytext=(x[i], y2[i] + 100), fontsize=13, rotation=30, wrap=True)
    ax.annotate(str(data[i][3]), xy=(x[i], y3[i]), xytext=(x[i], y3[i] - 100), fontsize=13, rotation=30, wrap=True)

plt.tight_layout()

plt.savefig('line chart/png/108.png', dpi=300)

plt.clf()