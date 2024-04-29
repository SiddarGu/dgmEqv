
import matplotlib.pyplot as plt
import numpy as np

month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
online_orders = np.array([500,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600])
retail_store_orders = np.array([800,700,600,400,900,800,700,600,500,400,300,200])

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

ax.plot(month, online_orders, label="Online Orders", color="red", linewidth=2.0)
ax.plot(month, retail_store_orders, label="Retail Store Orders", color="blue", linewidth=2.0)
ax.set_title('Comparison of Online and Retail Store Orders in 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Orders')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=2)
plt.xticks(month)
plt.tight_layout()
plt.savefig('line chart/png/501.png')
plt.clf()