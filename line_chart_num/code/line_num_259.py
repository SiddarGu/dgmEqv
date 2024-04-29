
import matplotlib.pyplot as plt
import pandas as pd

data = [[2001, 10000, 1000], [2002, 12000, 1500], [2003, 14000, 2000], [2004, 15000, 2500], [2005, 17000, 3000], [2006, 18000, 3500], [2007, 20000, 4000]]

df = pd.DataFrame(data,columns=['Year','Number of Cases','Number of Lawyers'])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

ax.plot(df['Year'], df['Number of Cases'], label='Number of Cases', marker="o", color='red')
ax.plot(df['Year'], df['Number of Lawyers'], label='Number of Lawyers', marker="^", color='blue')

for i, txt in enumerate(df['Number of Cases']):
    ax.annotate(txt, (df['Year'][i], df['Number of Cases'][i]), rotation=90, fontsize=12)
for i, txt in enumerate(df['Number of Lawyers']):
    ax.annotate(txt, (df['Year'][i], df['Number of Lawyers'][i]), rotation=90, fontsize=12)

ax.legend(loc='best')
ax.set_title('Annual litigation and lawyer growth in the United States')
ax.set_xticks(df['Year'])
ax.grid(True)
plt.tight_layout()

fig.savefig('line chart/png/523.png')
plt.clf()