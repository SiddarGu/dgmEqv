
import matplotlib.pyplot as plt
import numpy as np

# data
Year = np.array([2018,2019,2020,2021])
Traffic_Violations = np.array([2000,2500,3000,3500])
Civil_Suits = np.array([500,600,700,800])
Criminal_Suits = np.array([800,900,1000,1100])

# plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.set_title('Number of legal cases in the US between 2018-2021')
ax.plot(Year, Traffic_Violations, label='Traffic Violations', marker='o')
ax.plot(Year, Civil_Suits, label='Civil Suits', marker='o')
ax.plot(Year, Criminal_Suits, label='Criminal Suits', marker='o')
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
ax.set_xlabel('Year')
ax.set_ylabel('Number of Cases')
ax.grid(axis='y', linestyle='--')

for x, y in zip(Year, Traffic_Violations):
    ax.annotate(str(y), xy=(x, y), xycoords='data', xytext=(-20, 10), 
                textcoords='offset points', fontsize=10,
                arrowprops=dict(arrowstyle="->"))

for x, y in zip(Year, Civil_Suits):
    ax.annotate(str(y), xy=(x, y), xycoords='data', xytext=(-20, 10), 
                textcoords='offset points', fontsize=10,
                arrowprops=dict(arrowstyle="->"))

for x, y in zip(Year, Criminal_Suits):
    ax.annotate(str(y), xy=(x, y), xycoords='data', xytext=(-20, 10), 
                textcoords='offset points', fontsize=10,
                arrowprops=dict(arrowstyle="->"))

ax.set_xticks(Year)
ax.xaxis.set_tick_params(rotation=45)
plt.tight_layout()
plt.savefig('line chart/png/613.png')
plt.cla()