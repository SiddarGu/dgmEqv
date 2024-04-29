
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6)) 
ax = plt.subplot(111)

x = [2015,2016,2017,2018,2019]
y1 = [1000,1100,1200,1300,1400]
y2 = [500,600,700,800,900]
y3 = [100,120,140,160,180]
y4 = [400,480,560,640,720]

ax.plot(x, y1, color='skyblue', linewidth=2, label='Gross Profit')
ax.plot(x, y2, color='olive', linestyle='-.', linewidth=2, label='Operational Expenses')
ax.plot(x, y3, color='deeppink', linestyle='--', linewidth=2, label='Administrative Expenses')
ax.plot(x, y4, color='green', linestyle='-', linewidth=2, label='Net Profit')

ax.set_xticks([2015,2016,2017,2018,2019]) 
ax.set_title('Net Profit Margin of a Company from 2015 to 2019')
ax.set_xlabel('Year')
ax.set_ylabel('million dollars')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/503.png')
plt.clf()