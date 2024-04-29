
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import numpy as np

fig = plt.figure(figsize=(13,5))
ax = fig.add_subplot(111)

Country = ['USA','Canada','Mexico','Brazil']
No_of_Laws = [50,40,45,55]
No_of_Amendments = [20,18,19,21]

ax.bar(Country, No_of_Laws, label="No. of Laws", bottom=No_of_Amendments)
ax.bar(Country, No_of_Amendments, label="No. of Amendments")
for i, v in enumerate(No_of_Laws):
    ax.text(i-0.1, v/2+No_of_Amendments[i], str(v), color='black', fontweight='bold')
for i, v in enumerate(No_of_Amendments):
    ax.text(i-0.1, v/2, str(v), color='black', fontweight='bold')

ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}')) 
ax.set_xlabel('Country')
ax.set_ylabel('Number of Laws and Amendments')
ax.set_title("Number of laws and amendments in four countries in 2021")
ax.set_xticks(np.arange(len(Country)))
ax.set_xticklabels(Country)
ax.legend()
plt.tight_layout()
plt.savefig(r'Bar Chart/png/94.png')
plt.clf()