
import matplotlib.pyplot as plt
import pandas as pd

data = {'Year':[2001,2002,2003,2004,2005],'Number of Employees':[1000,1200,1500,1800,2000],'Percentage of Female Employees':[30,35,40,45,50]}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
ax = plt.subplot(1, 1, 1)
ax.plot(df['Year'], df['Number of Employees'], marker='o', color='blue', label='Number of Employees')
ax.plot(df['Year'], df['Percentage of Female Employees'], marker='o', color='red', label='Percentage of Female Employees')
ax.set_title('Gender Diversity in the Workplace from 2001 to 2005')
ax.set_xlabel('Year')
ax.set_ylabel('Number & Percentage')
ax.legend(loc='upper center')
plt.xticks(df['Year'])
plt.tight_layout()
plt.savefig('line chart/png/279.png')
plt.clf()