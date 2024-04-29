
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(1,1,1)

x_data=['2018','2019','2020','2021','2022']
y1_data=[20,22,21,23,25]
y2_data=[4,5,6,7,8]
y3_data=[2,3,4,5,6]

ax.plot(x_data, y1_data, label='Tax Rate', linestyle='--', marker='o', color='green')
ax.plot(x_data, y2_data, label='Unemployment Rate', linestyle=':', marker='s', color='blue')
ax.plot(x_data, y3_data, label='Inflation Rate', linestyle='-', marker='^', color='red')

plt.title('Tax, Unemployment, and Inflation Rates in the US from 2018 to 2022')
ax.set_xticks(x_data)
ax.set_xlabel('Year')
ax.set_ylabel('Rate (%)')

ax.xaxis.set_major_formatter(ticker.FixedFormatter(x_data))
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}%'))
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/394.png')
plt.show()
plt.clf()