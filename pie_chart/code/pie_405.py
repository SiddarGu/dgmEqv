
import matplotlib.pyplot as plt
import pandas as pd

data = {'Tax Categories':['Income Tax','Property Tax','Sales Tax','Excise Tax', 'Other Taxes'],
        'Percentage':[45,25,17,9,4]}

df = pd.DataFrame(data)

plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.set_title("Taxation Distribution in the USA, 2023")

wedges, texts, autotexts = ax.pie(df['Percentage'],labels=df['Tax Categories'],autopct='%1.1f%%',
                                  textprops={'fontsize': 12},shadow=True, startangle=90)
plt.setp(autotexts, size=14, weight="bold")

for t in texts:
    t.set_size('large')
    t.set_weight('bold')

for w in wedges:
    w.set_linewidth(1.5)
    w.set_edgecolor('black')

ax.legend(df['Tax Categories'],
          title="Tax Categories",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.savefig('pie chart/png/395.png')
plt.clf()