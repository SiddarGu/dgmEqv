
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = [[2019,1000,1200],
        [2020,1200,900],
        [2021,1100,1100],
        [2022,1300,1300],
        [2023,1400,1100]]

df = pd.DataFrame(data,columns=['Year','Online Sales(million dollars)','Store Sales(million dollars)'])

fig=plt.figure(figsize=(15,8))
ax=fig.add_subplot(1,1,1)
ax.set_title('Comparing Online and Store Sales in the Retail Industry from 2019 to 2023', fontsize=20)

ax.plot(df['Year'],df['Online Sales(million dollars)'],label='Online Sales(million dollars)',color='b', linewidth=1, marker='o', markersize=3)
ax.plot(df['Year'],df['Store Sales(million dollars)'],label='Store Sales(million dollars)',color='r', linewidth=1, marker='o', markersize=3)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Sales(million dollars)', fontsize=14)
ax.set_xticks(df['Year'])
ax.grid(True, linestyle='-', linewidth='0.3', color='#202020')
ax.legend(loc='upper left', fontsize=13, frameon=False)

fig.tight_layout()
plt.savefig('line chart/png/368.png')
plt.clf()