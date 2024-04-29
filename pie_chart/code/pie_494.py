

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure
fig = plt.figure()
ax = fig.add_subplot()

# Data
tax_brackets = ['0-19,000','19,001-77,000','77,001-160,000','160,001-320,000','320,001-400,000','400,001 and above']
percentages = [10,15,25,28,33,39]

# Plot
ax.pie(percentages, labels=tax_brackets, autopct='%1.1f%%', startangle=90, textprops={'rotation': 0, 'wrap': True}, shadow=True)
ax.set_title('Percentage of Tax Rates in the US, 2023', fontsize=14)

# Legend
red_patch = mpatches.Patch(color='red', label='Tax Brackets')
ax.legend(handles=[red_patch], loc='lower right')

# Adjust figure parameters
fig.tight_layout()
fig.set_figwidth(8)
fig.set_figheight(6)

# Save graph
plt.savefig('pie chart/png/293.png')

# Clear state
plt.clf()