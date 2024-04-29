
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.set_title('Total and Retail vs E-Commerce Purchases from 2019 to 2022')
ax.set_xlabel('Year')
ax.set_ylabel('Total Purchases(million units)') 
ax.set_xticks([2019, 2020, 2021, 2022])
ax.plot([2019, 2020, 2021, 2022], [100, 120, 90, 140], color='red', label='Total Purchases')
ax.plot([2019, 2020, 2021, 2022], [80, 90, 70, 100], color='green', label='Purchases From Retail Store')
ax.plot([2019, 2020, 2021, 2022], [20, 30, 20, 40], color='blue', label='Purchases From E-Commerce')
ax.legend(loc='upper left', bbox_to_anchor=(1,1), borderaxespad=0., ncol=1, fancybox=True, shadow=True)
for a,b,c,d in zip([2019, 2020, 2021, 2022], [100, 120, 90, 140], [80, 90, 70, 100], [20, 30, 20, 40]):
    ax.annotate('Total:%s\nRetail:%s\nE-Commerce:%s' % (b,c,d), xy=(a, b), xytext=(a, b+2),rotation=45,ha='center',va='top',wrap=True)
plt.tight_layout()
plt.savefig('line chart/png/534.png')
plt.clf()