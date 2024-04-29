
import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
month = ['January','February','March','April','May','June']
online_sales = [1000,1500,2000,1700,1900,2100]
store_sales = [1200,1000,800,1100,900,1000]
total_sales = [2200,2500,2800,2800,2800,3100]
plt.plot(month,online_sales,label='online sales')
plt.plot(month,store_sales,label='store sales')
plt.plot(month,total_sales,label='total sales')
plt.xticks(month,rotation=45)
plt.xlabel('Month')
plt.ylabel('Sales (million dollars)')
plt.title('Total sales of online and store sales in the first half year of 2021')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/392.png')
plt.clf()