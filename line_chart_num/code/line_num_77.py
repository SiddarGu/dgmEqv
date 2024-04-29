
import matplotlib.pyplot as plt 
import numpy as np

# set the figure size
plt.figure(figsize=(10,6))

# parse the data
year = [2020, 2021, 2022, 2023, 2024]
tax_revenue = [300, 320, 340, 360, 380]
gov_spending = [400, 450, 500, 550, 600]

# plot the data
plt.plot(year, tax_revenue, color='orange', label='Tax Revenue')
plt.plot(year, gov_spending, color='green', label='Government Spending')

# set the title of the figure
plt.title('Tax Revenue and Government Spending in the US from 2020 to 2024')

# add legend
plt.legend(loc='best')

# add grids
plt.grid(linestyle='--')

# add label for each point
for x, y in zip(year, tax_revenue):
    plt.annotate(y, xy=(x, y), xytext=(-20, 10), textcoords='offset points')
for x, y in zip(year, gov_spending):
    plt.annotate(y, xy=(x, y), xytext=(-20, 10), textcoords='offset points')

# set xticks
plt.xticks(year)

# adjust the picture 
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/465.png')

# clear the figure
plt.clf()