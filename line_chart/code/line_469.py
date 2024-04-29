
import matplotlib.pyplot as plt
import pandas as pd

data = [[2001,5000,10000],
        [2002,5300,9000],
        [2003,5500,8200],
        [2004,6000,7600],
        [2005,6500,7000],
        [2006,7000,6500]]

df = pd.DataFrame(data, columns = ['Year', 'Criminal Cases', 'Civil Cases'])

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.plot('Year', 'Criminal Cases', data=df, label='Criminal Cases', color='red', marker='o')
ax.plot('Year', 'Civil Cases', data=df, label='Civil Cases', color='blue', marker='o')
ax.set_title('Annual criminal and civil cases in the US from 2001 to 2006')
ax.set_xlabel('Year')
ax.set_ylabel('Cases')
ax.legend()
ax.grid(axis='y')
plt.xticks(df['Year'])
plt.tight_layout()
plt.savefig('line chart/png/95.png')
plt.clf()