
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot(111)
x1=[2020,2021,2022,2023]
y1=[10,12,14,16]
y2=[100,120,140,160]
y3=[90,108,126,144]
ax.bar(x1,y1,width=0.4,label='Growth Rate',color='#ff8000')
ax.bar(x1,y2,width=0.4,bottom=y1,label='Income(billion USD)',color='#00b8ff')
ax.bar(x1,y3,width=0.4,bottom=y2,label='Expenses(billion USD)',color='#ff0000')
ax.set_xticks(x1)
plt.title('Business growth rate and financial performance from 2020 to 2023')
plt.legend(loc='best')
plt.tight_layout()
fig.savefig('bar chart/png/281.png')
plt.close()