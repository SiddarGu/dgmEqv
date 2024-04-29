
import matplotlib.pyplot as plt

# create figure
plt.figure(figsize=(10, 8))

# set x, y, label and explode
x = ["Single-Family Homes","Townhomes","Condominiums","Multi-Family Homes"]
y = [60,15,15,10]
label = ["Single-Family Homes","Townhomes","Condominiums","Multi-Family Homes"]
explode = [0.1, 0, 0, 0]

# set font size
plt.rc('font', size=12)

# draw pie chart
plt.pie(y, explode=explode, labels=label,autopct='%1.1f%%', startangle=90, shadow=True, textprops={'fontsize': 12, 'color': 'black'})

# set title
plt.title("Distribution of Homeownership Types in the USA, 2023")

# set position of legend
plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1))

# set tight layout
plt.tight_layout()

# save the figure
plt.savefig('pie chart/png/38.png')

# clear the figure
plt.clf()