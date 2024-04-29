
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Data
Year = [2019, 2020, 2021, 2022]
GDP = [22, 20, 21, 22]
Interest_Rates = [2.5, 0.25, 0.5, 1.0]
Inflation_Rates = [2.3, 1.2, 1.7, 2.0]

# Plot
ax.bar(Year, GDP, label='GDP(trillion USD)', bottom=Interest_Rates, width=0.2, color='g')
ax.bar(Year, Interest_Rates, label='Interest Rates(%)', bottom=Inflation_Rates, width=0.2, color='y')
ax.bar(Year, Inflation_Rates, label='Inflation Rates(%)', width=0.2, color='r')

# Labels
ax.set_title("Economic indicators of GDP, Interest Rates, and Inflation Rates from 2019 to 2022")
ax.set_xticks(Year)
ax.set_xlabel('Year')
ax.set_ylabel('Values')

# annotate
for i in range(4):
    ax.annotate(GDP[i], (Year[i], GDP[i]/2+Interest_Rates[i]), ha='center', va='center')
    ax.annotate(Interest_Rates[i], (Year[i], Interest_Rates[i]/2+Inflation_Rates[i]), ha='center', va='center')
    ax.annotate(Inflation_Rates[i], (Year[i], Inflation_Rates[i]/2), ha='center', va='center')

# Legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=3, fancybox=True, shadow=True)

# Adjustments
fig.tight_layout()

# Save
fig.savefig('Bar Chart/png/608.png')

# Clear
plt.cla()