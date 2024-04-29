
import matplotlib.pyplot as plt
import pandas as pd
data = {'Region':['North','South','East','West'],
        'Production A(tonnes)':[3000,2500,2700,2000],
        'Production B(tonnes)':[3500,3800,4000,4500],
        'Production C(tonnes)':[2700,3000,3200,3500]}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))

plt.title("Production output in three categories by region in 2021")

ax = plt.subplot()

plt.bar(df['Region'], df['Production A(tonnes)'], label='Production A', width=0.2)
plt.bar(df['Region'], df['Production B(tonnes)'], bottom=df['Production A(tonnes)'], label='Production B', width=0.2)
plt.bar(df['Region'], df['Production C(tonnes)'], bottom=df['Production B(tonnes)']+df['Production A(tonnes)'], label='Production C', width=0.2)

ax.set_xticks(df['Region'])
ax.set_xticklabels(df['Region'], rotation=90, wrap=True)

plt.legend()

plt.tight_layout()
plt.savefig('bar chart/png/514.png')
plt.clf()