
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# plotting data
year = [2018, 2019, 2020, 2021]
net_profit = [15.2, 20.4, 23.8, 25.9]
expenses = [25, 30, 35, 40]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting data
ax.bar(year, net_profit, color='green', label='Net Profit')
ax.bar(year, expenses, bottom=net_profit, color='red', label='Expenses')

# Formatting
fmt = '$%.0fM'
tick = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

for i, v in enumerate(net_profit):
    ax.text(year[i] - 0.2, v/2, str(v), color='white', fontweight='bold')

for i, v in enumerate(expenses):
    ax.text(year[i] - 0.2, v/2 + net_profit[i], str(v), color='white', fontweight='bold')

# Labels, title and legend
ax.set_title('Net Profit and Expenses of a Business from 2018 to 2021')
ax.set_xlabel('Year')
ax.set_ylabel('Revenue (Million)')
ax.legend(loc='upper right')

# Grid lines
ax.grid(linestyle='--')

# Adjustment
fig.tight_layout()
plt.xticks(year)

# Save figure
plt.savefig('Bar Chart/png/228.png')

# Clear the current image state
plt.clf()