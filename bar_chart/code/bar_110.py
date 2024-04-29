
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
bar_width = 0.4
country = ['USA', 'UK', 'Germany', 'France']
retail_sales = [8.0, 5.4, 7.2, 4.6]
e_commerce_sales = [3.2, 2.6, 2.8, 2.2]
rects1 = ax.bar(country, retail_sales, bar_width, label='Retail Sales')
rects2 = ax.bar(country, e_commerce_sales, bar_width, bottom=retail_sales, label='E-commerce Sales')
ax.set_xticks(country)
ax.set_title('Comparison of Retail and E-commerce Sales in four countries in 2021', fontsize=16)
ax.set_ylabel('Sales (billion)', fontsize=12)
ax.legend(fontsize=12)
plt.tight_layout()
plt.savefig('bar chart/png/552.png')
plt.clf()