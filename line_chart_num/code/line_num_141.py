
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 8))
plt.subplot(1, 1, 1)

online_sales = [15, 17, 19, 21, 23, 25, 27, 29]
offline_sales = [14, 15, 17, 19, 21, 23, 25, 27]
total_sales = [29, 32, 36, 40, 44, 48, 52, 56]

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']

plt.plot(months, online_sales, label='Online Sales', marker='o', color='blue')
plt.plot(months, offline_sales, label='Offline Sales', marker='o', color='red')
plt.plot(months, total_sales, label='Total Sales', marker='o', color='green')

plt.title('Evolution of Retail and E-commerce sales in 2021')
plt.xlabel('Months')
plt.ylabel('Sales (billion dollars)')
plt.xticks(rotation=45)
plt.legend(loc='upper right', ncol=2, fontsize=10, bbox_to_anchor=(1.05, 1), borderaxespad=0.)

for a,b,c in zip(months,online_sales,offline_sales):
    plt.annotate('{}'.format(b), xy=(a, b), fontsize=9, xytext=(0, 7), rotation=45,
                 textcoords='offset points')
    plt.annotate('{}'.format(c), xy=(a, c), fontsize=9, xytext=(0, -7), rotation=45,
                 textcoords='offset points')

plt.tight_layout()
plt.savefig('./line chart/png/489.png')
plt.clf()