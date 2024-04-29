
import matplotlib.pyplot as plt
import pandas as pd

data = {'Location':['USA','UK','Germany','France'],
        'Football Fanbase':[25000,30000,28000,27000],
        'Cricket Fanbase':[10000,12000,11000,15000]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(df['Location'], df['Football Fanbase'], width=0.3, label='Football Fanbase')
ax.bar(df['Location'], df['Cricket Fanbase'], width=0.3, bottom=df['Football Fanbase'], label='Cricket Fanbase')

ax.set_title('Fanbase of Football and Cricket in four countries in 2021')
ax.set_xlabel('Location')
ax.set_ylabel('Number of Fans')

ax.set_xticks(df['Location'])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()

plt.savefig('bar chart/png/539.png')
plt.clf()