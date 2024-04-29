
import matplotlib.pyplot as plt
import numpy as np

Month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August')
Electricity_Consumption = np.array([20000, 18000, 22000, 21000, 23000, 19000, 25000, 21000])
Electricity_Cost = np.array([1200, 1000, 1300, 1500, 1700, 1200, 1500, 1600])

fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot()
ax.plot(Month,Electricity_Consumption, label='Electricity Consumption (KW-h)')
ax.plot(Month,Electricity_Cost, label='Electricity Cost (USD)')
ax.set_title('Household electricity consumption and cost from January to August 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Electricity Consumption & Cost')
ax.legend()
ax.grid()
for x,y in zip(Month,Electricity_Consumption):
    ax.annotate(str(y), xy=(x,y), xytext=(-5,5), textcoords='offset points')
for x,y in zip(Month,Electricity_Cost):
    ax.annotate(str(y), xy=(x,y), xytext=(-5,5), textcoords='offset points')
plt.xticks(Month, rotation='vertical')
plt.tight_layout()
plt.savefig('line chart/png/281.png')
plt.clf()