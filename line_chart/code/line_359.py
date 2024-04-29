
import matplotlib.pyplot as plt
import pandas as pd

data = {'Year':[2011,2012,2013,2014,2015],
        'Donations (USD)':[30000,35000,40000,45000,50000],
        'Volunteer Hours':[20000,25000,30000,35000,40000]}
df = pd.DataFrame(data)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.plot(df['Year'], df['Donations (USD)'], linestyle='-', marker='^', color='red', label='Donations (USD)')
ax.plot(df['Year'], df['Volunteer Hours'], linestyle='-', marker='o', color='blue', label='Volunteer Hours')
ax.set_xticks(df['Year'])
ax.set_title('Increase in donations and volunteer hours for a non-profit organization from 2011-2015')
ax.set_xlabel('Year')
ax.set_ylabel('Amount (USD)')
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('line chart/png/525.png')
plt.clf()