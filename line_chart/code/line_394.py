
import matplotlib.pyplot as plt
import pandas as pd

data = [['January', 1000, 800, 1200, 1500],
        ['February', 1200, 900, 1100, 1600],
        ['March', 800, 1100, 1300, 1200],
        ['April', 1500, 1200, 1400, 800]]

df = pd.DataFrame(data, columns = ['Month', 'Production A(units)', 'Production B(units)', 'Production C(units)', 'Production D(units)'])

plt.figure(figsize=(8, 6))
plt.title('Monthly production of four types of products for 2021')
plt.plot(df['Month'], df['Production A(units)'], label='Production A(units)')
plt.plot(df['Month'], df['Production B(units)'], label='Production B(units)')
plt.plot(df['Month'], df['Production C(units)'], label='Production C(units)')
plt.plot(df['Month'], df['Production D(units)'], label='Production D(units)')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Month')
plt.ylabel('Units')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/231.png')
plt.clf()