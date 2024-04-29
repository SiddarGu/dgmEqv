

import matplotlib.pyplot as plt

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
online_sales = [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200]
retail_store_sales = [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
ax.plot(month, online_sales, label='Online Sales')
ax.plot(month, retail_store_sales, label='Retail Store Sales')
ax.set_xticks(month)
ax.set_title('Comparison between Online and Retail Store Sales in 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Sales(million dollars)')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/527.png')
plt.clf()