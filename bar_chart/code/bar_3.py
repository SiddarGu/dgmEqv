
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

#data
Country = ["USA","UK","Germany","France"]
Government_Spending = [800, 600, 400, 500]
Tax_Revenue = [900, 700, 500, 600]

#plot
fig, ax = plt.subplots(figsize=(8,8))
plt.title('Government Spending and Tax Revenue in Four Countries in 2021')
ax.bar(Country, Government_Spending, bottom=Tax_Revenue, label='Government Spending')
ax.bar(Country, Tax_Revenue, label='Tax Revenue')
ax.set_ylabel('Billion')
ax.xaxis.set_ticks(np.arange(len(Country)))
ax.set_xticklabels(Country,rotation=90, fontsize=8)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/397.png')
plt.cla()