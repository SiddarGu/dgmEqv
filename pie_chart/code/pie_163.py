

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(figsize=(8, 6))
plt.subplot(1, 1, 1)

# The data
Economic_Sectors=['Agriculture','Manufacturing','Services','Mining']
percentage=[25,20,50,5]

# The pie chart
plt.pie(percentage, labels=Economic_Sectors,autopct='%1.1f%%',
        shadow=True, startangle=90,
        wedgeprops={'linewidth': 2, 'edgecolor': 'k'})

plt.title("Economic Sectors Distribution in the USA, 2023")
plt.legend(bbox_to_anchor=(1.05,1))

# Rotate the labels of x-axis
plt.xticks(rotation=-45, ha='left')

# Automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Save the figure
plt.savefig("pie chart/png/513.png")

# Clear the current image state
plt.clf()