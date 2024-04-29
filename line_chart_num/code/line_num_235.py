
import matplotlib.pyplot as plt
import pandas as pd

data = [['2020 Q1',200,150,60],
        ['2020 Q2',180,140,50],
        ['2020 Q3',210,130,45],
        ['2020 Q4',220,160,55]]

df = pd.DataFrame(data, columns=['Period','Car Sales(thousands)','Truck Sales(thousands)','Motorcycle Sales(thousands)'])

fig,ax = plt.subplots(figsize=(15,7))

ax.plot(df['Period'], df['Car Sales(thousands)'], marker='o', color='red', label='Car Sales')
ax.plot(df['Period'], df['Truck Sales(thousands)'], marker='o', color='blue', label='Truck Sales')
ax.plot(df['Period'], df['Motorcycle Sales(thousands)'], marker='o', color='green', label='Motorcycle Sales')

ax.set_title('Vehicle Sales in 2020 by Quarter', fontsize=15)
ax.set_xlabel('Period')
ax.set_ylabel('Sales (thousands)')
plt.xticks(df['Period'], rotation=45)
ax.grid(True)

for i, txt in enumerate(df['Car Sales(thousands)']):
    ax.annotate(txt, (df['Period'][i], df['Car Sales(thousands)'][i]), xytext=(10,-10), textcoords='offset points')
for i, txt in enumerate(df['Truck Sales(thousands)']):
    ax.annotate(txt, (df['Period'][i], df['Truck Sales(thousands)'][i]), xytext=(10,-10), textcoords='offset points')
for i, txt in enumerate(df['Motorcycle Sales(thousands)']):
    ax.annotate(txt, (df['Period'][i], df['Motorcycle Sales(thousands)'][i]), xytext=(10,-10), textcoords='offset points')

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)
plt.tight_layout()
plt.savefig('line chart/png/321.png', dpi=300)
plt.clf()