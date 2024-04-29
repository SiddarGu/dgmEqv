
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(10,4))
ax=fig.add_subplot(111)
x=['2019','2020','2021']
y1=[20,22,24]
y2=[18,20,22]
ax.bar(x,y1,bottom=y2,label='Revenue',width=0.5,edgecolor='black')
ax.bar(x,y2,label='Expenses',width=0.5,edgecolor='black')
ax.legend(loc='upper center')
ax.set_title('Revenue and Expenses of a company from 2019 to 2021')
ax.set_xlabel('Year')
ax.set_ylabel('Amount(billion)')
ax.set_xticks(x)
ax.annotate('20',xy=(0,20),xytext=(-0.3,20.8))
ax.annotate('18',xy=(0,18),xytext=(-0.3,18.8))
ax.annotate('22',xy=(1,22),xytext=(0.2,22.8))
ax.annotate('20',xy=(1,20),xytext=(0.2,20.8))
ax.annotate('24',xy=(2,24),xytext=(0.6,24.8))
ax.annotate('22',xy=(2,22),xytext=(0.6,22.8))
plt.tight_layout()
plt.savefig('Bar Chart/png/501.png')
plt.clf()