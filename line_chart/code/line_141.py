
import matplotlib.pyplot as plt
import pandas as pd

data = {'Country':['US', 'China', 'India', 'UK', 'Germany'], 'Population':[330, 1400, 1350, 65, 83], 'GDP (billion dollars)':[21000, 13000, 3000, 2.8, 3.8]}
df = pd.DataFrame(data)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.set_title('Population and GDP of Major Countries in 2020')
ax.plot(df['Country'], df['Population'], label='Population')
ax.plot(df['Country'], df['GDP (billion dollars)'], label='GDP (billion dollars)')
ax.legend(loc='upper right', fontsize='large')
ax.set_xticks(df['Country'])
ax.tick_params(axis='x', rotation=45, labelsize='large')
plt.tight_layout()
plt.savefig('line chart/png/158.png')
plt.clf()