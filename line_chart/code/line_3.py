
import matplotlib.pyplot as plt
import pandas as pd

data = [[2020, 20000, 500, 10000000], 
        [2021, 25000, 600, 15000000], 
        [2022, 30000, 650, 18000000], 
        [2023, 35000, 700, 20000000]]

df = pd.DataFrame(data, columns=['Year', 'Number of Shops', 'Online Sales(billion dollars)', 'Online Customers'])

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

ax.plot(df['Year'], df['Number of Shops'], label='Number of Shops')
ax.plot(df['Year'], df['Online Sales(billion dollars)'], label='Online Sales(billion dollars)')
ax.plot(df['Year'], df['Online Customers'], label='Online Customers')

ax.set_xticks(df['Year'])

ax.set_title('Growth of Retail and E-commerce between 2020 and 2023')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Shops, Online Sales(billion dollars), Online Customers')

ax.legend(loc='upper left', bbox_to_anchor=(1,1), borderaxespad=0.)

fig.tight_layout()

plt.savefig('line chart/png/175.png')
plt.clf()