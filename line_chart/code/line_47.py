

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
online_shopping = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
in_store_shopping = [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()
ax.plot(months, online_shopping, color='red', label='Online Shopping')
ax.plot(months, in_store_shopping, color='blue', label='In-store Shopping')
ax.set_title('Change in Retail Shopping Trends in the US from January to December 2021')
ax.legend(loc='best')
ax.set_xticks(months)
plt.tight_layout()
plt.savefig('line chart/png/257.png')
plt.clf()